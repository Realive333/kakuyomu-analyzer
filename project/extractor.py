import filereader.html as html
import decoder

import sys
import os

def main():
    try:
        directory = sys.argv[1]
    except Exception as Argument:
        directory = ""
        
    try:
        os.mkdir("../abstract")
    except OSError as error:
        print(error)
        
    decoder.fileDecoder(directory)
    
if __name__ == '__main__':
    main()