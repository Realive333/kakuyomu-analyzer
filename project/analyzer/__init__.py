from filereader import html
from lxml import etree
from io import StringIO

class Analyzer:
    def __init__(self, path):
        self.path = path
        self.html = html.read(path)
        self.getStatus()
    
    def getPath(self):
        return self.path
        
    def getText(self):
        return self.html
    
    def getStatus(self):
        root = etree.HTML(self.html)
        self.genre = root.xpath("//li[@id='workGenre']/a/text()")[0]
        self.label = root.xpath("//li[@itemprop='keywords']/a/text()")
        self.stars = root.xpath("//p[@id='workPoints']/a/span/text()")[0]
        self.wid = root.xpath("//h1[@id='workTitle']/a/@href")[0].split("/")[-1]

   