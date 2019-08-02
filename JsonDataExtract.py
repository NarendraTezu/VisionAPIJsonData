#import requried library

import json
import re

jsonfilename = input("Enter your json file : ")
filedata = open(jsonfilename, "r")
filedata = json.load(filedata)

def extract_values(obj, key):
    #Pull all values of specified key from nested JSON.
    arr = []

    def extract(obj, arr, key):
        #Recursively search for values of key in JSON tree.
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results

z = extract_values(filedata, "description")
dict1 = {}
for i in z:
    string1 = str(i)
    newstr = string1.replace("\n"," ")

# Extract Value form json output and store in dict1
    list1 = [r"Gender: (\S+)", r"Age: (\S+)", r"Ref By: (\S+)"] #use regex for geting the useful data
    keylist = ["Gender","Age","Ref By"]
    i=0
    for item in list1:
        match = re.search(item, newstr)
        if match:
                dict1[keylist[i]] = match.group(1)
                i = i+1

#print(dict1)     # print store data in dict1

# write the requried json file with dict1 data with name result.json 

with open('result.json', 'w') as fp:
    json.dump(dict1, fp)
    print("*********JSON file genrated with name result.json********* ")

