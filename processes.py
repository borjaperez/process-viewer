import pygtk
pygtk.require('2.0')
import gtk
import os

class Processes:
	"""Processes class"""

	

	def execute(self):
		output = ""
		outputfd = os.popen(self.comando, 'r')
		for line in outputfd.readlines():
			output += line;
		return output
		
		

	def todo_proc(self):
		self.comando = "ps a"
		return self.comando
	def usu_proc(self):
		self.comando = "ps"
	def todo_proc_tty(self):
		self.comando = "ps ax"
	def usu_proc_tty(self):
		self.comando = "ps x"




if __name__ == "__main__":
	p = Processes ()
	p.usu_proc_tty()
	print p.__init__()

