import os
import glob
from PIL import Image
import requests
import mimetypes


def getImages(imageArray):
    cwd = os.getcwd()
    fd = os.path.join(cwd, r'imageTemp')
    if not os.path.exists(fd):
        os.mkdir(fd)
    
    files = glob.glob('imageTemp/*')
    if files:
        # deletion
        for f in files:
            os.remove(f)
    
    ext = []
    # download
    for index in range(len(imageArray)):
        response = requests.get(imageArray[index], stream=True)
        # getting extension of image
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        img = Image.open(response.raw)
        img.save('imageTemp/'+str(index)+extension)
        ext.append(extension)
        
    return ext