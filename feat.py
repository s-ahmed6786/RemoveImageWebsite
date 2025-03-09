from rembg import remove
from PIL import Image

print("Processing Image...")

input = Image.open("image.png")

output = remove(input)

output.save('out_image.png')

print("Done!")
