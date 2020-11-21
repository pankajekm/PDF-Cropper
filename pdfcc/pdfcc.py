"""
PdfCC will help you to crop unnecessary boundaries from the pdf files. We are working on the additional functionalities.




"""



import os
import argparse
from PIL import Image
from pdf2image import convert_from_path
from pdf2image.exceptions import (
    PDFInfoNotInstalledError,
    PDFPageCountError,
    PDFSyntaxError,
)


class PdfCC:
    def __init__(self, fileName, outputFileName, left, right, top, bottom):
        self.fileName = fileName
        self.outFileName = outputFileName
        self.left = left
        self.right = right
        self.bottom = bottom
        self.top = top
        self.TEMP = ".temp/"

    def cropFile(self):
        """ Function to crop the pdf"""
        try:
            os.mkdir(".temp/")
        except OSError:
            print("temp already exists")
        self.__pdftoimage()
        imageList = []
        flag = False

        for i in range(0, self.pageCount + 1):
            print("Page:" + str(i) + "::")
            image = self.__loadImage(
                self.TEMP + self.fileName + str(i) + ".png")
            image = self.__cropImage(image)
            if flag:
                imageList.append(image)
            else:
                im = image
                flag = True
            self.__saveImage(image,
                             self.TEMP + self.fileName + "out" + str(i) + ".png")
            print("Done")
        im.save(self.outFileName, save_all=True, append_images=imageList)

    def __cropImage(self, image):

        width, height = image.size
        if width < self.right or height < self.bottom:
            print("Cropping size greater than page size")
            return image
        croppedImage = image.crop(
            (self.left, self.top, self.right, self.bottom))
        return croppedImage

    def __loadImage(self, fileName):
        return Image.open(fileName)

    def __pdftoimage(self):
        images = convert_from_path(self.fileName)

        for i, image in enumerate(images):
            fname = self.fileName + str(i) + ".png"
            image.save(self.TEMP + fname, "PNG")
        self.pageCount = i

    def __saveImage(self, image, fileName):
        image.save(fileName)


def main():
    """
    This is a CLI wrapper.
    """
    parser = argparse.ArgumentParser(
        description="PdfCC -- The ideal pdf size crop & compress.\nRemoves\
             unwanted info and compresses the pdf.")
    parser.add_argument("Path",
                        metavar="input_path",
                        type=str,
                        help="Path to the input pdf file.")
    parser.add_argument(
        "-L",
        nargs="?",
        dest="L",
        const=450,
        default=450,
        type=int,
        help="Specify the left limit",
    )
    parser.add_argument(
        "-R",
        nargs="?",
        dest="R",
        const=2800,
        default=2800,
        type=int,
        help="Specify the right limit",
    )
    parser.add_argument(
        "-T",
        nargs="?",
        dest="T",
        const=0,
        default=0,
        type=int,
        help="Specify the top limit",
    )
    parser.add_argument(
        "-B",
        nargs="?",
        dest="B",
        const=1900,
        default=1900,
        type=int,
        help="Specify the left limit",
    )
    parser.add_argument(
        "-o",
        nargs="?",
        metavar="output_path",
        dest="opath",
        default="o.pdf",
        help="Specify the output path (optional)",
    )
    args = parser.parse_args()

    pdfcropper = PdfCC(args.Path, args.opath, args.L, args.R, args.T, args.B)
    pdfcropper.cropFile()
