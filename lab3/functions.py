#EX1
def my_function():
    print("Hello from a fucntion")
    
#EX2
def my_function():
    print("Hello from a fucntion")
my_function()

#EX3
def my_function(fname, lname):
  print(fname)
my_function("Oleg", "Mongol")
#EX4
def my_function(x):
    return x + 5
print(my_function(5))

#EX5
def my_function(*kids):
    print("The youngest child is" + " " + kids[2])
my_function("Vanya", "Sasha", "Vasya")

#EX6
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Thomas", lname = "Shelby")

