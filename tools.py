import cv2
import pytesseract
import easyocr
from PIL import Image, ImageGrab
import matplotlib.pyplot as plt


COLOR_DICT = ["โอรส", "เบจ", "ดำ", "ฟ้า", "ครีม", "ครีมสลับขาว", "ทอง", "เขียว", "เทา", "กากี", "กะปิ", "ขี้ม้า", "กลม", "นาค", "นูด", "นู๊ต", "ส้ม", "ชมพู", "ม่วง", "แดง", "เงิน", "แทน", "ตาล", "ขาว", "ขาวสลับดำ", "เหลืิิอง"]

def read_image_text(image_path):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #display_image_from_array(gray_image)
    threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold_image, lang='tha', config='--psm 6')
    return text

def display_image_from_array(image_array):
    displayed_image = Image.fromarray(image_array)
    displayed_image.show()

def easy_ocr(image_path, output_path="", render=False, output=False):
    reader = easyocr.Reader(['th'])
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)
    transformed_image = cv2.equalizeHist(image)
    results = reader.readtext(transformed_image)
    for index, result in enumerate(results):
        # print(result[1])
        print("Color found:", result[1])
        if(render == True):
            render_bouding_box(result[0], image_path, output_path, index)
    if (output == True):
        return results
    
def easy_ocr_text(image_path):
    reader = easyocr.Reader(['th'])
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, image = cv2.threshold(gray_image, 150, 255, cv2.THRESH_BINARY_INV)
    image = cv2.fastNlMeansDenoising(image, None, 30, 7, 21)
    transformed_image = cv2.equalizeHist(image)
    results = reader.readtext(transformed_image)
    coordinate = []
    for index, result in enumerate(results):
        coordinate.append(result[0])
    return coordinate

def tesseract(image_path, output_path="", render=False, output=False):
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    threshold_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(threshold_image, lang='tha')
    if (render == True):
        render_bouding_box(text, image_path, output_path)
    if (output == True):
        return text

def render_bouding_box(coordinates, input_path, output_path, index):
    image = cv2.imread(input_path)
    if (index > 0):
        image = cv2.imread(output_path)
    for i in range (len(coordinates)):
        start_point = (int(coordinates[i][0]), int(coordinates[i][1]))
        print(start_point)
        end_point = (int(coordinates[(i + 1) % len(coordinates)][0]), int(coordinates[(i + 1) % len(coordinates)][1]))
        color = (0, 0, 0)
        thickness = 2
        cv2.line(image, start_point, end_point, color, thickness)
    cv2.imwrite(output_path, image)

def estimate_text_location_and_size(top_left, top_right, bottom_left, bottom_right):
    horizontal_location = (top_right[0] - bottom_left[0]) /2 + bottom_left[0]
    vertical_location = (bottom_right[1] - top_left[1]) / 2 + top_left[1]
    width = top_right[0] - top_left[0]
    height = bottom_right[1] - top_right[1]
    return (horizontal_location, vertical_location, width, height)


def screenshot_specific_area(coordinate, image_path, output_path):
    image = Image.open(image_path)
    print(coordinate)
    left, right, bottom, top = coordinate[0][0], coordinate[2][0], coordinate[2][1], coordinate[0][1]
    if (bottom < top):
        return
    if (right < left):
        return
    crop_image = image.crop((left, top, right, bottom))
    crop_image.save(output_path)


