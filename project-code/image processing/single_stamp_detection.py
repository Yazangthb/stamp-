from PIL import Image
import numpy as np
def remove_black_pixels(image_path, output_path):
    # Open the image
    image = Image.open(image_path)

    # Convert the image to RGBA mode
    image = image.convert("RGBA")

    # Get the image data as a list of pixels
    pixels = list(image.getdata())
    sub_lists = [pixels[i:i + 686] for i in range(0, len(pixels), 686)]
    arr=np.array(image.getdata())
    # Create a new list to store the modified pixels
    new_pixels = []
    coordinates=list()
    tple=image.size.__add__((4,))
    print(tple)

    print(len(image.getdata()))
    print(836*558)
    # for i in image.getdata():
    #     print(i)
    pixelsnp=np.empty(tple)
    pixelsnp=sub_lists


    # Iterate over each pixel
    # comment
    for pixelist in pixelsnp:
        # Check if the pixel is black
        for pixel in pixelist:
            if pixel[0] >200 and pixel[1]<120 and pixel[2]<120:
                # Add non-black pixel to the new list
                new_pixels.append(pixel)
                coordinates.append((pixelist.index(pixel),pixelsnp.index(pixelist)))
            else: new_pixels.append((255,255,255))
        for p in new_pixels:
            if p[:]!=(255,255,255):
                pp=p
                while pp==(255,255,255):
                    pp=(255,0,0)
                    pp+=1

    # Create a new image with the modified pixel data
    new_image = Image.new("RGBA", image.size)
    new_image.putdata(new_pixels)
    coordinates.sort(key=lambda e:e[0])
    xmin=coordinates[0][0]
    xmax=coordinates[len(coordinates)-1][0]
    coordinates.sort(key=lambda e:e[1])
    ymin = coordinates[0][1]
    ymax = coordinates[len(coordinates)-1][1]

    print(xmin,xmax,ymin,ymax)
    # Save the new image
    square_output_path = "C:\\Users\\Yazan\\Desktop\\IP tests\\image{}.png".format("square")
    new_image.save(output_path)
    crop_square(image_path, xmin, xmax, ymin, ymax, square_output_path)
    print("Image with black pixels removed saved successfully!")

def crop_square(image_path, xmin, xmax, ymin, ymax, output_path):
    # Open the image
    image = Image.open(image_path)

    # Crop the square region based on the given coordinates
    square_image = image.crop((xmin, ymin, xmax, ymax))

    # Save the cropped image
    square_image.save(output_path)

    print("Square region cropped and saved successfully!")


# Example usage



# Example usage
image_path = "C:\\Users\\Yazan\\Desktop\\stamp - Copy.png"
output_path =  "C:\\Users\\Yazan\\Desktop\\IP tests\\image{}.png".format("with numpy")


remove_black_pixels(image_path, output_path)

