import argparse
import cv2
import numpy as np
import os
ap = argparse.ArgumentParser()
ap.add_argument('-i', '--input', required=True,
               help = 'path to image')
ap.add_argument('-o', '--output', required=True,
               help = 'enter a number to print')
ap.add_argument('-r', '--rotation', required=True,
               help = 'to rotate image')
ap.add_argument('-z', '--zoom', required=True,
               help = 'to zoom image')
ap.add_argument('-g', '--grayscale', required=True,
               help = 'to convert image color to gray scale')
args = vars(ap.parse_args())

num_dir_image = len(args['input'])
list_of_files =list()
#list of images
file = os.listdir(args['input']) #stores the list of image

def rotate_image(index,img):
	img =cv2.imread(img)
	height, width = img.shape[0:2]
	angle = 30
	scale = 2.5
	M = cv2.getRotationMatrix2D((width/2, height/2), angle, scale)
	rotatedImage = cv2.warpAffine(img,M, (width, height))
	cv2.imwrite(os.path.join(args['output'], file[index]),rotatedImage)
    
def gray_image(index, img):
    image = cv2.imread(img) #loads the image by default as colored 
    #converting image to Gray scale 
    gray_img = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY) # converts the image to gray
    cv2.imwrite(os.path.join(args['output'], file[index]), gray_img)
    

    

for index, img in enumerate(file):
	img = os.path.join(args['input'], img) #the file path of the image
	print(img)
	if args['rotation'] == "True":
		rotate_image(index,img)
	elif args['grayscale'] == "True":
		gray_image(index, img)
    
      
print('done')

   

