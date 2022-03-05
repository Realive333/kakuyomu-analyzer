import codecs

def read(path):
    with codecs.open(path, 'r', 'utf-8') as f:
        text = f.read()
    return text
        