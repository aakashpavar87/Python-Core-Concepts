import matplotlib

matplotlib.use("TkAgg")


import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("/home/aakash/Desktop/Python Core Concepts/Hanumanji.jpeg")
plt.imshow(im)
plt.axis("off")
plt.show()
