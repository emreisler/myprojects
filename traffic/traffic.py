import cv2
import numpy as np
import os
import sys
import tensorflow as tf

from sklearn.model_selection import train_test_split

#Prevent warnings in terminal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

EPOCHS = 10
IMG_WIDTH = 30
IMG_HEIGHT = 30
NUM_CATEGORIES = 43
TEST_SIZE = 0.4

def main():

    # Check command-line arguments
    if len(sys.argv) not in [2, 3]:
        sys.exit("Usage: python traffic.py data_directory [model.h5]")

    # Get image arrays and labels for all image files
    images, labels = load_data(sys.argv[1])

    # Split data into training and testing sets
    labels = tf.keras.utils.to_categorical(labels)
    x_train, x_test, y_train, y_test = train_test_split(
        np.array(images), np.array(labels), test_size=TEST_SIZE
    )

    # Get a compiled neural network
    model = get_model()

    # Fit model on training data
    model.fit(x_train, y_train, epochs=EPOCHS)

    # Evaluate neural network performance
    model.evaluate(x_test,  y_test, verbose=2)

    # Save model to file
    if len(sys.argv) == 3:
        filename = sys.argv[2]
        model.save(filename)
        print(f"Model saved to {filename}.")


def load_data(data_dir):
    #create an empty images list
    images = list()

    # create an empty labels list
    labels = list()

    #go to data directory
    for filename in os.listdir(data_dir):
        for file in os.listdir(f"{data_dir}/{filename}"):
            #Convert images to NP array
            img = cv2.imread(f"{data_dir}/{filename}/{file}")

            #Resize images to make all image arrays same dimensions
            resized = cv2.resize(src=img, dsize=(IMG_WIDTH, IMG_HEIGHT), interpolation=cv2.INTER_AREA)

            #append resized image to images list
            images.append(resized)

            #append folder names as label in labels list
            labels.append(filename)

    return images, labels

    """
    Load image data from directory `data_dir`.

    Assume `data_dir` has one directory named after each category, numbered
    0 through NUM_CATEGORIES - 1. Inside each category directory will be some
    number of image files.

    Return tuple `(images, labels)`. `images` should be a list of all
    of the images in the data directory, where each image is formatted as a
    numpy ndarray with dimensions IMG_WIDTH x IMG_HEIGHT x 3. `labels` should
    be a list of integer labels, representing the categories for each of the
    corresponding `images`.
    """



def get_model():
    #create a sequential model
    model = tf.keras.Sequential([

        tf.keras.layers.Conv2D(32,(3,3), activation="relu",input_shape=(IMG_WIDTH,IMG_HEIGHT,3)),
        tf.keras.layers.MaxPooling2D(pool_size=(3,3)),

        #Inputs
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(0.2),

        # hidden layer
        tf.keras.layers.Dense(NUM_CATEGORIES * 32 , activation="relu"),
        tf.keras.layers.Dropout(0.2),

        #hidden layer
        tf.keras.layers.Dense(NUM_CATEGORIES * 16, activation="relu"),

        # hidden layer
        tf.keras.layers.Dense(NUM_CATEGORIES * 8, activation="relu"),


        #Output layer
        tf.keras.layers.Dense(NUM_CATEGORIES,activation="softmax")
    ])

    # check neural network model visaully
    print(model.summary())

    #compile the model
    model.compile(loss='categorical_crossentropy', optimizer='adam',metrics=["accuracy"])

    return model
    """
    Returns a compiled convolutional neural network model. Assume that the
    `input_shape` of the first layer is `(IMG_WIDTH, IMG_HEIGHT, 3)`.
    The output layer should have `NUM_CATEGORIES` units, one for each category.
    """



if __name__ == "__main__":
    main()
