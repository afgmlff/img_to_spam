import numpy as np
import PIL
from PIL import Image

var_img = PIL.Image.open("fon.png")
print(var_img.size)


image_sequence = var_img.getdata()
image_array = np.array(image_sequence)


'''
for i in image_array:
	i[3].pop()
'''
a = image_array[:][:,0:-1]
print(a)



'''
for i in a0:
  if((a0[i] != 255)):
    print(image_array[i])
'''

img = Image.fromarray(a, 'RGB')
img.save('my.png')
#img.show()
