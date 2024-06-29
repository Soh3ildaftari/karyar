import pprint
import os
file1=['apple','pitch','banana']
file2=['car','apple','house','and']
file3=['car','banana','leave']
# read file from path line by line
# separate strings to words
dirpath="data/"
files=os.listdir(dirpath)
file_data={}
for file in files:
    path=os.path.join(dirpath,file) 
    with open(path,'r') as file:
        data = file.read()
        data=data.split()
        file_data[file.name]=data
# pprint.pprint(file_data)
stopWords=['a','of','on','i','with','the','at','from']
def language(file):
    filtered_file = [word.lower() for word in file if word.lower() not in stopWords]
    return filtered_file
def inverted_indexes(file_data):
    inverted_index = {}
    for filename,file in file_data.items():
        processed_words = language(file)
        for word in processed_words:
            if word not in inverted_index:
                inverted_index[word] = []
            if filename not in inverted_index[word]:
                inverted_index[word].append(filename)
    return inverted_index
def query():
    query=input("search:")
    query=f"*{query}*"
    files=inverted_index[query]
    
    for file in files:
        print(f"{query}: {file}")
inverted_index=inverted_indexes(file_data)
query()

