
import PIL
from PIL import Image
from PIL import ImageEnhance
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageStat

# read image and convert to RGB
image=Image.open("Pillow in Jupyter\msi_recruitment.gif")
image=image.convert('RGB')

width, height = image.size
changes = [.1,.5,.9]
images=[]
channels = [0,1,2]
fnt= ImageFont.truetype("Pillow in Jupyter/fanwood-webfont.ttf", size= 75)
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

        
    
def addBorder(img,ro,c,color):
    info = Image.new('RGB',(first_image.width,(first_image.height+80)))
    info.paste(img,(0,0))
    b = ImageDraw.Draw(info)
    b.rectangle([(0,first_image.height),(first_image.width,first_image.height+80)], fill=(0,0,0))
    d = ImageDraw.Draw(info)
    r,g,b = color._getmean()
    phrase = "Channel {b}   Intensity {a}".format(b=channels[ro], a = changes[c])
    d.text((5,first_image.height+10), phrase, font = fnt, fill=(int(r),int(g),int(b)))
    return info
            
# create a contact sheet from different brightnesses
first_image=images[0]
contact_sheet=PIL.Image.new(first_image.mode, (first_image.width*3,(first_image.height*3)+240))
x=0
y=0
row = 0
col = 0
for img in images:
    # Lets paste the current image into the contact sheet
    # get a drawing context
    color = ImageStat.Stat(img)
    withBorder = addBorder(img,row,col,color)
    contact_sheet.paste(withBorder, (int(x), int(y)) )
    # Now we update our X position. If it is going to be the width of the image, then we set it to 0
    # and update Y as well to point to the next "line" of the contact sheet.
    if x+first_image.width == contact_sheet.width:
        x=0  
        y=y+(first_image.height+80)
        row += 1
        col = 0
    else:
        x=x+first_image.width
        col += 1

# resize and display the contact sheet
contact_sheet = contact_sheet.resize((int(contact_sheet.width/2),int(contact_sheet.height/2) ))
contact_sheet.show()