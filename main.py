from rembg import remove
from PIL import Image

print("Hello World")

img = Image.open("image.jpg")

remove(img)
