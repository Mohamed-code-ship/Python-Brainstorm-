my_list = [0,1,2,3,4,5,6,7,8,9]
#index =   0,1,2,3,4,5,6,7,8,9
#negative =-8,-7,-6,5,-4,-3,-2,-1

# + ve indexing is just the same as the numbers above 
# N/B : not all the time as the first index is always 0 

# We want to print the values from the last index to the first 

# list[start:end:step]

print (my_list[:-1])

# if we want to print the above even numbers including 0

print(my_list[0:-1:2])

# if we want to print the above even numbers excluding 0

print(my_list[2:-1:2])

# N/B stating point has to be the actual not compared to the ending point . 