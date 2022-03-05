import analyzer

import os
import json
from collections import Counter
    
def fileDecoder(directory):
    try:
        os.mkdir(f"../abstract/{directory}")
    except OSError as error:
        print(error)
    dic = []
    for root, directories, files in os.walk(f"../works/{directory}"):
        for file in files:
            if file == "abstract.html":
                path = os.path.join(root, file)
                anyz = analyzer.Analyzer(path)
                data = {
                    "id": anyz.wid,
                    "genre": anyz.genre,
                    "label": anyz.label,
                    "stars": anyz.stars
                }
                dic.append(data)
    with open(f'../abstract/{directory}/abstract.json', 'w', encoding='utf-8') as f:
        json.dump(dic, f, ensure_ascii=False)
                    
def fileEncoder(directory):
    for root, directories, files in os.walk(f"../abstract/{directory}"):
        for file in files:
            if file == "abstract.json":
                path = os.path.join(root, file)
                with open(f'../abstract/{directory}/abstract.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
    return data
    
def getSummary(data):
    records = []    
    for file in data:
        flag = False
        genre = file.get('genre')
        labels = file.get('label')
        labelDict = {}
        for label in labels:
            labelDict[label] = 1
        for record in records:
            r_genre = record.get('genre')
            r_labels = record.get('label')
            if genre == r_genre:
                d1 = Counter(r_labels)
                d2 = Counter(labelDict)
                record['label'] = dict(d1+d2)
                flag = True
        if flag == False:
            records.append({'genre':genre, 'label':labelDict})
    return records