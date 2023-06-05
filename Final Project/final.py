import zipfile


from PIL import Image
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

def searchPicture(picture, critera):
    '''Takes an image and a search term as arguements. It will then convert the picture to the most advantageous form to you 
    Pytesseract to extract all text from the picture. Then it will look to see if the search terms is on that page. If so it will
    return true if not False

    ::param picture is a PIL object picture
    ::param search term is a word to search for in the picture
    '''

    text = pytesseract.image_to_string(picture)
    for word in text.split():
        if word.upper() == critera.upper():
            return True
    return False
    
def getFaces(imgSearch):
    '''Takes a list of all pictures that contain the search criteria and will extract all faces from them
    
    ::param hits is a list of pictures that contain search crtieria'''

    face_cascade = cv.CascadeClassifier("Final Project\haarcascade_frontalface_default.xml")
    for pic in imgSearch:
        x = cv.cvtColor(np.array(pictures[pic]), cv.COLOR_RGB2BGR)
        gray = cv.cvtColor(x, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray)
        faces




if __name__ == '__main__':
    createDictionary(location)
    search = "application" 
    hits = []
    for img in pictures.keys():
        if searchPicture(pictures[img], search):
            hits.append(img)
    getFaces(hits)