import sublime, sublime_plugin
import os
import json
import urllib
#from urllib.parse import urlparse

### CONFIGURATION
CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'xdk_plugin.conf');
MSGS = {
	'CONFIG_FILE_IS_EMPTY': 'Configuration file is empty or not created. Please enter correct XDK folder in the prompt below.',
	'CONFIG_STRING_IS_NOT_DIR': 'Path specified in configuration is not accessable. Please enter correct XDK folder in the prompt below.',
	'SPECIFIED_DIRECTORY_IS_NOT_XDK': 'Path specified in configuration is not XDK one. Please enter correct XDK folder in the prompt below.',
	'CAN_NOT_PARSE_SERVER_DATA': 'Can not parse XDK server data file.',
	'CAN_NOT_VALIDATE_SECRET_KEY': 'Can not authorize to XDK.',
	'XDK_CONNECTION_FAILED': 'Connection to XDK failed. Do you have XDK running?',

	'CAN_NOT_GET_FOLDER': 'Can not get current folder. Do you have project folder opened?'
}
### E.O. CONFIGURATION

class XDKException(Exception):
	need_configuration = False
	def __init__(self, value, need_configuration=False):
		self.value = value
		self.need_configuration = need_configuration
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
		print('make_request: addr=', addr);
		#parsed = urlparse(addr)
		#parsed = urllib.parse.urlparse(addr)
		params = urllib.parse.urlencode(params).encode('utf-8')
		#request = urllib.request.Request(addr, headers=headers, data=params)
		try:
			request = urllib.request.Request(addr, params, headers)
			response = urllib.request.urlopen(request)
		except: 
			raise XDKException(MSGS['XDK_CONNECTION_FAILED']); 
		return response

	#def make_simple_request(self, addr, params={}, headers={}):
	#	response = self.make_request(addr, params, headers);
	#	return response.status == 200;

	def invoke_command(self, cmd):
		def _make_request():
			return self.make_request(self.plugin_base_path, cmd, {
				'Cookie' : self.auth_cookie
			})

		response = _make_request();
		# if authentication failed - try authenticate again
		if response.status == 401:
			self.reset_authorization()
			self.prepare()
			response = _make_request()
			return response.code == 200
		else:
			return response.code == 200



	def load_config_data(self):
		if self.plugin_base_path is not None:
			print('load_config_data: already has plugn_base_path')
			return

		print('load_config_data: trying to read CONFIG_FILE=', CONFIG_FILE);
		with open(CONFIG_FILE, 'r') as f:
			self.config_contents = f.read();
		print('load_config_data: CONFIG_FILE read')
		if not self.config_contents:
			raise XDKException(MSGS['CONFIG_FILE_IS_EMPTY'], True);
		self.xdk_dir = self.config_contents.strip()
		print('load_config_data: xdk_dir=' + self.xdk_dir)
		if not os.path.exists(self.xdk_dir) or not os.path.exists(self.xdk_dir):
			raise XDKException(MSGS['CONFIG_STRING_IS_NOT_DIR'], True);
		self.server_data_path = os.path.join(self.xdk_dir, 'server-data.txt')
		print('load_config_data: server_data_path=', self.server_data_path)
		if not os.path.isfile(self.server_data_path):
			raise XDKException(MSGS['SPECIFIED_DIRECTORY_IS_NOT_XDK'], True)
		server_data_contents = None;
		with open(self.server_data_path, 'r') as f:
			server_data_contents = f.read()
		print('load_config_data: server_data_contents=' + server_data_contents);	
		try:
			decoded = json.loads(server_data_contents.replace('[END]', ''))
			self.auth_secret = decoded['secret']
			# TODO: Replace this!
			self.base_path = 'http://localhost:' + str(decoded['port']);
			self.plugin_base_path = 'http://localhost:' + str(decoded['port']) + '/http-services/plugin-listener/plugin/entrance'
			print('load_config_data: auth_secret=' + self.auth_secret);
			print('load_config_data: base_path=' + self.base_path);
			print('load_config_data: plugin_base_path=' + self.plugin_base_path);
		except:
			raise XDKException(MSGS['CAN_NOT_PARSE_SERVER_DATA'], True);

	def authorize(self):
		if self.auth_cookie is not None:
			print('authorize: auth_cookie is not none');
			return 

		print('authorize: making request to /validate');	
		response = self.make_request(self.base_path + '/validate', {}, {'x-xdk-local-session-secret': self.auth_secret });
		cookies = dict(response.info().items())
		print('authorize: response.status=' + str(response.status));
		print('authorize: cookies length=', len(cookies));
		if response.status != 200 or 'Set-Cookie' not in cookies: 
			raise XDKException(MSGS['CAN_NOT_VALIDATE_SECRET_KEY']);
		self.auth_cookie = cookies['Set-Cookie']
		print('authorize: auth_cookie=', self.auth_cookie);

	def reset_authorization(self):
		self.auth_secret = None
		self.auto_cookie = None

	def _on_configuration_changed(self, val):
		pass

	def _on_configuration_canceled(self, val):
		pass

	def _on_configuration_done(self, value):
		with open(CONFIG_FILE, 'w') as f:
			f.write(value);
		self.prepare();


	def show_configuration_prompt(self): 
		window = self.view.window();
		window.show_input_panel('Enter XDK folder:', '', self._on_configuration_done, self._on_configuration_changed, self._on_configuration_canceled)
		

	def prepare(self):
		try:
			self.load_config_data()
			self.authorize()
		except XDKException as e:
			sublime.error_message(e.value);
			if e.need_configuration:
				self.show_configuration_prompt()
			return False
		return True




