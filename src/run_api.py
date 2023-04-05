import sys
import os
from pdf_splitter import split_pdf
from PyPDF2 import PdfReader
from pdf2image import convert_from_path


def parse_boolean(b):
    return b == "True"


# for simpler filename generation
def simple_counter_generator(prefix="", suffix=""):
    i = 0
    while True:
        i += 1
        yield 'p'





input_pdf = sys.argv[1]
split_pdfs = split_pdf(input_pdf)
offset = 0


for fragment in split_pdfs:
    input_arg = fragment
    reader = PdfReader(open(input_arg, "rb"))
    no_pages = len(reader.pages)
    if not os.path.exists('output/'):
        os.mkdir('output')
    output_arg = 'output/' + fragment.split('/')[-1][:-4].replace(' ', '')
    command = 'python3 run_api_get_hocr.py ' + input_arg + ' ' + output_arg + ' ' + str(offset) + ' ' + str(no_pages)
    os.system(command)
    offset = offset + 1


setname = input_pdf.split('/')[-1][:-4].replace(" ", "")
outputDirectory = "output/" + setname
if not os.path.exists(outputDirectory):
    os.mkdir(outputDirectory)

if not os.path.exists(outputDirectory + "/CorrectorOutput"):
        os.mkdir(outputDirectory + "/CorrectorOutput")
        os.mknod(outputDirectory + "/CorrectorOutput/" + 'README.md', mode=0o666)

# Creating Final set folders and files
if not os.path.exists(outputDirectory + "/Comments"):
    os.mkdir(outputDirectory + "/Comments")
    os.mknod(outputDirectory + "/Comments/" + 'README.md', mode=0o666)
if not os.path.exists(outputDirectory + "/VerifierOutput"):
    os.mkdir(outputDirectory + "/VerifierOutput")
    os.mknod(outputDirectory + "/VerifierOutput/" + 'README.md', mode=0o666)

if not os.path.exists(outputDirectory + "/Inds"):
    os.mkdir(outputDirectory + "/Inds")
    os.mknod(outputDirectory + "/Inds/" + 'README.md', mode=0o666)
if not os.path.exists(outputDirectory + "/Dicts"):
    os.mkdir(outputDirectory + "/Dicts")
    os.mknod(outputDirectory + "/Dicts/" + 'README.md', mode=0o666)
if not os.path.exists(outputDirectory + "/Cropped_Images"):
    os.mkdir(outputDirectory + "/Cropped_Images")
if not os.path.exists(outputDirectory + "/MaskedImages"):
    os.mkdir(outputDirectory + "/MaskedImages")

os.system('cp ./project.xml ' + outputDirectory)
os.system('cp ./dicts/* ' + outputDirectory + "/Dicts/")
individualOutputDir = outputDirectory + "/Inds"


if not os.path.exists(outputDirectory + "/Images"):
    os.mkdir(outputDirectory + "/Images")

imagesFolder = outputDirectory + "/Images"

if not os.path.exists(outputDirectory + "/text_files"):
    os.mkdir(outputDirectory + "/text_files")

imageConvertOption = 'True'

print("converting pdf to images")
jpegopt = {
    "quality": 100,
    "progressive": True,
    "optimize": False
}

output_file = simple_counter_generator("page", ".jpg")
if (parse_boolean(imageConvertOption)):
    convert_from_path(input_pdf, output_folder=imagesFolder, dpi=300, fmt='jpeg', jpegopt=jpegopt,
                        output_file=output_file)

print("images created.")

