####### REQUIRED IMPORTS FROM THE PREVIOUS ASSIGNMENT #######
import tkinter
from newmypackage.model import InstanceSegmentationModel
from newmypackage.data.dataset import Dataset
from newmypackage.analysis.visualize import plot_visualization


####### ADD THE ADDITIONAL IMPORTS FOR THIS ASSIGNMENT HERE #######
from tkinter import *
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog as fd
from functools import partial
import numpy
import os
import os.path


# Define the function you want to call when the filebrowser button is clicked.
#def fileClick(clicked, dataset, segmentor):
def fileClick(clicked, segmentor, dataset):
	####### CODE REQUIRED (START) #######
	# This function should pop-up a dialog for the user to select an input image file.
	# Once the image is selected by the user, it should automatically get the corresponding outputs from the segmentor.
	# Hint: Call the segmentor from here, then compute the output images from using the `plot_visualization` function and save it as an image.
	# Once the output is computed it should be shown automatically based on choice the dropdown button is at.
	# To have a better clarity, please check out the sample video.

	filename = fd.askopenfilename(initialdir = './data/imgs/')
	imgnum = int(filename[-5])

	datavals = []
	for i in range(len(dataset)):
			datavals.append(dataset.__getitem__(i))
	
	boxes, masks, classes, scores = segmentor.__call__(numpy.asarray((datavals[imgnum]['image'].transpose((2, 1, 0)) / 255)))

	plot_visualization(dataset[imgnum]['image'], boxes, masks, classes, scores, f'./output/seg.jpg', True)
	plot_visualization(dataset[imgnum]['image'], boxes, masks, classes, scores, f'./output/bb.jpg', False)

	if(clicked.get() == "Segmentation"):
		image = Image.open('./output/seg.jpg')
		imgTk = ImageTk.PhotoImage(image)
		imglabel = Label(root, image = imgTk)
		imglabel.image = imgTk
		imglabel.grid(row=2, column=0, columnspan = 4)
	else:
		image = Image.open('./output/bb.jpg')
		imgTk = ImageTk.PhotoImage(image)
		imglabel = Label(root, image = imgTk)
		imglabel.image = imgTk
		imglabel.grid(row=2, column = 0, columnspan = 4)

	return

	####### CODE REQUIRED (END) #######

# `process` function definition starts from here.
# will process the output when clicked.
def process(clicked):

	####### CODE REQUIRED (START) #######
	# Should show the corresponding segmentation or bounding boxes over the input image wrt the choice provided.
	# Note: this function will just show the output, which should have been already computed in the `fileClick` function above.
	# Note: also you should handle the case if the user clicks on the `Process` button without selecting any image file.
	if(not os.path.exists("./output/seg.jpg")):
		nofile = Label(root, text = 'No file selected. Please select a file first.')
		nofile.grid(row=2)
		return

	if(clicked.get() == "Segmentation"):
		image = Image.open('./output/seg.jpg')
		imgTk = ImageTk.PhotoImage(image)
		imglabel = Label(root, image = imgTk)
		imglabel.image = imgTk
		imglabel.grid(row=2, column=0, columnspan = 4)
	else:
		image = Image.open('./output/bb.jpg')
		imgTk = ImageTk.PhotoImage(image)
		imglabel = Label(root, image = imgTk)
		imglabel.image = imgTk
		imglabel.grid(row=2, column=0, columnspan = 4)

	return

	####### CODE REQUIRED (END) #######


# `main` function definition starts from here.
if __name__ == '__main__':

	if(os.path.exists("./output/seg.jpg")):
		os.remove('./output/seg.jpg')
	if(os.path.exists("./output/seg.jpg")):
		os.remove('./output/bb.jpg')
	
	####### CODE REQUIRED (START) ####### (2 lines)
	# Instantiate the root window.
	# Provide a title to the root window.

	root = Tk()
	root.title('SWE LAB - PYTHON GUI Assignment - 20CS30015')
	
	####### CODE REQUIRED (END) #######

	# Setting up the segmentor model.
	annotation_file = './data/annotations.jsonl'
	transforms = []
	
	# Instantiate the segmentor model.
	segmentor = InstanceSegmentationModel()
	# Instantiate the dataset.
	dataset = Dataset(annotation_file, transforms=transforms)
	
	
	# Declare the options.
	options = ["Segmentation", "Bounding-box"]
	clicked = StringVar()
	clicked.set(options[0])

	e = Entry(root, width=70)
	e.grid(row=0, column=0)

	####### CODE REQUIRED (START) #######
	# Declare the file browsing button
	filebrowser = Button(root, text=". . . . .", command=partial(fileClick, clicked, segmentor, dataset))
	filebrowser.grid(row=0, column=1)
	####### CODE REQUIRED (END) #######

	####### CODE REQUIRED (START) #######
	# Declare the drop-down button

	drop = OptionMenu(root , clicked , *options)
	drop.grid(row=0, column=2)

	####### CODE REQUIRED (END) #######

	# This is a `Process` button, check out the sample video to know about its functionality
	myButton = Button(root, text="Go", command=partial(process, clicked))
	myButton.grid(row=0, column=3)

	
	####### CODE REQUIRED (START) ####### (1 line)
	# Execute with mainloop()

	root.mainloop()

	####### CODE REQUIRED (END) #######