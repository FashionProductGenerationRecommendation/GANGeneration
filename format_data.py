import os
import pandas as pd

from shutil import copyfile

path = "~/fashion-dataset/styles.csv"


dict_={}
style = pd.read_csv(path,usecols=['id','gender','masterCategory','baseColour','usage','productDisplayName']).dropna()
#  style.apply(lambda x:  dict_[x["id"]] = "{}".format(x["gender"]+" "+x["masterCategory"]+" "+x["baseColour"]+" "+x["gender"]+" "+x["usage"]+" "+x["productDisplayName"]),axis=1)
for i in range(0,len(style)):
    x = style.iloc[i]
    dict_[x["id"]] = x["gender"]+" "+x["masterCategory"]+" "+x["baseColour"]+" "+x["gender"]+" "+x["usage"]+" "+x["productDisplayName"]



# text_path = "/Users/Bharat/Desktop/Stony Brook/BigData/Project/Flower/text-to-image-master/untitled folder/text/"
text_path = 'text_c10/text/'
list_of = []
for i,(key,value) in enumerate(dict_.items()):
    if len(list_of)<=8000 and key not in list_of:
        list_of.append(key)
        file_name = "image_"+str(key)+".txt"
        file1 = open(text_path+file_name,"w")
        file1.write(value)
        file1.close() 






path = 'fashion-dataset/images/images/'
files = os.listdir(path)
# path1 = '/Users/Bharat/Desktop/Stony Brook/BigData/Project/Flower/text-to-image-master/untitled folder/data'
path1 = '102flowers'
for file in files:
    digit = int(file.split(".")[0])
    if int(digit) in list_of:
        # my_dest ="soul" + str(i) + ".jpg"
        # my_source =path + filename
        my_dest =path1 + '/image_'+file
        # rename() function will
        # rename all the files
        # os.rename(path+file, my_dest)
        copyfile(path+file, my_dest)




#8189