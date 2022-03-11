import analyzer

import os
import json
import logging
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
        print(f'collect abstract from {file.get("id")}')
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
                d3 = dict(d1+d2)
                d3 = dict(sorted(d3.items(), key=lambda item:item[1], reverse=True))
                record['label'] = d3
                record['count'] += 1
                flag = True
        if flag == False:
            records.append({'genre':genre, 'count':1, 'label':labelDict})
        
    return records