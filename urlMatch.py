
import re

raw = []    
def readReRule(fname):
    f = open(fname)
    reRules = []
    try:
        for line in f:
            raw.append(line.strip())
            reRules.append(re.compile(line.strip()))
    except:
        print line 

    return reRules

def matchUrl(url, rules):
    for rule,rawRe in zip(rules, raw):
        if rule.search(url) is not None:
            print rawRe        
            return True                            
    return False
    
if __name__=="__main__":
    rules = readReRule("reList")
    while True:
        url = raw_input()
        print matchUrl(url.strip(), rules)
        
