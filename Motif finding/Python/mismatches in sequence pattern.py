pattern=input("Pattern=")
text=input("Text=")
d=input("d=")

def hd(str1,str2):
    i=0
    count=0
    while(i<len(str1)):
        if(str1[i]!=str2[i]):
            count +=1
        i +=1
    return count

def apm(pattern,text,d):
    positions=[]
    for i in range (len(text)-len(pattern)+1):
        if hd(pattern,text[i:i+len(pattern)])<=int(d):
            positions.append(i)
    return positions

print(*apm(pattern,text,d))