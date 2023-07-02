from PIL import Image
import numpy as np
import time


def traverse_pixels(coordinates, start_pixel):
    current_pixel = start_pixel
    shape = [current_pixel]
    next_pixel = find_next_pixel(coordinates, current_pixel)

    while next_pixel != start_pixel:
        shape.append(next_pixel)
        current_pixel = next_pixel
        next_pixel = find_next_pixel(coordinates, current_pixel)

    return shape


def find_next_pixel(coordinates, current_pixel):
    x, y = current_pixel
    boundx,boundy=0,0
    while boundx<5 and boundy<5:
        # Check the right-up direction
        next_pixel = (x + 1, y - 1)
        if next_pixel in coordinates:
            return next_pixel

    return None


def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time for {func.__name__}: {execution_time} seconds")
        return result
    return wrapper

@timer_decorator
def sort_indexes_by_difference(lst, ind,reverse=True):
    lst = np.asarray(lst)  # Convert the input to a numpy array
    indexes = [(np.abs(lst[el][ind] - lst[el+1][ind]), el, el+1) if el < len(lst)-1 else (0, el, el) for el in range(len(lst))]
    indexes.sort(key=lambda e: e[0], reverse=reverse)
    print(indexes)
    return indexes


def remove_black_pixels(image_path, output_path):
    # Open the image
    bb=time.time()
    image = Image.open(image_path)
    # Convert the image to RGBA mode
    image = image.convert("RGBA")
    begin=time.time()
    # Get the image data as a list of pixels
    # pixels = list(image.getdata())
    pixels = np.array(image)
    # print(np.where(pixels!=[255,255,255,255]))
    print(pixels.shape)
    end = time.time()
    print(end - begin)
    # Display the shape and data type of the array
    print("Array Shape:", pixels.shape)
    print("Data Type:", pixels.dtype)
    tple=tuple(pixels.shape)
    print(tple)
    print("------------")
    # Create a new list to store the modified pixels
    new_pixels = []
    coordinates=list()

    print(len(image.getdata()))
    print(836*558)


    s = time.time()
    new_pixels = []
    coordinates = []

    # Iterate over each pixel
    # comment
    s=time.time()
    print(pixels.shape)

    # Create an array of True/False values based on the condition
    mask = (pixels[:, :, 0] > 200) & (pixels[:, :, 1] < 120) & (pixels[:, :, 2] < 120)

    # Create a new array with the non-black pixels or (255, 255, 255) values
    new_pixels = np.where(mask[..., np.newaxis], pixels, np.array([255, 255, 255, 255], dtype=np.uint8))

    # Get the coordinates of the non-black pixels
    coordinates = np.argwhere(mask)
    print("coord",coordinates.shape)
    # Modify the non-(255, 255, 255) pixels
    new_pixels[np.where(np.all(new_pixels == [255, 255, 255, 255], axis=-1))] = [255, 0, 0, 255]
    en=time.time()
    print("loop time is: ",en-s)
    # Create a new image with the modified pixel data
    # new_image = Image.new("RGBA", image.size)
    # new_image.putdata(pixels)
    coordinates=np.sort(coordinates, axis=0)
    print("printed array of coordinates:")
    print(coordinates)
    xmin=list()
    xmax=list()
    xmin.append(coordinates[0][1])
    xmax.append(coordinates[len(coordinates)-1][1])
    # new_image.save("C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("filtered"))
    all_x=sort_indexes_by_difference(coordinates,1)
    print("len",len(all_x),len(coordinates))
    all_y=sort_indexes_by_difference(coordinates,0,reverse=False)
    print("allx")
    # print(all_x)
    print(coordinates[942])
    print(coordinates[943])
    print("ally")
    # print(all_y)
    # for onex in all_x:
    #     print(abs(coordinates[onex[1]][0]-coordinates[onex[2]][0]))
    # xs=list()
    min_points_indices=[]
    for onex in all_x:
        print(onex)
        if(onex[0]<50):
            # xs.append(onex)
            break
        else:
            # xs.append(onex)
            min_points_indices.append(onex[2])
            xmax.append(coordinates[onex[1]][1])
            xmin.append(coordinates[onex[2]][1])

    # print(xs[0][1])
    # xmax.append(coordinates[xs[0][1]][1])
    # xmin.append(coordinates[xs[0][2]][1])
    print(xmin)
    print(xmax)
    print("--------------")
    print(xmin[0])
    print(xmax[0])
    print(xmin[1])
    print(xmax[1])
    print("--------------")

    xmax.sort()
    print(xmax)
    # after finding the x points for the two stamps you need to find the y
    # you start with either xmin for the stamp and then walk through the neighbour pixels unitil the pixels y
    # coordinates start becoming higher(with the assumption that we are finding the ymin
    # coordinates = np.sort(coordinates, axis=1)
    ymin = []
    ymax = []
    # for start_point in min_points_indices:
    #     while coordinates[start_point][1]-coordinates[start_point-1][1]>=0:
    #         print(coordinates[start_point][1]-coordinates[start_point-1][1])
    #         start_point+=1
    #     ymin.append(last)
    #
    print(coordinates)
    filtered_coordinates = coordinates[(coordinates[:, 1]>= xmin[0]) & (coordinates[:, 1] <= xmax[0])]
    filtered_coordinates=np.sort(filtered_coordinates, axis=0)


    cropped_image = image.crop((xmin[0], filtered_coordinates[0][0], xmax[0], filtered_coordinates[len(filtered_coordinates)-1][0]))
    filtered_coordinates = coordinates[(coordinates[:, 1] >= xmin[1]) & (coordinates[:, 1] <= xmax[1])]
    filtered_coordinates = np.sort(filtered_coordinates, axis=0)
    cropped_image2 = image.crop((xmin[1], filtered_coordinates[0][0], xmax[1], filtered_coordinates[len(filtered_coordinates)-1][0]))
    cropped_image.save("C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("sq1"))
    cropped_image2.save("C:\\Users\\yazan\\OneDrive\\Desktop\\IP tests\\image{}.png".format("sq2"))
    # print(xmin,xmax,ymin,ymax)
    # Save the new image
    square_output_path = "C:\\Users\\Yazan\\Desktop\\IP tests\\image{}.png".format("square")
    # crop_square(image_path, xmin, xmax, ymin, ymax, square_output_path)
    print("Image with black pixels removed saved successfully!")
    print("function time approximately: ",time.time()-bb)

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
