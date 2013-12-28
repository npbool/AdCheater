import urllib
import re

redirRules = []
hideRules = []
def readReRule(fname):
    f = open(fname)

    for line in f:

        expr,hide = line.split('\t')
        hide = hide.strip()
        expr = expr.strip()

        if hide!="":
            hideRules.append((re.compile(expr), hide, expr))
        else:
            redirRules.append((re.compile(expr), expr))

    return (redirRules, hideRules)

def matchRedir(url):
    for rule in redirRules:
        if rule.search(url) is not None:
            return True
    return False;

def matchHide(url):
    for rule in hideRules:
        if rule.search(url) is not None:
            return True
    return False

htmlRe = re.compile(r'(/|\.html|\.htm|\.jsp|\.php|\.asp|/[^./]*)$')
image_suffix = ['jpg','jpeg','png','gif','bmp',]
def getProperImage(url, imageType):
    return "http://59.66.131.124/ad."+imageType

def urlRewrite(url):
    data = {}

    #redirect
    for rr,expr in redirRules:
        if rr.search(url) is not None:
            print "MATCH:"+expr
            for imageType in image_suffix:
                print url, imageType
                if url.endswith(imageType):
                    return getProperImage(url,imageType)

            #not image
            return "127.0.0.1:12345"

    #replace ele
    subs = ','.join([hr[1] for hr in hideRules if hr[0].search(url) is not None])

    if subs != '' or htmlRe.search(url) is not None:
        print "SUB"
        data['url'] = url
        data['subs'] = subs
        return urllib.urlencode(data)
    return url

if __name__=="__main__":
    #url = 'http://img1.126.net/channel7/cover.gif'
    #for imageType in image_suffix:
    #    if url.endswith(imageType):
    #        print imageType

    readReRule("reList")
    while True:
        print "HE"
        url = raw_input().strip()
        print urlRewrite(url)
