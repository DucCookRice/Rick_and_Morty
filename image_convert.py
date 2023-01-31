import numpy as np
import os
from PIL import Image
from os import listdir


def get_img_name(name):   
    file_directory = []                                                                  # blank list to store all file path (directory)
    file_name_new = []
    character_name = name                                                                # character name , for example : Morty , Rick , ... must have ""

    folder = os.path.join(directory, character_name)                                     # create a path for each character image directory
    file_name = os.listdir(folder)                                                       # list every object in the character image directory

    for i in range(0,len(file_name)):                                                    # this for loop is to create all the directory for all images in the folder 
        direct = os.path.join(folder,file_name[i])
        file_directory.append(direct)
        file_name_new.append(os.path.splitext(file_name[i]))
    return file_directory , character_name , folder , file_name_new , file_name     


def make_new_dir(character_name):                                                        # make new directory to store image  return to the new directory path
    new_path = os.path.join(directory,(character_name + str(1)))
    try:
        os.makedirs(new_path)
    except IOError :                                                                     #  if already exist such directory then skip 
        return new_path
    else :
        return new_path                                                                  # return to the new directory path
    

def check_img(file_directory,new_path,file_name_new):                                    # check if image is jpg or png , if jpg then save the image in the new directory created before 
    
    for i in range(0,len(file_directory)):

        img = Image.open(file_directory[i])

        new_img_path = os.path.join(new_path,file_name_new[i][0])                        

        if img.format =='JPEG':

            img.save(new_img_path +".jpg","JPEG")                                        # if jpg then save the image in the new directory created before

        if img.format =='PNG':
            new_img_path = os.path.join(new_path,file_name_new[i][0])
            img.convert('RGB').save(new_img_path +".jpg" ,"JPEG")                        # if png then convert the image t RGB mode then save as jpg file in the new directory created before



def img_convert(character_name):                                                          # get the image in the image folder , check , convert to jpg file and then save in new directory             
    file_directory , character_name , folder , file_name_new , file_name = get_img_name(character_name)
    new_path = make_new_dir(character_name)
    check_img(file_directory,new_path,file_name_new)

def main():
    for i in character_list :
        img_convert(i)


if __name__ == "__main__":
    directory = ('C:\\Users\\wadalab\\AIduc\\DucCNN\\morty_data_set')
    character_list = ["Morty", "Rick", "Summer", "Meeseeks","Poopybutthole"]
    main()
    print("Done")
