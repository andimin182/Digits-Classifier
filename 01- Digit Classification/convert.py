import numpy as np
from PIL import Image
import PIL

image = Image.open('Data/image.png')

print(image.format)
print(image.size)
print(image.mode)

# Convert in np
image_np = np.asarray(image)
print(image_np.shape)
