import os
import glob
from PIL import Image
import requests
import mimetypes


def getImages(imageArray):
    files = glob.glob('imageTemp/*')
    if files:
        # deletion
        for f in files:
            os.remove(f)
    
    # download
    for index in range(len(imageArray)):
        response = requests.get(imageArray[index], stream=True)
        # getting extension of image
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        img = Image.open(response.raw)
        img.save('imageTemp/'+str(index)+extension)