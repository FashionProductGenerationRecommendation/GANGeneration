import pandas as pd
path = "/Users/Bharat/Desktop/Stony Brook/BigData/Project/Flower/text-to-image-master/untitled folder/fashion-dataset/styles.csv"


dict_={}
style = pd.read_csv(path,usecols=['id','gender','masterCategory','baseColour','usage','productDisplayName']).dropna()
#  style.apply(lambda x:  dict_[x["id"]] = "{}".format(x["gender"]+" "+x["masterCategory"]+" "+x["baseColour"]+" "+x["gender"]+" "+x["usage"]+" "+x["productDisplayName"]),axis=1)
for i in range(0,len(style)):
    x = style.iloc[i]
    dict_[x["id"]] = x["gender"]+" "+x["masterCategory"]+" "+x["baseColour"]+" "+x["gender"]+" "+x["usage"]+" "+x["productDisplayName"]



text_path = "/Users/Bharat/Desktop/Stony Brook/BigData/Project/Flower/text-to-image-master/untitled folder/text/"

for i,(key,value) in enumerate(dict_.items()):
    file_name = "image_"+str(key)+".txt"
    file1 = open(text_path+file_name,"w")
    file1.write(value)
    file1.close() 
