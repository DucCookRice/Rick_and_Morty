import numpy as np
from PIL import Image
import os
from keras.preprocessing.image import img_to_array


character_array = []
character_label = []
directory = ('C:\\Users\\wadalab\\AIduc\\DucCNN\\morty_data_set')
character_list = ["Morty", "Rick", "Summer", "Meeseeks","Poopybutthole"]

def get_image(character_name):                                                                                  # get the image path from the created folder Morty1 or Rick1 , etc
    file_name = []
    character_name = character_name
    image_dir = os.path.join(directory,character_name+str(1))
    image_file = os.listdir(image_dir)

    for i in range(0,len(image_file)):
        file_name.append(os.path.join(image_dir,image_file[i]))
    return file_name, character_name                                                                           # return to the image path name and character name 


def from_img_to_array(character_image,character_name):                                                          
    character_name = character_name
    for i in character_image:
        img = Image.open(i)                                                                                     # import the image using pillow - Image.open
        #img = img.astype('float32')
        img = img.resize((200,200))                                                                             # resize the image to 200 x 200 pixel
        img = img_to_array(img)                                                                                 # convert the image to array ( 3 channel RGB )

        img = img / 255                                                                                         # Standardize image array

        character_array.append(img)                                                                             # save the image to a list 

        character_label.append(character_name)                                                                  # create a label list 


def preprocess(character_name):                                                                                 # this function is used to execute the above 2 function
    character_image, character_name = get_image(character_name)
    from_img_to_array(character_image, character_name)


def data_set():                                                                                                # the main , for the character in the list , preprocess data 
    for i in character_list:
        preprocess(i)
    
    return character_array , character_label
    
def main():
    character_array = []
    character_label = []
    directory = ('C:\\Users\\wadalab\\AIduc\\DucCNN\\morty_data_set')
    character_list = ["Morty", "Rick", "Summer", "Meeseeks","Poopybutthole"]
    data_set()

    return character_array , character_label
if __name__ == "__main__":
    main()