#equivalent to id2word.npy and word2id.npy ,train_captions and train_images

import numpy as np
import cv2
import glob

import pickle

encoding = {} #dictionary
#Open the file
with open("C:/Users/omkar waghmare/Desktop/text to image/text-to-image-master/captions.txt", 'r') as my_File:
    #Read the files
    contents = my_File.readlines()
    my_File.seek(0)
    read_File = my_File.read()

#Split the words
    words = read_File.split()
    #print(words)
#Using a set will only save the unique words
unique_words = set(words)
print(len(unique_words))
print("*******************************")

i= 1000
for a in unique_words:
	encoding[a] = i
	i = i+1

encoding["<PAD>"]=i

#creating train_captions.npy
final_array = np.empty(shape = (8106,1)) 
final_list = list()

for line in contents:
    line = line.replace("\n" , "")
    listOfWords = list()
    i = 0
    for word in line.split(" "):
        listOfWords.append(np.str_(encoding[word]))
    
    while len(listOfWords) < 20:
        listOfWords.append(np.str_(encoding["<PAD>"]))

    # print(listOfWords) # Works


    listOflist = list()
    while i < 5:
        listOflist.append(listOfWords)
        i+=1

    final_list.append(listOflist)
    #print(final_list)

    #np.append(arr = final_array , values = listOflist, axis=0)

#final_final_array = np.array(final_list)
np.save("train_captions_dog.npy",final_list)
print(len(final_list))
print(type(final_list[0]))



with open("C:/Users/omkar waghmare/Desktop/text to image/text-to-image-master/captions_dog.txt", "wb+") as fp:   #Pickling
    pickle.dump(final_list, fp)


'''
np.insert(arr=final_array, obj = 0 ,values = final_list, axis=0)
print(len(final_list))
np.save("train_captions_dog.npy",final_array)
test = np.load("train_captions_dog.npy")
print(".SHAPETEST",test.shape)
'''

np.save("word2id_dog.npy",encoding)
print("Saved words to ID")

#reversing the dictionary
id2word = {v: k for k, v in encoding.items()}
np.save("id2word_dog.npy",id2word)
print("Saved ID to word")

#creating train_images
X_data = []
files = glob.glob ("C:\\Users\\omkar waghmare\\Desktop\\text to image\\text-to-image-master\\imgs_dog_V2\\*.jpg")
for myFile in files:
    #print(myFile)
    image = cv2.imread (myFile) 
    X_data.append (image)

print(len(X_data))
np.save('C:/Users/omkar waghmare/Desktop/text to image/text-to-image-master/train_images_dog.npy',np.array(X_data))
print("Saved Images as numpy")
print("SAvedddddddddddddddddddddddddd")