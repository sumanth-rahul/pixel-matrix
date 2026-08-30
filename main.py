import numpy as np

from image_compression import compression_image,compress_svd
from bw_comp import bw_comp_image
from blur import blur_image
from edge import edge_image
from sharpen import sharpen_image

INPUT_IMAGE="sample_images/sample2.jpg"

print("IMAGE OPERATIONS")
print("1. Image Compression")
print("2. change color photo to black & white and compress")
print("3. Sharpen the image")
print("4. edge detection of the image")
print("5. blur the image")

n=(int)(input("which operation would you like to perfom: "))

if(n==1):
	print("NOTE:while entering the percentage value, if the value is greater than ~13(in that range) the compressed image size will be greater than the orginal image size because original image store as uint8 and compressed image store as float32.so enter the value of percentage between (1-13) to get the compressed image size less than the orginal image size ")
	k= (int)(input("enter the value of the percentage you want to keep: "))
	k=np.clip(k,1,100)
	compression_image(INPUT_IMAGE,k)

elif(n==2):
	print("NOTE:while entering the percentage value, if the value is greater than ~15(in that range) the compressed image size will be greater than the orginal image size because original image store as uint8 and compressed image store as float32, so the size of compressed image will be greater than orginal image,so please enter the value of percentage between (1-15) to get the compressed image size less than the orginal image size ")
	kb= (int)(input("enter the value of the percentage you want to keep (1-15): "))
	kb=np.clip(kb,1,100)
	bw_comp_image(INPUT_IMAGE,kb)

elif(n==3):
	sharpen_image(INPUT_IMAGE)

elif(n==4):
	edge_image(INPUT_IMAGE)

elif(n==5):
	blur_image(INPUT_IMAGE)

else:
	print("Choose from the above operation")

