# i=1
# while i<=10:
#     if i==7 or i==8 or i==9:
#         print("*")
#     else:
#         print(i)
#     i=i+1
        
i=1
while i<=20:
    if i%3==0 and i%5==0:
        print("navgurukul")
    elif i%3==0:
        print("nav")
    elif i%5==0:
        print("gurukul")
    else:
        print(i)
    i+=1