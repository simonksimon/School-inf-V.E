import os
def files(directory, level=0):
    for item in os.listdir(directory):
        if os.path.isdir(directory+"\\"+item) and item[0] not in ".$":
            if len(os.listdir(directory+"\\"+item))!=0: #vrati aj subory ktore su v danom adresari treba len adresare nie subory
                print("-",' '*level,item)
                files(directory+"\\"+item,level+1)
files(r"C:\Program Files")