import sublime, sublime_plugin
import XDK.core
from XDK.core import MSGS

#class ExampleCommand(sublime_plugin.TextCommand):
#	def run(self, edit):
#		self.view.insert(edit, 0, "Hello, World!")

class XdkRunEmulatorCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		try:
			folder = self.view.window().folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_emulate',
			'folder': folder,
			'filename': filename
		})

#########################################################

class XdkRunTestPushFilesCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		try:
			folder = self.view.window().folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_test',
			'method': 'push_files',
			'folder': folder,
			'filename': filename
		})
		
class XdkRunTestBeginDebuggingCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try:
			folder = self.view.window().folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_test',
			'method': 'push_files',
			'folder': folder,
			'filename': filename
		})

#########################################################

class XdkRunDebugLaunchAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try: 
			folder = self.view.window().folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_debug',
			'method': 'launch_app',
			'folder': folder,
			'filename': filename
		})

class XdkRunDebugDebugAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try:
			folder = self.view.window().folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_debug',
			'method': 'debug_app',
			'folder': folder,
			'filename': filename
		})

class XdkRunDebugStopAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try:
			folder = self.view.window.folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_debug',
			'method': 'stop_app',
			'folder': folder,
			'filename': filename
		})

#########################################################

class XdkRunProfileStartCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try:
			folder = self.view.window.folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_profile',
			'method': 'start',
			'folder': folder,
			'filename': filename
		})

class XdkRunProfileStopCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try:
			folder = self.view.window.folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_profile',
			'method': 'stop',
			'folder': folder,
			'filename': filename
		})

class XdkRunProfileCloseAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		try:
			folder = self.view.window.folders()[0]
		except:
			sublime.error_message(MSGS['CAN_NOT_GET_FOLDER'])
			return

		filename = self.view.file_name()
		self.invoke_command({
			'action': 'run_profile',
			'method': 'close_app',
			'folder': folder,
			'filename': filename
		})

#########################################################


class XdkConfigureCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		# TODO: provide user with instructions?
		self.show_configuration_prompt()




		
