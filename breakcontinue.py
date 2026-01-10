#break

i=1
while(i<= 10):
    if(i%6 == 0):
        break
    print(i)
    i+=1
print("putside loop now...")

#continue
i=1
while(i<= 20):
    if(i%3 == 0):
        i+=1
        continue
    print(i)
    i+=1
print("outside loop now...")

#print all the odd nums from 1 to 10
i=0
while(i<=10):
    i+=1
    if(i%2 ==0):
        
        continue
    print(i)
    