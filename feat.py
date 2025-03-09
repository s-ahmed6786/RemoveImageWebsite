from rembg import remove
from PIL import Image

print("Hello World")

input = Image.open("image.jpg")

output = remove(input)

output.save('out.png')
