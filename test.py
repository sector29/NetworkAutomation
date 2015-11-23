#from tkinter import *
import tkinter
class GUI():
	__frames = []
	__labels = []
	__buttons = []

	def __init__(self, widgets):
		# Create the main window.
		self.main_window = tkinter.Tk()

		for widget in enumerate(widgets):
			if(widget[1][0] == 'Frame'):
				self.__create_frame(widget)
			elif(widget[1][0] == 'Button'):
				self.__create_button(widget[1][1])
			elif(widget[1][0] == 'Label'):
				self.__create_label(widget[1][1])
		print(self.__frames)
		self.__pack_frames()

		# Enter the tkinter main loop.
		tkinter.mainloop()
		#print('done')

	def __create_frame(self, widget):
		print('widget: ', widget)
		self.__frames.append( [ tkinter.Frame( width=widget[1][1]['width'], height=widget[1][1]['height'], bg=widget[1][1]['bg'] ), widget[1][1] ]  )

	def __pack_frames(self):
		print('__pack_frames')
		print('frames: ', self.__frames)
		for frame in enumerate( self.__frames ):
			frame[1][0].pack(side=frame[1][1]['side'])

	def __create_button(self,widget):
		print(widget)
		self.__buttons.append( tkinter.Button(self.__frames[-1][0], text=widget['text'], width=widget['width'], bg=widget['bg'], anchor=widget['anchor']) )
		self.__buttons[-1].pack(side=widget['side'])

	def __create_label(self,widget):
		print(widget)
		self.__labels.append( tkinter.Label(self.__frames[-1][0], text=widget['text'], width=widget['width'], bg=widget['bg'], anchor=widget['anchor']) )
		self.__labels[-1].pack(side=widget['side'])



def main():
	#gui widgets

	widgets = [ ['Frame',  {'width':'0','height':'0','side':'left','bg':''}],
					['Label',  {'width':'30','text':'Hello World ','side':'left','anchor':'e','bg':'yellow'}],
					['Label',  {'width':'30','text':'Hello World','side':'left','anchor':'w','bg':'pink'}],

				['Frame',  {'width':'0','height':'0','side':'right','bg':'black'}],
					['Label',  {'width':'30','text':'Hello World 2 ','side':'left','anchor':'e','bg':'red'}],
					['Label',  {'width':'30','text':'Hello World 2','side':'left','anchor':'w','bg':'orange'}],

				['Frame',  {'width':'0','height':'0','side':'bottom','bg':'black'}],
					['Button',  {'width':'10','text':'Submit','side':'left','anchor':'center','command':'self.ok_button','bg':'red'}],
					['Button',  {'width':'10','text':'Cancel','side':'left','anchor':'center','command':'self.cancel_button','bg':'red'}],
				]

	gui = GUI(widgets)

main()