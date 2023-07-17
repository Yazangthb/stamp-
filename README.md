# Stamp recognition

## Project Description
Our project offers a solution for stamp detection, classification, and comparison using Maching learning and Computer Vision techniques. The primary goal is to facilitate the identification and analysis of stamps present in document scans.

## Authors and acknowledgment
- Yazan Alnakri: Image processing, data augmentation, API design
- Laith Nayal: Image processing, data augmentation, API design
- Osama Orabi: ML engineer, data scientist, cleaning data.
## Demo
### Classify the stamp on the image
- ![Request](https://drive.google.com/file/d/11BNO1TdvKf4hVhaczPbF38tG8mK1rkmC/view?usp=drive_link)
- ![Good response](https://drive.google.com/file/d/1gidMT8Ohe04btB_s1zTkC3ynDJZ4kwL3/view?usp=drive_link)
- ![Response with errors:](https://drive.google.com/file/d/1iBvDWP606L1fo8l4DhSpGclE4i_1qanc/view?usp=drive_link)
### Add new stamp to the database
- ![Request](https://drive.google.com/file/d/15gpQR2Ytj8OPzcApF_1U6TOre-UZe4wG/view?usp=drive_link)
- ![Response](https://drive.google.com/file/d/1Z8gMqiPFSar0Cf3yB8PTDBy7X3GEwZdz/view?usp=drive_link)

## How to use
- POST    /images/upload - allows the user to upload images that they want to detect and classify the stamps on.
    - Input - scans of document in an image format (png, jpg) and the names for the corresponding stamps.
    - Output - [{stamp_name, stamp_picture, accuracy}, …]
- POST    /images/add_stamp - allows the user to add new stamps to the database.
    - Input - {[stamp_name1, stamp_name2, ...], document_picture}
- Requests that will be added soon
    - POST    /images/compare - allows the user to compare two images of the stamps in order to check validity.
        - Input - 2 scans of documents in an image format.
        - Output - similarity score.
    - GET     /help - returns instructructions on how to use the API.

## Features

Our project offers the following key features, divided into four parts:

### 1. Data Augmentation

- **Creation of a dataset**: We generate a comprehensive dataset of documents with stamps by combining real documents with stamps generated with Stable Diffusion.

### 2. Stamp Detection

- **Detection**: Our system identifies stamp(s) present in document images using advanced image processing techniques.
- **Location determination**: We precisely locate the detected stamp(s) on the document, providing their coordinates.

### 3. Stamp Embedding

- **Feature extraction**: We utilize out own CNN model to generate embeddings from stamp images.
- **Vectorization of stamps**: The embeddings represent stamps as high-dimensional vectors, capturing their unique characteristics.

### 4. Classification

- **Distance calculation**: From the embeddings, we calculate the cosine similarity to measure the similarity between stamps.
- **Classification**: Based on the calculated distances, our system provides reliable classification results for stamps.

## Technologies used
- Backend: Python, SQLight, Flask, Pydantic, Werkzeug, unit-testing
- Detection: Edge detection, Bluring, Python, cv2, matplotlib, numpy
- Embeddings: CNN, Image preprocessing, Python, tensorflow, numpy, scipy, matplotlib
- Dataset augmentation: Stable diffusion, Photoshop, Blender, Python

## Badges
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
