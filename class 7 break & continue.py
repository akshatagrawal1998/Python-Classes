# Break Statement
# e.g - used in Linear Search - when we are searching for a item in a list of 1 lac numbers, 
#we want to terminate the loop 
# as soon as we find our number - terminate the loop - saves runtime

for i in range(1,100000):
    if i == 51:
        break  # terminate
    print(i)




# Continue Statement : 

for i in range(1,11):
    if i == 5:
        continue  # skip when value of i  is 5 - just one iteration
    print(i)