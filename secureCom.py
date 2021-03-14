print("\n\n\n\n\n")
print("HELLO MIT CELL")
k=int(input("Please enter k value to shift transform message: "))
if k<1 and k>20:
    print("enter the number b/w 1-20 only")
inp=input("Please enter your message : ")
letter = 0
ins=""

print("You send :")
for i in inp:
    if ord(i)>=97 and ord(i)<=122:                         #if all Lower char
        if ord(i)==122:                     #code for z
            letter = chr(90+(k-1))
        else:
            letter= chr(ord(i)+k)
    elif ord(i)>=65 and ord(i)<=90:                       #if all Upper char
        if ord(i)==90:                      #code for Z
            letter = chr(65+(k-1))
        else:
            letter= chr(ord(i)+k)
    elif i.isalnum():                       #if all num
        if int(i)>=0 and int(i)<9:
            letter = int(i)+k
        else:
            letter = 0+(k-1)
    elif i==" ":
        letter = "@"                        #for space
    elif i==".":
        letter = "#"                        #for .
    else:
        letter = i                          #for rest of symbols
    print(letter, end="")
    
    ins+=str(letter)                        #store the trasformed msg
print("\nvalue of k is :",k)

print()
print()
print()


print("HELLO INSTRUCTOR:")
print(f"YOU GOT A MESSAGE {ins}")
p=int(input("To read this in original please type k value provided by Cell: "))
print("ORIGIGNAL MESSAGE")
for i in ins:
    if ord(i)>=97 and ord(i)<=122:                         #if all Lower char
        if ord(i)==97:                     #code for z
            letter1 = chr(122-(p-1))
        else:
            letter1= chr(ord(i)-p)
    elif ord(i)>=65 and ord(i)<=90:                       #if all Upper char
        if ord(i)==65:                      #code for Z
            letter1 = chr(65-(p-1))
        else:
            letter1= chr(ord(i)-p)
    elif i.isalnum():                       #if all num
        if int(i)>=1 and int(i)<=9:
            letter1 = int(i)-p
        else:
            letter1 = 9-(p-1)
    elif i=="@":
        letter1 = " "                        #for space
    elif i=="#":
        letter1 = "."                        #for .
    else:
        letter1 = i                          #for rest of symbols
    print(letter1, end="")
