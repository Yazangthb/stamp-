## Libraries

import os

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Parent directory to output the extracted stamps
# there is also in line 28 the path to read the image from
parent_directory = r"C:\Users\yazan\OneDrive\Desktop\dataset 50"

n = int(input("enter the number of images: "))
## Read and display the n images

for n in range(1, n):
    folder_name = 'output{}'.format(n)

    # Create the folder path
    folder_path = os.path.join(parent_directory, folder_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    zeros = 4
    formatted_number = str(n).zfill(zeros)
    print(formatted_number)

    imgFile = r"C:\Users\yazan\OneDrive\Desktop\dataset 50\{}.png".format(formatted_number)
    img = cv2.imread(imgFile)
    origin_image = img.copy()
    cv2.imwrite(folder_path.__add__("\original_image.png"), img)


    def imshow(img, showAxis=False, size=(20, 10)):
        plt.figure(figsize=size)
        if not showAxis: plt.axis('off')
        if len(img.shape) == 3:
            plt.imshow(img[:, :, ::-1])
        else:
            plt.imshow(img, cmap='gray')


    imshow(img)
    cv2.imwrite(folder_path.__add__("\image.png"), img)

    # Blur & detect the edges

    # Convert to Grayscale
    gray = cv2.cvtColor(img.copy(), cv2.COLOR_BGR2GRAY)

    cv2.imwrite(folder_path.__add__("\gray.png"), gray)

    # Blur to remove noise
    blur = cv2.bilateralFilter(gray.copy(), 5, 25, 20)
    cv2.imwrite(folder_path.__add__("\ilter0.png"), blur)


    # Find edges using canny edge detector
    def auto_canny(grayim, sigma=0.93):
        # compute the median of the single channel pixel intensities
        v = np.median(grayim)
        # apply automatic Canny edge detection using the computed median
        lower = int(max(0, (1.0 - sigma) * v))
        upper = int(min(255, (1.0 + sigma) * v))
        edged = cv2.Canny(grayim, lower, upper)
        # return the edged image
        return edged


    # Find the edges and display the image
    # sigma_values = [0.01, 0.8, 1.0, 1.2, 1.5]
    # for count, sigma in enumerate(sigma_values):
    #     edged = auto_canny(blur, sigma)
    #     imshow(edged)
    #     cv2.imwrite(folder_path.__add__("\edges{}.png".format(count)), edged)
    edged = auto_canny(blur, 1.9)
    imshow(edged)
    # cv2.imwrite(folder_path.__add__("\edges{}.png"), edged)
    ## Find Contours

    # detect the contours on the binary image
    contours, _ = cv2.findContours(image=edged.copy(), mode=cv2.RETR_EXTERNAL, method=cv2.CHAIN_APPROX_NONE)
    print(f'Total nr of contours found: {len(contours)}')

    # Sort Contours by Area and get topN
    topN = 10
    sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)
    sorted_contours = sorted_contours[:topN]
    filtered_contours = []
    for contour in contours:
        area = cv2.contourArea(contour)
        if area < 150000 and area > 3500:
            filtered_contours.append(contour)
    #  Fill the area inside contours
    filteredCircle = np.zeros((img.shape[:2]), dtype=np.uint8)
    cv2.drawContours(image=filteredCircle, contours=filtered_contours, contourIdx=-1, color=(255, 255, 255),
                     thickness=cv2.FILLED)

    imshow(filteredCircle)
    cv2.imwrite(folder_path.__add__("\contours10.png"), filteredCircle)

    for i, contour in enumerate(filtered_contours):
        # Create a blank mask image for the contour
        mask = np.ones_like(gray, dtype=np.uint8) * 255

        # Draw the contour on the mask
        cv2.drawContours(mask, [contour], 0, (0, 0, 0), -1)

        # Apply the mask to the original image
        result = cv2.bitwise_and(gray, mask)

        # Find the bounding rectangle around the contour
        x, y, w, h = cv2.boundingRect(contour)

        # Extract the contour as a separate image
        extracted_image = result[y:y + h, x:x + w]

        # Save the extracted image
        cv2.imwrite(folder_path.__add__("\extacted{}.png".format(i)), extracted_image)
    kernel = np.ones((3, 3), np.uint8)
    closedCircle = cv2.morphologyEx(filteredCircle, cv2.MORPH_CLOSE, kernel, iterations=1)
    imshow(closedCircle)
    # cv2.imwrite(folder_path.__add__("\image.png"), closedCircle)
