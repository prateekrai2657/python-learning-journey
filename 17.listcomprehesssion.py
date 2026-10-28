# List comprehension = A concise way to create lists in python 
# compact and easier to read than traditional loop
# way to  represent = [expression for value in iterables if condition]
doubles = [x *2 for x in range (1,11) ]
print(doubles)

numbers=[2,-4,8,3,-22,69]
positive_nums=[num for num in numbers if num>=0]
negative_nums=[num for num in numbers if num<=0]
print(positive_nums)
print(negative_nums)