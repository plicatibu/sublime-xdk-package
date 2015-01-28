import sublime, sublime_plugin
import XDK.core
from XDK.core import MSGS

class XdkCommand_(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		if not self.prepare():
			return
		self.invoke_command(self.prepare_data())

########## EMULATOR 

class XdkRunEmulatorDockedCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_emulate',
			method='run_docked'
		)
		return data

class XdkRunEmulatorUndockedCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_emulate',
			method='run_undocked'
		)
		return data

########## TEST 

class XdkRunTestPushFilesCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_test', 
			method='push_files'
		)
		return data

class XdkRunTestBeginDebuggingCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_test',
			method='begin_debugging'
		)
		return data


########## DEBUG

class XdkRunDebugLaunchAppCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_debug',
			method='launch_app'
		)
		return data

class XdkRunDebugDebugAppCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_debug',
			method='debug_app'
		)
		return data

class XdkRunDebugStopAppCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_debug',
			method='stop_app'
		)
		return data

########## PROFILE

class XdkRunProfileCpuStartCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_profile',
			method='start_cpu_profiling'
		)
		return data

class XdkRunProfileMemoryStartCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_profile',
			method='start_memory_profiling'
		)
		return data

class XdkRunProfileStopCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_profile',
			method='stop'
		)
		return data

class XdkRunProfileCloseAppCommand(XdkCommand_):
	def prepare_data(self):
		data = self.prepare_request_data()
		data.update(
			action='run_profile',
			method='close_app'
		)
		return data

########## ABOUT

class XdkShowAboutCommand(sublime_plugin.ApplicationCommand):
	def run(self):
		sublime.message_dialog("""Intel® XDK HTML5 Cross-platform Development Tool enables developers to easily design, test, debug, and build HTML5 web and hybrid apps across multiple app stores and form factor devices.  

The Intel XDK plugin for Sublime Text* allows you to drive your HTML5 app emulation, testing, profiling, and builds from within Sublime Text; you just need to set up your project within the Intel XDK first.  

See XXX for more information about the Intel XDK Sublime Text* plugin.  

Please see http://xdk.intel.com for more information about the Intel XDK and for support.

*Other names and brands may be claimed as the property of others.   
Copyright (c) 2013-2014 Intel Corporation. All Rights Reserved.
""")


		
