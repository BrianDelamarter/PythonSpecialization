
import PIL
from PIL import Image
from PIL import ImageEnhance


# read image and convert to RGB
image=Image.open("readonly/msi_recruitment.gif")
image=image.convert('RGB')

# build a list of 9 images which have different brightnesses
width, height = image.size
changes = [.1,.5,.9]
images=[]
for x in range(1, 4):
    if x == 1:
        for change in changes:
            pixel_map = image.copy()
            for i in range(width):
                for j in range(height):
                    r, g, b = image.getpixel((i, j))
                    adjust = (int(change*r),int(g),int(b))
                    pixel_map.putpixel((i,j),adjust)
            images.append(pixel_map)
    elif x == 2:
        for change in changes:
            pixel_map = image.copy()
            for i in range(width):
                for j in range(height):
                    r, g, b = image.getpixel((i, j))
                    adjust = (int(r),int(change*g),int(b))
                    pixel_map.putpixel((i,j),adjust)
            images.append(pixel_map)
    elif x == 3:
        for change in changes:
            pixel_map = image.copy()
            for i in range(width):
                for j in range(height):
                    r, g, b = image.getpixel((i, j))
                    adjust = (int(r),int(g),int(change*b))
                    pixel_map.putpixel((i,j),adjust)
            images.append(pixel_map)

# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,first_image.height*3))
x=0
y=0
for img in images:
    # Lets paste the current image into the contact sheet
    contact_sheet.paste(img, (x, y) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0
        y=y+first_image.height
    else:
        x=x+first_image.width

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
display(contact_sheet)