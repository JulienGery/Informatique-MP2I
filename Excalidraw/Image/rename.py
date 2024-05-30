from os import listdir, rename
from os.path import isfile, join

images = [f for f in listdir('.') if isfile(join('.', f))]

print(images)

for image in images:
    rename(image, image.replace(' ', '_'))
