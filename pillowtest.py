from PIL import Image
from keras.preprocessing.image import img_to_array
import matplotlib.pyplot as plt
morty = (r"C:\Users\wadalab\AIduc\DucCNN\morty.png")
morty = Image.open(morty)
morty = morty.resize((200,200))
plt.imshow(morty)
plt.show()
#morty1.save(r"C:\Users\wadalab\AIduc\DucCNN\morty1.jpg")
#r , g, b = morty1.split()
##img_array = img_to_array(morty1)
#morty2 = Image.merge("RGB",(r,g,b))
