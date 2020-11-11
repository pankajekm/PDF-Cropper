import os
from PIL import Image
from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)
class PDFCropper():
    def __init__(self,fileName,outputFileName,left,right,top,bottom):
        self.fileName=fileName
        self.outFileName=outputFileName
        self.left=left
        self.right=right
        self.bottom=bottom
        self.top=top


    def cropFile(self):
        self.pdftoimage()
        imageList=[]
        flag=False
        
        for i in range(0,self.pageCount+1):
            image=self.loadImage(self.fileName+str(i)+".png")
            image=self.cropImage(image)
            if flag:
                imageList.append(image)
            else:
                im=image
                flag=True
            self.saveImage(image,self.fileName+"out"+str(i)+".png")
        im.save(self.outFileName,save_all=True, append_images=imageList)
        
        
    def cropImage(self,image):
        
        width, height = image.size 
        

        #add condition to skip croping if 
        croppedImage= image.crop((self.left, self.top, self.right,self.bottom))
        return croppedImage 
    def loadImage(self,fileName):
        return Image.open(fileName) 
    
    def pdftoimage(self):
        images = convert_from_path(self.fileName)
        
        for i, image in enumerate(images):
             fname = self.fileName + str(i) + ".png"
             image.saveImage(fname, "PNG")
        self.pageCount=i
        

    def saveImage(self,image,fileName):
        image.save(fileName)
    

if __name__ == "__main__":
    pdfcropper=PDFCropper("1.pdf","out.pdf",450,2800,0,1900)
    pdfcropper.cropFile()