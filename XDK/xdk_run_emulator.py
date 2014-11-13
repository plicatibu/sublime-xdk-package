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

		filename = self.view.file_name();
		self.invoke_command({
			'action': 'run_emulator',
			'folder': folder,
			'filename': filename
		})

class XdkConfigureCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		self.show_configuration_prompt()




		
