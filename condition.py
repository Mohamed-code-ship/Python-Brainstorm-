# The while, if and else statements are used for looping and conditional code execution 

# Here is an example :

a = 2
b = 3 

if a > b :
    print("Computer says yes ")
else : 
    print("Computer says no ")

# If you want to pass no value you use the Pass key word .Here is an example : 


if a < b :
    pass  # Do nothing 
else : 
    print('Computer says no !')

    # using elif for multiple test case : 

if suffix == '.htm':
    content = 'text/html'
elif suffix == '.jpg':
    content = 'image/jpeg'
elif suffix == '.png':
    content = 'image/png'
else:
    raise RuntimeError(f'Unknown content type {suffix!r}')
