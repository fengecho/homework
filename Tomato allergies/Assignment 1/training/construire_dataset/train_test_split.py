import os
import random
import time
import shutil
##############code faire référence à lien suivant https://blog.csdn.net/w5688414/article/details/78970874
xmlfilepath='annotations'
saveBasePath = "./train_val"

trainval_percent = 0.98
train_percent = 0.9
total_xml = os.listdir(xmlfilepath)
num = len(total_xml)
list = range(num)
tv = int(num*trainval_percent)
tr = int(tv*train_percent)       #quantite image a entrainer
te = num - tv       #quantite image au test
trainval = random.sample(list, tv)       #trouve les numéros des ensemble images à entrainer et valider
train = random.sample(trainval, tr)     #trouver les numéros des images à entrainer


print("training size", tr)
print("valider size", tv-tr)
print("test size", te)
# print(total_xml[1])
start = time.time()

# print(trainval)
# print(train)

test_num=0
val_num=0
train_num=0

for i in list:
    name = total_xml[i]
    
    if i in trainval:  #train and val set
    # ftrainval.write(name)
        if i in train:
            # ftrain.write(name)
            # print("train")
            # print(name)
            # print("train: "+name+" "+str(train_num))
            directory = "train"
            train_num += 1
            train_dir_path = os.path.join(os.getcwd(), saveBasePath + '/{}'.format(directory))
            if(not os.path.exists(train_dir_path)) :
                os.mkdir(train_dir_path)
            filePath = os.path.join(xmlfilepath, name)
            newfile=os.path.join(saveBasePath, os.path.join(directory, name))
            shutil.copyfile(filePath, newfile)

        else:

            directory = "validation"
            validation_dir_path = os.path.join(os.getcwd(), saveBasePath + '/{}'.format(directory))
            if(not os.path.exists(validation_dir_path)):
                os.mkdir(validation_dir_path)
            val_num += 1
            filePath = os.path.join(xmlfilepath, name)
            newfile = os.path.join(saveBasePath, os.path.join(directory, name))
            shutil.copyfile(filePath, newfile)
            # print(name)
    else:  #test set
        # ftest.write(name)
        # print("test")
        # print("test: "+name+" "+str(test_num))
        directory = "test"
        test_dir_path = os.path.join(os.getcwd(), saveBasePath + '/{}'.format(directory))
        if(not os.path.exists(test_dir_path)):
            os.mkdir(test_dir_path)
        test_num+=1
        filePath=os.path.join(xmlfilepath, name)
        newfile=os.path.join(saveBasePath,os.path.join(directory, name))
        shutil.copyfile(filePath, newfile)
        # print(name)

# End time
end = time.time()
seconds=end-start
print("train total : "+str(train_num))
print("validation total : "+str(val_num))
print("test total : "+str(test_num))
total_num=train_num+val_num+test_num
print("total number : "+str(total_num))
print( "Time taken : {0} seconds".format(seconds))
