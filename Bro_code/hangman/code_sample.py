# Suppose this is foo.py.

print("before import")
import math

print("before function_a")
def function_a():
    print("Function A")

print("before function_b")
def function_b():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    function_a()
    function_b()
print("after __name__ guard")

# HOW IT WORKS

# When ever python interpreter reads source file it does two things - setting a few specials variables like __name__ and then executes all the code
# When youre running the source file(module) as the main program the interpre will assign the hard coded string "__main__" to the "__name__" variable
# - Its as if the interpreter inserts this at the top of your module when run as the main program
# __name__ = "__main__"
#  After special variables are set up, the interpreter executes all the code in the module one state at the time
# 1. it prints the string "before import"
# 2. Loads the math module and assigns it to a variable called math, this is equivalent to replacing import math with the following (n.b that the __import__ is a low level function in python that takes a string and triggers the actual import)
# - Finding and loading module given its string name "math", and assigning it to a local var called math
# 3. it prints the string be fore functions_a
# 4. Executes the def block creating a function object then assigning that function object to a var caled function_a
# 5. it prints the string "before function_b"
# 6. continues on to execue the second def block, creating another object, then ssigning it to a value called function_b
# 7. prints the string "before __name__ guard"

# ONly when your code is the main program
# 8. It will see that __name__ was indeed set to "__main__" and it calls two functions, printing the strings "functions A" and "Function B10.0"

# ONLY when your module is imported by another
# 8.(instead) if your module is not the main program but was imported by another one, then __name__ will be "foo", not "__main__", and itll skips the  body of the if statement

#ALWAYS
# 9. It will print the string "after __name__ guard" in both situations


# WHY
# Sometimes you want a .py file that can be both used by other programs and or modules as a module, and can also be run as the main program itself.
