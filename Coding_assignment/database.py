#!/usr/bin/python

class Database:
    #variable de class
    graph = []
    extract = {}

    def __init__(self, root_node):
        self.name = root_node
        Database.graph.append((self.name, None))

    def add_nodes(self, nodes):
        if isinstance(nodes, list):
            Database.graph = Database.graph + nodes
        else:
            print("pls entrer a list of tuple")

    def add_extract(self, extract):
        if isinstance(extract, dict):
            Database.extract = extract
        else:
            print("pls entrer a dict")

    def get_extract_status(self):
        status = {}
        for image_number, values in Database.extract.items():
            granularity = False
            coverage = False
            for label in values:
                in_first = 0        #pour compter label se trouve combien de fois dans le premier place d'une tuple
                in_second = 0       #pour compter label se trouve combien de fois dans le deuxieme place d'une tuple
                index = 0
                parent_appear_time = 1
                for t in Database.graph[1:]:        #parcourir le graph a partir deuxieme element
                    index += 1
                    if label == t[0]:       #label se trouve dans la 1ere place d'une tuple
                        in_first += 1
                        for tuple in Database.graph[1:]:     #Il n'est pas possible qu'on  trouve 2 fois le meme label dans 1er place des tuple, donc on va compter la presence de son parent node(sauf root nood)
                            if t[1] == tuple[1] and t[1] != Database.graph[0][0]:
                                parent_appear_time += 1
                    if label == t[1]:       #label se trouve dans la deuxieme place d'une tuple
                        in_second += 1
                        for rest_tuple in Database.graph[index+1:]:
                            if label == rest_tuple[0]:
                                in_first += 1
                            if label == rest_tuple[1]:
                                in_second += 1

                if in_first == 0 and in_second == 0:        #label n'exist pas dans la graph, sortir la boucle d'une value(list d'un key) directement, status correspond est "invalid"
                    status[image_number] = "invalid"
                    break
                elif in_first == 0 and in_second >=1:        #label est root node
                    granularity = True
                elif in_first == 1 and in_second >= 1:      #il exist un ou plusieur fils pour ce label
                    granularity = True
                elif in_first == 1 and in_second ==0:       #label existe un seul fois, mais son parent-node present plusieurs fois comme parent-node
                    if parent_appear_time >= 2:
                        coverage = True

            if image_number not in status:      #si label est valid
                if coverage:
                    status[image_number] = "coverage_staged"
                elif granularity is True and coverage is False:
                    status[image_number] = "granularity_staged"
                elif granularity is False and coverage is False:
                    status[image_number] = "valid"

        return status

