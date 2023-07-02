# Stamp classification

## Description
We provide stamp detection, classification and comparison using Computer Vision.
The user only needs to upload the document scans.

## Methodology
- **Data augmentation**. We create our own dataset of documents with stamps, based on the datasets we found online and our own scans.
- **Stamp detection**. We detect stamp(s) on the given image (of a document) and its location (coordinates on the document) using image processing.
- **Stamp embedding**. We create stamp embeddings from an image of the stamp, using a fine-tuned EfficientNetB0 model.
- **Classification**. From the embeddings, we calculate the distance between them (cosine similarity) and provide classification.

## Usage of the API
- POST    /auth/sign_in/email - allows the user to sign in with email and password.
- POST    /auth/login/google - allows the user to sign in using their google account.
- POST    /auth/login/email - allows the user to login in with email and password.
- POST    /images/upload - allows the user to upload image(s) that they want to detect and classify the stamps on.
    - Input - scans of documents in an image format.
    - Output - [{stamp_name, stamp_picture, accuracy}, …]
- POST    /feedback/add_stamps - allows the user to add new stamps to the database.
    - Input - [{stamp_name, stamp_picture}, …]
- POST    /feedback/report - allows the user to report any possible errors or classification problems.
    - Input - text and an image (optional).
- POST    /images/compare - allows the user to compare two images of the stamps in order to check validity.
    - Input - 2 scans of documents in an image format.
    - Output - similarity score.
- GET     /help - returns instructructions on how to use the API.

## References:

Articles:
- [EfficientNet: Improving Accuracy and Efficiency through AutoML and Model Scaling](https://ai.googleblog.com/2019/05/efficientnet-improving-accuracy-and.html)
- [Image classification via fine-tuning with EfficientNet](https://keras.io/examples/vision/image_classification_efficientnet_fine_tuning/#transfer-learning-from-pretrained-weights)


Code:
- [Original EfficientNet GitHub](https://github.com/qubvel/efficientnet)
- [EfficientNet Tutorial GitHub](https://github.com/rom1504/image_embeddings)

Data:
- [Stamp verification dataset](https://www.kaggle.com/datasets/rtatman/stamp-verification-staver-dataset)
- [Stamps dataset](https://www.kaggle.com/datasets/weisinx7/stamps-dataset)
- [Noisy documents datase](https://www.kaggle.com/datasets/sthabile/noisy-and-rotated-scanned-documents)
