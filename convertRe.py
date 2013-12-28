
def convPlain(rule):
    reExpr = ""
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
    return reExpr

prev_expr = ""
def convRuleToRe(rule):
    global prev_expr

    reExpr = ""
    rule = rule.strip()

    option = ""
    hide = ""

    if rule.startswith("~"):
        return None,None
    option_index = rule.find("$")
    if option_index != -1:
        option = rule[option_index:]
        rule = rule[:option_index]
        return None,None

    hide_index = rule.find("##")
    if hide_index != -1:
        hide = rule[hide_index+2:]
        rule = rule[:hide_index]

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

    parts = rule.split(",")
    if hide!="" and len(parts)>1:
        reExpr += "("
        reExpr += convPlain(parts[0])
        for p in parts[1:]:
            reExpr+="|"+convPlain(p)
        reExpr += ")"
    else:
        reExpr += convPlain(rule)

    if mend:
        reExpr += '$'

    if reExpr=='' :
        reExpr = prev_expr
    prev_expr = reExpr
    return (reExpr, hide)

def convertToRe():
    fi = open("nlist")
    fo = open("reList","w")
    for r in fi:
        if r.startswith('['):
            continue
        reExpr,hide = convRuleToRe(r)
        if reExpr is not None:
            fo.write(reExpr+"\t"+hide+"\n")
    fi.close()
    fo.close()
   
convertToRe()
