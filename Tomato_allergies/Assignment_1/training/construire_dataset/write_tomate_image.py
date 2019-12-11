import json

labels_tomate = ["939030726152341c154ba28629341da6_lab", "9f2c42629209f86b2d5fbe152eb54803_lab",        #labels des tomates
                 "4e884654d97603dedb7e3bd8991335d0_lab", "f3c12eecb7abc706b032ad9a387e6f01_lab",
                 "e306505b150e000f5e1b4f377ad688a0_lab"]

new_dict = {}       #initialisation d'unne nouvelle dictionnaire
with open("img_annotations.json",'r') as load_f:
    load_dict = json.load(load_f)
    for k in load_dict:     #iteration des keys
        for sous_dict in load_dict[k]:      #iteration dans le list(valeur de key)
            if sous_dict["id"] in labels_tomate:
                new_dict[k] = load_dict[k]      #si il y la tomate dans la valeur, on sauvegarde ensemble de ce key et sa valeur dans un nouveau dictionnaire

with open("tomate_image.json",'w') as f:        #écire ce dictionnaire dans un nouveau fichier json
    json.dump(new_dict, f)

