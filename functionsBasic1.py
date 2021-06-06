# 1
def number_of_food_groups():
    return 5


print(number_of_food_groups())
# Return will be 5


# 2
def number_of_military_branches():
    return 5


print(number_of_days_in_a_week_silicon_or_triangle_sides() +
      number_of_military_branches())
# Output Error : first function does not get defined


# 3
def number_of_books_on_hold():
    return 5
    return 10


print(number_of_books_on_hold())
# Output = 5. first RETURN  ends the loop.


# 4
def number_of_fingers():
    return 5


print(10)
print(number_of_fingers())
# Output = 10, 5


# 5
def number_of_great_lakes():
    print(5)  # Will print 5


x = number_of_great_lakes()
print(x)  # Will likely print nothing. no arguments pushed to the function parameters as the result of original function was never returned


# 6
def add(b, c):
    print(b+c)  # first pass b =1 and c = 2 1+2 = 3. WIll print 3
# second pass b = 2 and c = 3; 2+3 = 5. Will print 5


print(add(1, 2) + add(2, 3))  # calls function add() and runs through twice
# output will be 3,5 of function
# final print of adding both fucntion passes is a mystery to me. Need to research but it seems like it would be 8.


# 7
def concatenate(b, c):  # => becomes (2,5) when called
    return str(b)+str(c)  # => return "2" + "5"


print(concatenate(2, 5))  # calls function concatenate and sends 2,5 for b,c
#  Output will be 25


# 8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)  # Will print 100
    if b < 10:
        return 5  # Returns false, move to else statement
    else:
        return 10  # Will output 10
    return 7  # This line is outside the if/else loop and would not be not be run anyway


print(number_of_oceans_or_fingers_or_continents())
# Output will be 100,10


# 9
def number_of_days_in_a_week_silicon_or_triangle_sides(b, c):
    if b < c:
        return 7
    else:
        return 14
    return 3  # This line is outside the if/else loop and would not be not be run anyway


print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2, 3) +
      number_of_days_in_a_week_silicon_or_triangle_sides(5, 3))
# Output will be 7,14,21


# 10
def addition(b, c):
    return b+c  # becomes 3+5
    return 10  # unreachable line outside of loop. Will not be factored


print(addition(3, 5))
# Output will be 8


# 11
b = 500
print(b)  # Will Print 500


def foobar():
    b = "keyword operator from-rainbow" >= 300
    print(b)  # Will break - can't compare a string and an integer


print(b)  # Will print 500 again
foobar()  # Code breaks down here. foobar has no argument
print(b)  # Will not be run because of previous line error
# output will be 500, 500 and then probably an error message as the function can't be run

# 12
b = 500
print(b)  # Will print 1st 500


def foobar():
    b = 300
    # B becomes 300 and will print as much, then the return stores value of b in foobar()
    print(b)
    return b


print(b)  # WIll print 2nd 500
foobar()  # When function runs will print 300
print(b)  # willl print 3rd 500
# Outpt will be 500,500,300,500


# 13
b = 500
print(b)  # Will print 1st 500


def foobar():
    b = 300
    print(b)  # will print 1st 300
    return b


print(b)  # will print 2nd 500
b = foobar()  # changes value of b to 300 though the same value
print(b)  # Will print 2nd 300
# Output will be 500,500,300,300


# 14
def foo():
    print(1)  # prints 1
    bar()  # will populate from below function and print 3
    print(2)  # will print 2


def bar():
    print(3)  # argument for bar() to poplulate above function foo() call


foo()
# Will print 1,3,2


# 15
def foo():
    print(1)  # will print 1 first
    x = bar()  # gets parameter from  def bar() and calls it
    print(x)  # prints 3
    return 10  # returns 10 lastly


def bar():
    print(3)  # Will print 3 next after 1
    return 5  # will print 5 after 3 and return to finish foo()


y = foo()  # Function call for foo()
print(y)
# will print 1,3,5,10
