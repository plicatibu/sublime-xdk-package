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
			'method': 'begin_debugging',
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
			folder = self.view.window().folders()[0]
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
			folder = self.view.window().folders()[0]
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
			folder = self.view.window().folders()[0]
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
			folder = self.view.window().folders()[0]
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
		self.find_xdk_installation()
		self.prepare()

#########################################################

class XdkShowAboutCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		sublime.message_dialog("""Intel® XDK HTML5 Cross-platform Development Tool enables developers to easily design, test, debug, and build HTML5 web and hybrid apps across multiple app stores and form factor devices.  

The Intel XDK plugin for Sublime Text* allows you to drive your HTML5 app emulation, testing, profiling, and builds from within Sublime Text; you just need to set up your project within the Intel XDK first.  

See XXX for more information about the Intel XDK Sublime Text* plugin.  

Please see http://xdk.intel.com for more information about the Intel XDK and for support.

*Other names and brands may be claimed as the property of others.   
Copyright (c) 2013-2014 Intel Corporation. All Rights Reserved.
""")


		
