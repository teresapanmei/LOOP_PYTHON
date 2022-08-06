# num=input("enter any alpha")
# i=0
# a=[]
# b=[]
# while i<len(num):
#     if num[i]=="a":
#         a.append(num[i])
#     elif num[i]=="e":
#         a.append(num[i])
#     elif num[i]=="i":
#         a.append(num[i])
#     elif num[i]=="o":
#         a.append(num[i])
#     elif num[i]=="u":
#         a.append(num[i])
#     else:
#         b.append(num[i])
#     i+=1
# print("vowel=",a)
# print("consonant=",b)



num=input("enter any alpha:")
i=0
a=[]
b=[]
while i<len(num):
    # if num[i]=="a" or num[i]=="e" or num[i]=="i" or num[i]=="o" or num[i]=="u":
    if num[i] in ("a""e""i""o""u"):
        a.append(num[i])
    else:
        b.append(num[i])
    i+=1
print(a)
print(b)

# num=input("enter any alpha:")
# i=0
# a=[]
# b=[]
# while i<len(num):
#     # if num[i]=="a" or num[i]=="e" or num[i]=="i" or num[i]=="o" or num[i]=="u":
#     if num[i] in ("a""e""i""o""u"):
#         a.append(num[i])
#     else:
#         b.append(num[i])
#     i+=1
# print(a)
# print(b)