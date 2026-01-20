# FORMAT
a= 5
b = 10
#sum = a+b

#nowmal formatting
print("language is {}".format("python"))
print("sum is {}".format(sum))
print("sum of {} & {} is {}".format(a,b,sum))

#index based formatting 
print("sum of {1} & {0} is {2}".format(a,b,sum))

#value based formatting ==> create variable inside the formating itself --------if reuse the variable to format 
print("values of vars {a} & {b}".format(a=5, b=10))
print("{a}values of vars {a} & {b}".format(a=5, b=10))

# F STRING  ===> in this we only make variable of a and b not sum '
print(f"sum of {a} & {b} is {a+b}")
print(f"avg of {a} & {b} is {(a+b)/2}")