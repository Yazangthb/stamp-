import os
os.environ['TESSDATA_PREFIX'] = r'C:\Program Files\Tesseract-OCR\tessdata'

import cv2
import pytesseract

def remove_text(image_path):
    # Set the path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Load the image
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Get the script and orientation of the text
    osd = pytesseract.image_to_osd(gray)

    # Parse the script and orientation information
    script = None
    orientation = None
    for line in osd.split('\n'):
        if line.startswith('Script:'):
            script = line.split(':')[1].strip()
        elif line.startswith('Orientation in degrees:'):
            orientation = int(line.split(':')[1].strip())

    # Apply OCR to recognize text regions
    text = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT, config='--psm 6')

    # Iterate over each detected text region
    for i in range(len(text['text'])):
        # Get the bounding box coordinates of the text region
        x = text['left'][i]
        y = text['top'][i]
        w = text['width'][i]
        h = text['height'][i]

        # Fill the text region with white color
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), -1)

    # Save the modified image with a specific path
    output_path = "C:\\Users\\yazan\\OneDrive\\Desktop\\output\\image_without_text.jpg"
    cv2.imwrite(output_path, image)

    print("Text removed successfully!")

# Call the function by providing the path to your image
remove_text(r"C:\Users\yazan\OneDrive\Desktop\im.png")
