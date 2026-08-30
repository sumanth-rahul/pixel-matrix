import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np
import numpy.linalg as la
from image_compression import compress_svd

def bw_comp_image(INPUT_IMAGE,k):
    original_image = imread(INPUT_IMAGE)
    
    img_color = original_image.astype(float)
    
    R = img_color[:, :, 0]  
    G = img_color[:, :, 1]  
    B = img_color[:, :, 2]  
    ##converting to balck & white
    bw_image = ((0.299 * R) + (0.587 * G) + (0.114 * B))/255.0 
    
    svdbw, U_bw, sigma_bw, V_bw, keep_bw = compress_svd(bw_image, k)
    
    original_bytes = original_image.nbytes
    original_kb = original_bytes / 1024
        
    comp_bytes = (
                U_bw.nbytes + sigma_bw.nbytes + V_bw.nbytes 
   )
    comp_kb = comp_bytes / 1024
        
    # 3. Calculate theoretical savings
    comp_per = (1 - (comp_kb / original_kb)) * 100
        
    print("ANALYSIS OF THE ORGINAL AND COMPRESSED IMAGES(B&W):")
    print(f"Original Array Size:  {original_kb:.2f} KB")
    print(f"SVD Components Size:  {comp_kb:.2f} KB")
    print(f"Decreased Space:  {comp_per:.2f}%")	
    
    if(comp_kb > original_kb):
        print("compressed image size is greater than the orginal image size, so try another value of percentage less than the current value to get the compressed image")

    fig, axes = plt.subplots(1, 3, figsize=(20, 5))
    
    axes[0].imshow(original_image)
    axes[0].set_title("original image")
    axes[0].axis('off')
    
    axes[1].imshow(bw_image, cmap='gray')
    axes[1].set_title("black and white image")
    axes[1].axis('off')
    
    
    axes[2].imshow(svdbw,cmap='gray')
    axes[2].set_title("compressed image")
    axes[2].axis('off')
    
    plt.tight_layout()
    plt.show()