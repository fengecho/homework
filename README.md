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

1. Extraire les donnée et préparer le dataset et les annotations
 Le dataset fourni par le auteur est au total 3000 images, ils sont mélangés(images avec tomates ou sans tomates). les 2 fichier sont également fournis:
 - **img_annotations.json** : il contient les informations des 3000 images dans le dataset, y compris noms des images, leur bounding boxes et noms des différents aliments qui sont contournés par leur bounding boxes.
 - **label_mapping.sv**: label ID des aliments et son nom correspondant.
 
 

