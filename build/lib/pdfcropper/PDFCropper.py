import os
import argparse
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
        self.TEMP = '.temp/'

    def cropFile(self):
        try:
            os.mkdir('.temp/')
        except:
            print("temp already exists")
        self.pdftoimage()
        imageList=[]
        flag=False
        
        for i in range(0,self.pageCount+1):
            print("Page:"+str(i)+"::")
            image=self.loadImage(self.TEMP+self.fileName+str(i)+".png")
            image=self.cropImage(image)
            if flag:
                imageList.append(image)
            else:
                im=image
                flag=True
            self.saveImage(image,self.TEMP+self.fileName+"out"+str(i)+".png")
            print("Done")
        im.save(self.outFileName,save_all=True, append_images=imageList)
        

    def cropImage(self,image):
        
        width, height = image.size 
        #add condition to skip croping if 
        if width < self.right or height < bottom:
            print("Cropping size greater than page size")
            return image
        croppedImage= image.crop((self.left, self.top, self.right,self.bottom))
        return croppedImage 

    def loadImage(self,fileName):
        return Image.open(fileName) 
    
    def pdftoimage(self):
        images = convert_from_path(self.fileName)
        
        for i, image in enumerate(images):
             fname = self.fileName + str(i) + ".png"
             image.save(self.TEMP+fname, "PNG")
        self.pageCount=i
        
    def saveImage(self,image,fileName):
        image.save(fileName)
    

def main():
    parser = argparse.ArgumentParser(description="PdfCropper -- The ideal pdf size cropper\nRemoves unwanted info and compresses the pdf.")
    parser.add_argument("Path", 
                        metavar='input_path', 
                            type=str,
                            help="Path to the input pdf file.")
    parser.add_argument('-L', nargs="?", dest='L', const=450, default=450, type=int, help='Specify the left limit')
    parser.add_argument('-R', nargs="?", dest='R', const=2800, default=2800, type=int, help='Specify the right limit')
    parser.add_argument('-T', nargs="?", dest='T', const=0, default=0, type=int, help='Specify the top limit')
    parser.add_argument('-B', nargs="?", dest='B', const=1900, default=1900, type=int, help='Specify the left limit')
    parser.add_argument('-o', nargs="?", metavar='output_path', dest='opath', default='o.pdf', help='Specify the output path (optional)')
    args=parser.parse_args()

    pdfcropper=PDFCropper(args.Path,args.opath,args.L,args.R,args.T,args.B)
    pdfcropper.cropFile()