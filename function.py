def hello():  #function defination 
    print("hello")
    print("from python")

hello()  #function call 
hello()

# function  defination 
def sum(a, b):
    s = a+b
    return s

#function call
ans = sum(3, 4)
print(ans)                                                 


#Question 1: function take 3 number input and return average value
def calc_avg(a, b, c):
    sum = a+b+c
    return sum/3
 
print(calc_avg(2,2,2))                                

# default value 
def sum(a, b=1):
    return a+b

print(sum(5))

#Lambda fumction 

avg = lambda a,b: (a+b)/2
print(avg(4, 5))

#Question 2  write a function to printy factorial of 'n'.

def calc_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *=i

        return fact
    
n = int(input("enter n: "))
print(calc_factorial(n))