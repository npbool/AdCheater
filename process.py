import sys
fi = open("list")
fo = open("nlist","w")

for line in fi:
    if len(line) < 3:
        continue
    
    if line[0] == '!' || line[0] == '[':
        continue
    if "#@#" in line:
        continue
    if line.startswith("@@"):
        continue
    fo.write(line.strip() + "\n")
    
fi.close()
fo.close()
