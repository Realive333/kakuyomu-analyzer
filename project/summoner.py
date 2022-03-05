import decoder

import json
import sys
import os

def main():
    try:
        directory = sys.argv[1]
    except Exception as Argument:
        directory = ""
        
    data = decoder.fileEncoder(directory)
    summary = decoder.getSummary(data)
    
    with open(f'../abstract/{directory}/summary.json', 'w', encoding='utf-8') as f:
        json.dump(summary, f, ensure_ascii=False)
        
if __name__ == '__main__':
    main()