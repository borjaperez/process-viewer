# Ejercicio 1

import gtk
from processes import Processes

class ejercicio(object):


	def __init__(self):
		builder = gtk.Builder()
		builder.add_from_file("practica1.glade")
		self.window = builder.get_object("show")
		self.window.connect("destroy", lambda w: gtk.main_quit())

		self.button = builder.get_object("quit")
		self.button.connect("clicked", lambda w: gtk.main_quit())

		self.button = builder.get_object("processes")
		self.button.connect("clicked", self.get_processes)

		#self.radiobutton = builder.get_object("myprocesses")
		

		#self.checkbutton = builder.get_object("withouttty")
		

		
		self.textview = builder.get_object("viewprocesses")
		self.buffer_texto = self.textview.get_buffer()
		
		

		self.window.show()

	def estados(self, widget):
		estado = widget.get_active()
		return estado

	def get_processes(self, widget, data=None):
		builder = gtk.Builder()
		builder.add_from_file("practica1.glade")

		self.iter = self.buffer_texto.get_start_iter()

		estadocheck = self.checkbutton.get_active()
		print estadocheck
		
		estadoradio = self.radiobutton.get_active()
		
		p = Processes()
		if estadocheck == True:
			if estadoradio == False:
				p.todo_proc_tty()
			else:
				p.usu_proc_tty()
		else:
			if estadoradio == False:
				p.todo_proc()
			else:
				p.usu_proc()

		result = p.execute()
		self.buffer_texto.set_text(result)
					
e = ejercicio()
e.window.show_all()
gtk.main()
