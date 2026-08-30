import cv2
import matplotlib.pyplot as plt
from matplotlib.image import imread
import numpy as np


def edge_image(INPUT_IMAGE):
    input_image=cv2.imread(INPUT_IMAGE)
    edge_kernel = np.array([
        [ -1, -1,  -1],
        [-1,  8, -1],
        [ -1, -1,  -1]
    ], dtype=np.float32)

    edge_image = cv2.filter2D(input_image, -1, edge_kernel)

    image_before = cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB)
    image_after = cv2.cvtColor(edge_image, cv2.COLOR_BGR2RGB)

    fig, axes = plt.subplots(1, 2, figsize=(15, 5))

    axes[0].imshow(image_before)
    axes[0].set_title('Before (Original Image)')
    axes[0].axis('off') 

    axes[1].imshow(image_after)
    axes[1].set_title('After (Kernel Applied) : edge detection kernel')
    axes[1].axis('off')  

    plt.tight_layout()
    plt.show()