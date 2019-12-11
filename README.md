# homework

Ce test contient 2 parties:
  1. Test programmation: Coding assignment
  2. Projet sur vision par ordinateur: Tomato allergies
## Coding assignment

Ce test issu de [Coding assignment - Food database](https://github.com/Foodvisor/coding-assignment). 
le répertoire [Code_assignement](https://github.com/fengecho/homework/tree/master/Coding_assignment) contient 3 fichiers suivants:
- `database.py`: il contient un class `Database`
- `test.py` : code à tester les 2 exemples fournis par le sujet
- `test_release.py` : code à tester les données issues de [release](https://github.com/Foodvisor/coding-assignment/releases/tag/v0.1.0)

### Run
pour utiliser les codes, il suiffit de télécharger les 3 fichiers du répertoire [Code_assignement](https://github.com/fengecho/homework/tree/master/Coding_assignment) et de les mettre ensemble dans un répertoire. Vous pouvez taper `python test.py`,  `python test_release.py` pour les exécuter sur **terminal** ou **command windows** ou bien Run les fichier `python test.py`,  `python test_release.py` directement sur un logicielle comme **Pycharme**



## Home assignment - Tomato allergies

Ce test issu du sujet [Home assignment - Tomato allergies - Assignment # 1](https://github.com/Foodvisor/home-assignment#assignment--1)
je l'ai fait en **Tensorflow 1.14**, pre-trained model [ssd_mobilenet_v1_coco_2018_01_28](http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_coco_2018_01_28.tar.gz). Le model est entraîné sur AWS EC2 avec la carte graphique Tesla K80. Il contient 2 parties:
- **Training**
- **Test**


### Training 

1. Extraire les donnée
 Le dataset fourni par le auteur est au total 3000 images, ils sont mélangés(images avec tomates ou sans tomates). les 2 fichier sont également fournis:
 - **img_annotations.json** : il contient les informations des 3000 images dans le dataset, y compris noms des images, leur bounding boxes et noms des différents aliments qui sont contournés par leur bounding boxes.
 - **label_mapping.sv** : label ID des aliments et son nom correspondant.
 
 Comme nous voulons détecter les tomates entiers ou en morceau(pas le jus), nous devons trouver les labels qui représent les tomates entiers ou en morceau. En faisant la recherche j'ai trouvé 5 labels qui représentent les tomates entiers ou en morceau, Ils sont:
- 939030726152341c154ba28629341da6_lab,Tomates (coupées),Tomatoes
- 9f2c42629209f86b2d5fbe152eb54803_lab,Tomates cerises,Cherry tomatoes
- 4e884654d97603dedb7e3bd8991335d0_lab,Tomates (entières),Tomatoe whole
- f3c12eecb7abc706b032ad9a387e6f01_lab,Tomate à la provençale,Stuffed Tomatoes
- e306505b150e000f5e1b4f377ad688a0_lab,Tomate farcie,Stuffed tomatoes
A partir des 5 labels, j'ai écrit [write_tomate_image.py](Tomato allergies/Assignment 1/training/construire_dataset/write_tomate_image.py), ce fichier extraire les noms des images, leur bouding boxes et leur labels dans une autre fichier `.json` à condition que ces image contiennent un ou plusieurs labels de ces 5 labels. Après, on obtient [tomate_image.json](Tomato allergies/Assignment 1/training/construire_dataset/tomate_image.json), un fichier qui contient tous les informations des images qui ont tomate dedans.

2. Extraire les images de tomate et construire fichiers .xml
Le fichier 

 
 

