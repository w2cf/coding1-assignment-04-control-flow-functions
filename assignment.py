def add_one(value):
    return value + 1

for number in [1, 2, 3]:
    if number > 1:
        print(add_one(number))

# 1. What is printed, in order? Explain how the loop and the if condition
# decide which numbers are passed to add_one.
# Your answer: the code prints every number that is bigger than 1, which in 
#this case are 2 and 3. Since they are passed to an add_one function, they turn into 
#3 and 4

# 2. What does add_one(2) return? Explain the difference between return
# inside the function and print in the loop.
# Your answer: add one(2) returns 3
# the loop on the other side does not return anything, it only shows the result
#so if they were to get used later in a code it would show nothing, as nothing
#was returned from executing the loop 
