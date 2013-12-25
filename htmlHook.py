import urllib
import urllib2
from bs4 import BeautifulSoup
def hook(url):
    html = urllib2.urlopen(url).read()
    soup = BeautifulSoup(html)
    soup.select("body")[0].clear()
    f = open("index.html","w")
        
    f.write(unicode(soup).encode('utf-8'))
    f.close()
hook("http://www.163.com")
