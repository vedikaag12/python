inp=input("Write the statement: ")
counta=0
counte=0
counti=0
counto=0
countu=0
a=[]
b=[]

for i in inp :
    if(i=='a'):
        a.append('a')
        counta=counta+1
    elif(i=='e'):
        a.append('e')
        counte=counte+1
    elif(i=='i'):
        a.append('i')
        counti=counti+1
    elif(i=='o'):
        a.append('o')
        counto=counto+1
    elif(i=='u'):
        a.append('u')
        countu=countu+1
    elif(i=='A'):
        a.append('a')
        counta=counta+1
    elif(i=='E'):
        a.append('e')
        counte=counte+1
    elif(i=='I'):
        a.append('i')
        counti=counti+1
    elif(i=='O'):
        a.append('o')
        counto=counto+1
    elif(i=='U'):
        a.append('u')
        countu=countu+1

cnt={"a":counta,"e":counte,"i":counti,"o":counto,"u":countu}
A=set(a)
print("TOTAL VOWEL FOUND:",A)
print("TOTAL OCCURANCE OF EACH VOWEL:",cnt)
