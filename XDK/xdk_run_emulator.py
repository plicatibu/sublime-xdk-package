import sublime, sublime_plugin
import XDK.core

#class ExampleCommand(sublime_plugin.TextCommand):
#	def run(self, edit):
#		self.view.insert(edit, 0, "Hello, World!")

class XdkRunEmulatorCommand(sublime_plugin.TextCommand, XDK.core.XDKPluginCore):
	def run(self, edit):
		self.prepare()



		
