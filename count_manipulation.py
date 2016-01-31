# Functions to manipulate global variable count

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.


    
###################################################
count = 0
def reset():
    global count
    count = 0
    return count
def increment():
    global count
    count += 1
    return count
def decrement():
    global count
    count -= 1
def print_count():
    print count

reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2
