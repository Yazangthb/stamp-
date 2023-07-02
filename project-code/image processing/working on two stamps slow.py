from PIL import Image
import numpy as np


def sort_indexes_by_difference(lst,ind):
    indexes = [(abs(lst[el][ind]-lst[el+1][ind]),el,el+1) if el < len(lst)-1 else (0,el,el) for el,ele in enumerate(lst) ]
    indexes.sort(key=lambda e:e[0],reverse=True)
    return indexes



def remove_black_pixels(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to RGBA mode
    image = image.convert("RGBA")

    # Get the image data as a list of pixels
    pixels = list(image.getdata())
    tple=image.size.__add__((4,))
    print(tple)

    sub_lists = [pixels[i:i + tple[0]] for i in range(0, len(pixels), tple[0])]
    arr=np.array(image.getdata())
    # Create a new list to store the modified pixels
    new_pixels = []
    coordinates=list()

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
    print(coordinates)
    new_image.save( "C:\\Users\\Yazan\\Desktop\\IP tests\\image{}.png".format("filtered"))
    all_x=sort_indexes_by_difference(coordinates,0)
    print(all_x)
    for onex in all_x:
        print(abs(coordinates[onex[1]][0]-coordinates[onex[2]][0]))
    xs=list()
    for onex in all_x:
        if(onex[0]<50):
            xs.append(onex)
            break
        else: xs.append(onex)
    xmin=list()
    xmax=list()
    xmax.append(coordinates[xs[0][1]])
    xmin.append(coordinates[xs[0][2]])
    xmin.append(coordinates[xs[1][1]])
    xmax.append(coordinates[xs[1][2]])
    print(xmin[0])
    print(xmax[0])
    print(xmin[1])
    print(xmax[1])
    # xmin.append(coordinates[0][0])
    # xmax=coordinates[len(coordinates)-1][0]
    # coordinates.sort(key=lambda e:e[1])
    # ymin = coordinates[0][1]
    # ymax = coordinates[len(coordinates)-1][1]
    #
    cropped_image = image.crop((xmax[0][1], 0, xmax[1][1], image.height))
    cropped_image2 = image.crop((xmin[0][1], 0, xmin[1][1], image.height))
    cropped_image.save( "C:\\Users\\Yazan\\Desktop\\IP tests\\image {}.png".format("square1"))
    cropped_image2.save( "C:\\Users\\Yazan\\Desktop\\IP tests\\image {}.png".format("square2"))
    # print(xmin,xmax,ymin,ymax)
    # Save the new image
    square_output_path = "C:\\Users\\Yazan\\Desktop\\IP tests\\image{}.png".format("square")
    # crop_square(image_path, xmin, xmax, ymin, ymax, square_output_path)
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
from PIL import Image
import numpy as np


def sort_indexes_by_difference(lst,ind):
    indexes = [(abs(lst[el][ind]-lst[el+1][ind]),el,el+1) if el < len(lst)-1 else (0,el,el) for el,ele in enumerate(lst) ]
    indexes.sort(key=lambda e:e[0],reverse=True)
    return indexes



def remove_black_pixels(image_path, output_path):
    # Open the image
    image = Image.open(image_path)
    # Convert the image to RGBA mode
    image = image.convert("RGBA")

    # Get the image data as a list of pixels
    pixels = list(image.getdata())
    tple=image.size.__add__((4,))
    print(tple)

    sub_lists = [pixels[i:i + tple[0]] for i in range(0, len(pixels), tple[0])]
    arr=np.array(image.getdata())
    # Create a new list to store the modified pixels
    new_pixels = []
    coordinates=list()

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
    print(coordinates)
    xmin=list()
    xmax=list()
    xmin.append(coordinates[0][0])
    xmax.append(coordinates[len(coordinates)-1][0])
    new_image.save("C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("filtered"))
    all_x=sort_indexes_by_difference(coordinates,0)
    print("allx")
    print(all_x)
    print(coordinates[942])
    print(coordinates[943])

    for onex in all_x:
        print(abs(coordinates[onex[1]][0]-coordinates[onex[2]][0]))
    xs=list()
    for onex in all_x:
        if(onex[0]<50):
            xs.append(onex)
            break
        else: xs.append(onex)


    xmin.append(coordinates[xs[0][1]])
    xmax.append(coordinates[xs[0][2]])
    print(xmin[0])
    print(xmax[0])
    print(xmin[1])
    print(xmax[1])
    # xmin.append(coordinates[0][0])
    # xmax=coordinates[len(coordinates)-1][0]
    # coordinates.sort(key=lambda e:e[1])
    # ymin = coordinates[0][1]
    # ymax = coordinates[len(coordinates)-1][1]
    #
    cropped_image = image.crop((xmin[0], 0, xmin[1][0], image.height))
    cropped_image2 = image.crop((xmax[1][0], 0, xmax[0], image.height))
    cropped_image.save("C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("sq1"))
    cropped_image2.save("C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("sq2"))
    # print(xmin,xmax,ymin,ymax)
    # Save the new image
    square_output_path = "C:\\Users\\Yazan\\Desktop\\IP tests\\image{}.png".format("square")
    # crop_square(image_path, xmin, xmax, ymin, ymax, square_output_path)
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
image_path = "C:\\Users\\yazan\\OneDrive\\Desktop\\stamp.png"
output_path =  "C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("with numpy")



remove_black_pixels(image_path, output_path)
