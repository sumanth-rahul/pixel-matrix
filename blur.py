import cv2
import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np


def blur_image(INPUT_IMAGE):
    input_image=cv2.imread(INPUT_IMAGE)
    blur_kernel = np.array([
        [1/9,1/9,1/9],
        [1/9,1/9,1/9],
        [1/9,1/9,1/9]
    ], dtype=np.float32)


    blured_image = cv2.filter2D(input_image, -1, blur_kernel)

    image_before = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    image_after = cv2.cvtColor(blured_image, cv2.COLOR_BGR2RGB)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    axes[0].imshow(image_before)
    axes[0].set_title('Before (Original Image)')
    axes[0].axis('off') 

    # Plot the filtered sharp image on the right axis
    axes[1].imshow(image_after)
    axes[1].set_title('After (Kernel Applied) : gaussian blur kernel')
    axes[1].axis('off')  

    plt.tight_layout()
    plt.show()