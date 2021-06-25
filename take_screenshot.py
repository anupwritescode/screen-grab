from PIL import ImageGrab
import datetime
from tkinter import messagebox
from tkinter import filedialog
from tkinter import Button
from tkinter import Tk
from tkinter import Label
from tkinter import StringVar

selected_folder = ""


def find_folder() :
	global selected_folder
	
	selected_folder = filedialog.askdirectory()
	current_folder_path.set(selected_folder)
	
def take_screenshot() :
	global selected_folder
	
	if (selected_folder != "") :
		win_.attributes("-alpha", 0) # hide window 
		now_ = datetime.datetime.now()
		im = ImageGrab.grab()
		im.save(selected_folder + "\\" + now_.strftime("%Y-%m-%d_%H-%M-%S")+".jpg", "JPEG")
		del im
		win_.attributes("-alpha", 1)

	else :
		messagebox.showerror("Error", "You need to select a folder first")

if __name__ == "__main__" :
	
	win_ = Tk()
	
	win_.title("Screen Grab")
	win_.resizable(False, False)
	win_.geometry("250x98+1000+500")
	
	select_folder = Button(win_, text = "Select Folder", command = find_folder)
	
	current_folder_path = StringVar()
	current_folder = Label(win_, textvariable = current_folder_path)
	current_folder_path.set("No folder selected")
	
	grab = Button(win_, text = "Take ScreenShot", command = take_screenshot)
	
	exit_ = Button(win_, text = "Quit", command = win_.destroy)
	
	select_folder.pack(side="top")
	current_folder.pack(side="top")
	grab.pack(side="top")
	exit_.pack(side="top")
	
	
	win_.mainloop()
	
	
