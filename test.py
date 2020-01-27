from PIL import Image

im = Image.open('imagenew1.png')
width, height = im.size

print(width)
print(height)