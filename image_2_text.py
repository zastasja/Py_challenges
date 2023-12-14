import os.path

from PIL import Image
from pytesseract import pytesseract


def image_2_text():
    file_name = "file name with extension"
    folder_location = r"path to folder"
    screenshots_folder = "folder with picture if it's in cyrillic - Скриншоты\\"
    path_to_tesseract = r"paths to tesseract.exe"
    image_path = os.path.join(folder_location, screenshots_folder, file_name)

    # Opening the image & storing it in an image object
    img = Image.open(image_path)
    pytesseract.tesseract_cmd = path_to_tesseract
  
    # This function will extract the text from the image
    text = pytesseract.image_to_string(img)

    # Displaying the extracted text
    print(text[:-1])
