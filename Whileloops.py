# while loop

# 1. finite loop which should print any value 5 time
count = 1   # Iterator means grneraly when we talk about iterator it mean we talk about the loop 
while (count <= 5):
    print("hello world", count)
    count += 1

print("after loop , count =", count)#6

#2. print number from 1 to 5
i=1
while(i<=5):
    print(i)
    i += 1

#3. print in reverse
count = 5
while(count>=1):
    print(count)
    count -= 1

#4. print multiplication table of any number 'n'.
num = int(input("enter the number: "))
i = 0
while(i<10):
    print(num*(i+1))
    i += 1