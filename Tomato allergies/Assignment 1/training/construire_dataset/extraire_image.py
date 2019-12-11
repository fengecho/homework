import shutil
import json
import os

with open("tomate_image.json",'r') as load_f:        #lire le fichier json
    load_dict = json.load(load_f)
    for k in load_dict:
        if os.path.exists("assignment_imgs/"+ k):
            shutil.copyfile("assignment_imgs/"+ k, "tomate_images_set/"+ k)