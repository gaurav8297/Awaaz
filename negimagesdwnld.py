import urllib
import cv2
import numpy as np
import os

def store_raw_images():
    neg_images_link = 'http://image-net.org/api/text/imagenet.synset.geturls?wnid=n07942152'
    neg_image_urls = urllib.urlopen(neg_images_link).read().decode()
    pic_num = 1

    if not os.path.exists('neg'):
        os.makedirs('neg')
    c=0
    for i in neg_image_urls.split('\n'):
        try:
            if pic_num>138:
                print(i)
                urllib.urlretrieve(i, "neg/" + str(pic_num) + ".jpg")
                # img = cv2.imread("neg/" + str(pic_num) + ".jpg", cv2.IMREAD_GRAYSCALE)
                # # should be larger than samples / pos pic (so we can place our image on it)
                # # resized_image = cv2.resize(img, (100, 100))
                # cv2.imwrite("neg/" + str(pic_num) + ".jpg", img)
            pic_num += 1

        except Exception as e:
            print(str(e))


def find_uglies():
    match = False
    c=1
    for file_type in ['neg']:
        for img in os.listdir(file_type):
            for ugly in os.listdir('uglies'):
                try:
                    current_image_path = str(file_type)+'/'+str(img)
                    ugly = cv2.imread('uglies/'+str(ugly))
                    question = cv2.imread(current_image_path)
                    if ugly.shape == question.shape and not(np.bitwise_xor(ugly,question).any()):
                        print('That is one ugly pic! Deleting!')
                        print(current_image_path)
                    os.rename(current_image_path,str(c)+".jpg")
                    c+=1
                except Exception as e:
                    print(str(e))
                    os.remove(current_image_path)
store_raw_images()
#find_uglies()

