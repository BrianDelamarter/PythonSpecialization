import zipfile


from PIL import Image
from PIL import ImageDraw
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR/tesseract.exe"
import cv2 as cv
import numpy as np
import datetime

# loading the face detection classifier
face_cascade = cv.CascadeClassifier('Final Project\haarcascade_frontalface_default.xml')

pictures = {}
location = "Final Project\small_img.zip"

def createDictionary(fileLocation):
    ''' Function takes a zip file to fill out a global dictionary with the key being file names and the item being a PILL object

    :Param path location of zip file that contains picture
    '''

    with zipfile.ZipFile("Final Project\small_img.zip", mode = 'r') as smallData:
        for info in smallData.infolist():
            pictures[info.filename] = Image.open(smallData.open(info.filename))

def binarize(image_to_transform, threshold = 240):
    # now, lets convert that image to a single greyscale image using convert()
    output_image=image_to_transform.convert("L")
    # the threshold value is usually provided as a number between 0 and 255.
    # the algorithm for the binarization is pretty simple, go through every pixel in the
    # image and, if it's greater than the threshold, turn it all the way up (255), and
    # if it's lower than the threshold, turn it all the way down (0).
    for x in range(output_image.width):
        for y in range(output_image.height):
            # for the given pixel at w,h, lets check its value against the threshold
            if output_image.getpixel((x,y))< threshold: #note that the first parameter is actually a tuple object
                # lets set this to zero
                output_image.putpixel( (x,y), 0 )
            else:
                # otherwise lets set this to 255
                output_image.putpixel( (x,y), 255 )
    #now we just return the new image
    return output_image

def searchPicture(picture, critera):
    '''Takes an image and a search term as arguements. It will then convert the picture to the most advantageous form to you 
    Pytesseract to extract all text from the picture. Then it will look to see if the search terms is on that page. If so it will
    return true if not False

    ::param picture is a PIL object picture
    ::param search term is a word to search for in the picture
    '''
    binarized = binarize(picture)
    text = pytesseract.image_to_string(binarized)
    for word in text.split():
        if word.upper() == critera.upper():
            return True
    return False
    
def getFaces(imgSearch):
    '''Takes a list of all pictures keys (file names) that contain the search criteria and will extract all faces from them
    
    ::param hits is a list of pictures that contain search crtieria'''

    face_cascade = cv.CascadeClassifier("Final Project\haarcascade_frontalface_default.xml")
    for pic in imgSearch:
        grey = pictures[pic].convert('L')
        x = np.array(grey)
        faces = face_cascade.detectMultiScale(x)
        drawing=ImageDraw.Draw(pictures[pic])
        for a in faces:
            aList = a.tolist()
            x,y,w,h = aList      
            drawing.rectangle((x,y,x+w,y+h), outline="white")
        pictures[pic].show()
            
                




if __name__ == '__main__':
    createDictionary(location)
    search = "application" 
    hits = []
    '''for img in pictures.keys():
        if searchPicture(pictures[img], search):
            hits.append(img)'''
    pic = ['a-0.png']
    getFaces(pic)