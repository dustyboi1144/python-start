# for i in range(1,21,2):
#     print(i)
# for i in range (57,571,57):
#     print(i)
# for i in range(1,51):
#     if (i==15):
#         continue
#     if(i%3==0):
#         print(i)
a=int(input("enter a number:"))
b=int(input("enter another number:"))
for i in range (1,1001):
    if(i%a==0 and i%b==0):
        print(i)
        break
else:
    print("no number found")