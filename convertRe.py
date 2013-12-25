
def convRuleToRe(rule):
    reExpr = ""
    rule = rule.strip()
    if("##" in rule):
        return None
    if("$" in rule):
        return None
    if(rule.startswith("||")):
        rule = rule[2:]
        reExpr = r'^(http://|http://www\.)'
        
    elif rule.startswith("|"):
        rule = rule[1:]
        reExpr = r'^'
    
    mend = False
    if rule.endswith('|'):
        rule = rule[:-1]
        mend = True
            
    for c in rule:
        if c=='^':
            reExpr += r"([/:?=&]|//)"     
        elif c=='*':
            reExpr += r".*"
        elif c=='.':
            reExpr += r'\.'
        elif c=='?':
            reExpr += r'\?'
        elif c=='+':
            reExpr += r'\+'
        elif c=='[':
            reExpr += r'\['
        elif c=='|':
            reExpr += r'\|'
        else:
            reExpr += c
    
    if mend:
        reExpr += '$'
    return reExpr

def convertToRe():
    fi = open("nlist")
    fo = open("reList","w")
    for r in fi:
        if r.startswith('['):
            continue
        reRule = convRuleToRe(r)
        if reRule is not None:
            fo.write(reRule+"\n")
    fi.close()
    fo.close()
   
convertToRe()
