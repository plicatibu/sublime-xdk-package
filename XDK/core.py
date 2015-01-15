import sublime, sublime_plugin
import os
import json
import urllib.request
import sys
import re

### CONFIGURATION
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xdk_plugin.conf');
API_VERSION = '0.0.1'
DEBUG_ENABLED = True
MSGS = {
	'SPECIFIED_DIRECTORY_IS_NOT_XDK': 'Path specified in configuration is not Intel® XDK one. Please enter correct XDK folder in the prompt below.',
	'CAN_NOT_PARSE_SERVER_DATA': 'Can not parse XDK server data file.',
	'CAN_NOT_VALIDATE_SECRET_KEY': 'Can not authorize to Intel® XDK.',
	'XDK_CONNECTION_FAILED': 'Connection to XDK failed. Do you have Intel® XDK running?',
	'CAN_NOT_GET_FOLDER': 'Can not get current folder. Do you have project folder opened?',
	'CAN_NOT_PARSE_RESPONSE_JSON': 'Can not parse response JSON',
	'CAN_NOT_FIND_XDK': 'Can not find Intel® XDK installation'
}
### E.O. CONFIGURATION

def _print(*args):
	if DEBUG_ENABLED:
		print(*args)

class XDKException(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class XDKPluginCore:
	# contents of plugin's conf file
	config_contents = None
	# xdk system dir
	xdk_dir = None
	# path to server-data.txt file
	server_data_path = None
	# entrance point for plugin-listener
	plugin_base_path = None
	# entrace to xdk
	base_path = None

	auth_secret = None
	auth_cookie = None

	def make_request(self, addr, params={}, headers={}):
		_print('make_request: addr=', addr);
		if params:
			params['_api_version'] = API_VERSION
			params = json.dumps(params)
			_print('make_request: params=' + str(params))
			headers['Content-Type'] = 'application/json'
		else:
			params = ''


		request = urllib.request.Request(addr, params.encode('utf-8'), headers)
		response = urllib.request.urlopen(request)
		return response

	def invoke_command(self, cmd):
		def _make_request():
			try: 
				return self.make_request(self.plugin_base_path, cmd, {
					'Cookie' : self.auth_cookie
				})
			except urllib.error.HTTPError as e:
				_print("Caught HTTPError' " + str(e.code))
				if (int(e.code) == 401):
					_print('401, trying to get new one'); 
					self.reset_authorization()
					self.prepare()
					return self.make_request(self.plugin_base_path, cmd, {
						'Cookie' : self.auth_cookie
					})
				else:
					raise

		try:
			response = _make_request()
			content = response.read()
			_print('invoke_command: content=')
			_print(content);
			try:
				parsed = json.loads(content.decode())
			except:
				raise XDKException(MSGS['CAN_NOT_PARSE_RESPONSE_JSON'])
		
			if parsed.get('error'):
				raise XDKException(parsed.get('msg') or 'Unknown error')

		except XDKException as e:
			sublime.error_message(e.value)
		except:
			sublime.error_message(MSGS['XDK_CONNECTION_FAILED'])


	def get_data_path(self):
		p = sys.platform
		path = None
		if p == 'darwin' and os.getenv('HOME'):
			path = os.path.join(os.getenv('HOME'), 'Library', 'Application Support', 'XDK')
		elif p == 'win32' and os.getenv('LOCALAPPDATA'):
			path = os.path.join(os.getenv('LOCALAPPDATA'), 'XDK')
		elif p == 'linux2' and os.getenv('HOME'):
			path = os.path.join(os.getenv('HOME'), '.config', 'XDK')
		server_data = os.path.join(path, 'server-data.txt')
		if path is None or not os.path.isfile(server_data) or not os.access(server_data, os.R_OK):
			raise XDKException(MSGS['CAN_NOT_FIND_XDK']) 
		return path


	def load_config_data(self):
		if self.plugin_base_path is not None:
			_print('load_config_data: already has plugn_base_path')
			return

		_print('load_config_data: trying to read CONFIG_FILE=', CONFIG_FILE);
		with open(CONFIG_FILE, 'r') as f:
			self.config_contents = f.read();
		_print('load_config_data: CONFIG_FILE read')
		if not self.config_contents:
			self.find_xdk_installation()
		self.xdk_dir = self.config_contents.strip()
		_print('load_config_data: xdk_dir=' + self.xdk_dir)
		self.server_data_path = os.path.join(self.xdk_dir, 'server-data.txt')
		_print('load_config_data: server_data_path=', self.server_data_path)
		if not os.path.isfile(self.server_data_path):
			raise XDKException(MSGS['SPECIFIED_DIRECTORY_IS_NOT_XDK'])
		server_data_contents = None;
		with open(self.server_data_path, 'r') as f:
			server_data_contents = f.read()
		_print('load_config_data: server_data_contents=' + server_data_contents);	
		try:
			decoded = json.loads(server_data_contents.replace('[END]', ''))
			self.auth_secret = decoded['secret']
			self.base_path = 'http://localhost:' + str(decoded['port']);
			self.plugin_base_path = 'http://localhost:' + str(decoded['port']) + '/http-services/plugin-listener/plugin/entrance'
			_print('load_config_data: auth_secret=' + self.auth_secret);
			_print('load_config_data: base_path=' + self.base_path);
			_print('load_config_data: plugin_base_path=' + self.plugin_base_path);
		except:
			raise XDKException(MSGS['CAN_NOT_PARSE_SERVER_DATA']);

	def authorize(self):
		if self.auth_cookie is not None:
			_print('authorize: auth_cookie is not none');
			return 

		_print('authorize: making request to /validate');	
		response = self.make_request(self.base_path + '/validate', {}, {'x-xdk-local-session-secret': self.auth_secret })
		cookies = dict(response.info().items())
		_print('authorize: response.status=' + str(response.status))
		_print('authorize: cookies length=' + str(len(cookies)))
		if response.status != 200 or 'Set-Cookie' not in cookies: 
			raise XDKException(MSGS['CAN_NOT_VALIDATE_SECRET_KEY'])
		self.auth_cookie = cookies['Set-Cookie']
		_print('authorize: auth_cookie=', self.auth_cookie);

	def reset_authorization(self):
		self.xdk_dir = None
		self.auth_secret = None
		self.auth_cookie = None
		self.plugin_base_path = None
	
	def find_xdk_installation(self):
		_print('find_xdk_installation: self.xdk_dir=' + str(self.xdk_dir))
		if self.xdk_dir is not None:
			_print('find_xdk_installation: self.xdk_dir is not none')
			return self.xdk_dir 	
		path = self.get_data_path()
		_print('find_xdk_installation: found path' + path)
		with open(CONFIG_FILE, 'w') as f:
			f.write(path);		

	def prepare(self):
		try:
			self.find_xdk_installation()
			self.load_config_data()
			self.authorize()
		except XDKException as e:
			sublime.error_message(e.value);
			
		except Exception as e:
			if isinstance(e, (urllib.error.HTTPError, urllib.error.URLError, ConnectionRefusedError)):
				sublime.error_message(MSGS['XDK_CONNECTION_FAILED'])
		return True

	def prepare_request_data(self):
		folder = self.view.window().folders()[0]
		regex = re.compile('.*\.xdk(e)?$')
		xdk_files = [ f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f)) and regex.match(f) ]
		xdk_file = None
		if len(xdk_files) > 1:
			dot_xdk_files = [ f for f in xdk_files if f[-4:] == '.xdk']
			if len(dot_xdk_files):
				xdk_file = dot_xdk_files[0]

		return {
			'folder': 				folder,
			'xdk_file':				xdk_file,
			'filename': 			self.view.file_name()
		}






