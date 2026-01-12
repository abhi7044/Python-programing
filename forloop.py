string = "hello"

#in => membership operator

for var in string:
    print(var)

# in : this in help to check the presence of a paticular value
# { String = "hellp/hello"
# if 'o' in String:
#     print("o exists in string")
# else:
#     print("does not exist")  } 

for i in range(5):
    print(i)

for i in range(5):
    print("hello world")

word = "artificial intelligence"
#count the number of i's
ans = 0
for ch in word:
    if(ch == 'i'):
        ans+=1

print ("ans of i = ", ans)


# Q1. Print sum of first 'n' natural numbers.
n = int(input("enter the number"))
sum =0
for i in range(1, n+1):
    sum += i
    print(sum)