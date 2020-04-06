import os
import matplotlib.pyplot as plt
from math import ceil


def show_random_faces(num=5):
    images = []
    i = 0 
    if os.path.exists('faces'):
        for folder in shuffle(os.listdir('faces')):
            if os.path.isdir(os.path.join('faces', folder)) and num!=i:
                for image in shuffle(os.listdir(os.path.join('faces', folder))):
                    if os.path.isfile(os.path.join('faces', folder, image)):
                        images.append([folder, image])
                        i+=1
                        break
    if num in [1, 2, 3]:
        fig = plt.figure(figsize=(4, 4))
    else:
        fig = plt.figure(figsize=(num, num))
    s = ceil(num/2)
    if s == 1:s=2
    for i in range(1, s*s+1):
        if i-1==len(images):break
        img = plt.imread(f'faces/{images[i-1][0]}/{images[i-1][1]}')
        fig.add_subplot(s, s, i)
        plt.title(images[i-1][0])
        plt.imshow(img)
    fig.tight_layout()
    plt.show()
