import numpy as np
from PIL import Image 
import matplotlib.pyplot as plt
from numba import stencil

@stencil
def blur_kernel(A):
    return 0.25 * (A[-1,0] + A[1,0] +  A[0,-1] + A[0,1])


# CHANGE the image file on this line for a different image
img = Image.open('penguin.jpg').convert('L')

# We'll work with a resized version of this image
#We make this fairly small so the single point blur works
dim = 200
img_resized = img.resize((dim,dim))

# ... and convert it into a numpy array of floats
img_data = np.asarray(img_resized,dtype=float)

img_blurred = blur_kernel(img_data)

# Display the result of blurring the picture
plt.figure(figsize = [6, 6])
plt.imshow(img_blurred,cmap='gray');

plt.show()
# In a real program we'd probably want to save this image somehow, or do some more processing here.
