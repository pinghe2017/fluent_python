# function is instance of clss function
# The __doc__ attribute is used to generate 
# the help text of an object
# the command help(factorial) will display a screen
def factorial(n):
  '''returns n`!'''
  return 1 if n < 2 else n*factorial(n-1)

# The map function returns an iterable
# where each item is the the result of the
# application of the first argument (a function) 
# to succesive elements of the second argument(an iterable)
a = map(factorial, range(11))
print(list(a))

# high order function : 
# A function that takes a function as argument or returns a function as result
fruits = ['banana','apple']
def reverse(word):
  return word[::-1]
sorted(fruits, key = reverse)

# list comprehension
fact = factorial

list(map(fact, range(6)))
b = [fact(n) for n in range(6)]

# lambda arguments : expression
# equal: X(arguments) : return(expression)
# the power of lamda use them as anomymous function inside another function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)



c = list(map(factorial, filter(lambda n: n % 2, range(6))))
d = [factorial(n) for n in range(6) if n % 2]


