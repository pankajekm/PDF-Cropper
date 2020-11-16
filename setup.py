import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pdfcropper",
    version="0.0.1",
    author="S Krishna Bhat",
    author_email="memotoskbhat@gmail.com",
    description="PDF cropper: removes unwanted noise from pdf and compresses them",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/pankaj.ekm/PDF-Cropper.git",
    install_requires=[
          'pdf2image',
          'pillow',
      ],
    packages=setuptools.find_packages(),
    entry_points = {
        'console_scripts': ['pdfcropper = pdfcropper.PDFCropper:main']
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
