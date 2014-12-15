import sublime, sublime_plugin
import XDK.core
from XDK.core import MSGS

class XdkRunEmulatorCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		data = self.prepare_request_data()
		data.update({
			'action': 'run_emulate'
		})
		self.invoke_command(data);

#########################################################

class XdkRunTestPushFilesCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		data = self.prepare_request_data()
		data.update({
			'action': 'run_test',
			'method': 'push_files'
		})
		self.invoke_command(data);

class XdkRunTestBeginDebuggingCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		data = self.prepare_request_data()
		data.update({
			'action': 'run_test',
			'method': 'begin_debugging'
		})
		self.invoke_command(data)

#########################################################

class XdkRunDebugLaunchAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		
		data = self.prepare_request_data()
		data.update({
			'action': 'run_debug',
			'method': 'launch_app'
		})
		self.invoke_command(data)

class XdkRunDebugDebugAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		
		data = self.prepare_request_data()
		data.update({
			'action': 'run_debug',
			'method': 'debug_app'
		})
		self.invoke_command(data)

class XdkRunDebugStopAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		
		data = self.prepare_request_data()
		data.update({
			'action': 'run_debug',
			'method': 'stop_app'
		})
		self.invoke_command(data)

#########################################################

class XdkRunProfileStartCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return
		
		data = self.prepare_request_data()
		data.update({
			'action': 'run_profile',
			'method': 'start'
		})
		self.invoke_command(data)

class XdkRunProfileStopCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		data = self.prepare_request_data()
		data.update({
			'action': 'run_profile',
			'method': 'stop'
		})
		self.invoke_command(data)

class XdkRunProfileCloseAppCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare(): return

		data = self.prepare_request_data()
		data.update({
			'action': 'run_profile',
			'method': 'close_app'
		})
		self.invoke_command(data)

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


		
