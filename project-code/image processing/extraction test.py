import random
import numpy as np


def traverse_neighbors(pixel, coordinates):
    x, y = pixel
    neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]  # Define the neighbors (adjust if needed)
    connected_pixels = []

    for neighbor in neighbors:
        if neighbor in coordinates:
            connected_pixels.append(neighbor)
            coordinates.remove(neighbor)

    return connected_pixels


def extract_shape(coordinates):
    if len(coordinates) == 0:
        return None

    start_pixel = random.choice(coordinates)
    connected_pixels = [start_pixel]
    coordinates.remove(start_pixel)

    while True:
        current_pixel = connected_pixels[-1]
        neighbors = traverse_neighbors(current_pixel, coordinates)

        if len(neighbors) == 0:
            break

        connected_pixels.extend(neighbors)

    # Determine the shape's boundaries
    x_coordinates, y_coordinates = zip(*connected_pixels)
    xmin, xmax = min(x_coordinates), max(x_coordinates)
    ymin, ymax = min(y_coordinates), max(y_coordinates)

    return connected_pixels, xmin, xmax, ymin, ymax


def extract_all_shapes(coordinates):
    shapes = []

    while True:
        result = extract_shape(coordinates)

        if result is None:
            break

        connected_pixels, xmin, xmax, ymin, ymax = result
        shapes.append((connected_pixels, xmin, xmax, ymin, ymax))

    return shapes
# Example usage
coordinates = [(1, 1), (1, 2), (2, 1), (3, 3), (4, 4), (5, 5), (5, 6), (6, 6), (7, 7)]

shapes = extract_all_shapes(coordinates)

# Print the extracted shapes
for shape in shapes:
    connected_pixels, xmin, xmax, ymin, ymax = shape
    print("Shape: ", connected_pixels)
    print("xmin:", xmin, "xmax:", xmax, "ymin:", ymin, "ymax:", ymax)
    print()
