from PIL import Image
import numpy as np
import argparse
from scipy import misc
import math

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#ap.add_argument("-i", "--image", required = True, help = "image")
ap.add_argument("-t", "--table", required = True,  help="table path")
args = vars(ap.parse_args())

x_1 = []
x_2 = []
y_1 = []
y_2 = []
names = []
with open(args["table"]) as inf:
    for line in inf:
        parts = line.split(',') # split line into parts
        if len(parts) > 1:   # if at least 2 parts/columns
            names.append(parts[0])
	    x_1.append(parts[1])
	    x_2.append(parts[3])
	    y_1.append(parts[2])
	    y_2.append(parts[4])

for i in range(0,len(names)):
	name = names[i]
	name = name.split('.')
	name = name[0].split('/')
	save_name = name[0]+'cropped.jpg'
	name = name[0]+'_'+name[1]
	print name
	points = [x_1[i],x_2[i],y_1[i],y_2[i]]
	original = Image.open('/home/elijah/Desktop/dataset_79/'+names[i])
	cropped_size = [299,299]
	size_original = original.size
	#a,b = original.size
	#w_prime,h_prime = np.divide(size_original,cropped_size)
	w_prime = size_original[0]/(float(cropped_size[0]))
	h_prime = size_original[1]/(float(cropped_size[1]))
	print w_prime,h_prime
	#w = int(x_2[i])-int(x_1[i])
	#h = int(y_2[i])-int(y_1[i])
	#points_2 = [w,h]
	#w_new,h_new = np.divide(size_original,points_2)
	#print w_new,h_new
	#x1_new = int(x_1[i])*(w_prime)
	#x2_new = (int(x_1[i])+w+1)*(w_prime-1)
	#y1_new = int(y_1[i])*h_prime
	#y2_new = (int(y_1[i])+h+1)*(h_prime-1)

	x1 = size_original[0]*(float(x_1[i])/299)
	x2 = size_original[0]*(float(x_2[i])/299)
	y1 = size_original[1]*(float(y_1[i])/299)
	y2 = size_original[1]*(float(y_2[i])/299)
	cropped_image = original.crop((x1,y1,x2,y2))
	print cropped_image.size
	#cropped_image.show()
	misc.imsave(name+'_cropped.jpg', cropped_image)


"""
for name in names:
	print '/home/elijah/Desktop/dataset_79/'+name 
"""
