marks = [99, 89, 100, 65, 92, "abc"]
print(marks)
marks[2] = 70  # because of this reason this is mutable

print(marks)
print(marks[4])  #in list they follow indexing index follow hoti hai
print(len(marks))
print(type(marks)) 

#slicing

print(marks[0:5])
print(marks[:len(marks)])
print(marks[5:])


# These method only use in the list 
nums = [1,2,3]

# append
nums.append(4)
print(nums)

# insert
nums.insert(2,10)
print(nums)

#sort
nums.sort()  
nums.sort(reverse = True)  #for decreasing 
print(nums)

# reverse
nums.reverse()
print(nums)


# LOOP'S
nums = [1, 2, 3, 10, 4]

for val in nums:
    print(val)

# Example : Find the index position '

nums = [1, 2, 3, 10, 4]

x=10
idx = 0

for val in nums:
    if(val == x):
        print(f"x found at idx ={idx}")
        break
    idx += 1