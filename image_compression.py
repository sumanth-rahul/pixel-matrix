import cv2
import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import numpy.linalg as la

def compress_svd(color,k):
	color=color.astype(float)
	U,sigma,V=la.svd(color, full_matrices=False)
	sigma[sigma <= 1e-5] = 0.0
	significant = sigma[sigma > 0]
	count= len(significant)
	sigma_new = np.zeros_like(sigma)
	keep = max(1, int(count * (k / 100)))
	U_comp = U[:, :keep]
	sigma_comp = sigma[:keep]
	V_comp = V[:keep, :]
	svd= U_comp @ np.diag(sigma_comp) @ V_comp
	return svd, U_comp.astype(np.float32), sigma_comp.astype(np.float32), V_comp.astype(np.float32), keep

def compression_image(INPUT_IMAGE,k):
    original_image=imread(INPUT_IMAGE)
    ##red-----------------------------------------
    svdred, U_red, sigma_red, V_red, keep_red = compress_svd(original_image[:, :, 0], k)

    ##green---------------------------------------
    svdgreen, U_green, sigma_green, V_green, keep_green = compress_svd(original_image[:, :, 1], k)
    
    ##blue----------------------------------------
    svdblue, U_blue, sigma_blue, V_blue, keep_blue = compress_svd(original_image[:, :, 2], k)
    
    ##stacking the RGB compressed part-------------------------
    svdfinal = np.dstack((svdred, svdgreen, svdblue)) 
    svdfinal = np.clip(svdfinal, 0, 255)
    svdfinal = svdfinal.astype(np.uint8)
    ##error image---------------------------------
    error_image = np.abs(original_image.astype(float) - svdfinal.astype(float))
    error_image = np.clip(error_image, 0, 255).astype(np.uint8)

    original_bytes = original_image.nbytes
    original_kb = original_bytes / 1024

    comp_bytes = (
        U_red.nbytes + sigma_red.nbytes + V_red.nbytes +
        U_green.nbytes + sigma_green.nbytes + V_green.nbytes +
        U_blue.nbytes + sigma_blue.nbytes + V_blue.nbytes
    )
    comp_kb = comp_bytes / 1024

    # 3. Calculate theoretical savings
    comp_per = (1 - (comp_kb / original_kb)) * 100

    print("ANALYSIS OF THE ORGINAL AND COMPRESSED IMAGES:")
    print(f"Original Array Size:  {original_kb:.2f} KB")
    print(f"SVD Components Size:  {comp_kb:.2f} KB")
    print(f"decreased space:  {comp_per:.2f}%")	

    if(comp_kb > original_kb):
        print("compressed image size is greater than the orginal image size, so try another value of percentage less than the current value to get the compressed image")

    ##plotting the images---------------------------------
    fig, axes = plt.subplots(1, 3, figsize=(20, 5))

    axes[0].imshow(original_image)
    axes[0].set_title("original image")
    axes[0].axis('off')

    axes[1].imshow(svdfinal)
    axes[1].set_title("compressed image")
    axes[1].axis('off')

    axes[2].imshow(error_image)
    axes[2].set_title("What SVD Actually Deleted")
    axes[2].axis('off')


    plt.tight_layout()
    plt.show()