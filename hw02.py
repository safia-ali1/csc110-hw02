# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    '''
    line 9 is storing a
    line 11 is storing b
    line 13 is returning a and b back to the function
    '''
    a = int(input( "give me x: "))
    #storing A
    b = int(input("give me y: "))
    #storing B
    return a,b
    #returning a and b back to the function




#calling the function

   # # ADD a Docstring for this function
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
 


# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
   '''
lines 38+39 store a*b into mult_result and then print it
lines 41+42 store a+b into add_result and then print it
line 44 is then storing and returning mult_result/add_result to the function
   '''
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
   mult_result=(a*b)
   print( "mult result:",mult_result,)
    #storing a*b into mult_result and then printing it
   add_result=(a+b)
   print( "add result:",add_result,)
    #storing a+b into add_result and then printing it
   return mult_result/add_result
    #returning mult_result/add_result back to the function



    
    

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    # ADD a Docstring for this function
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    ''' these lines print a variety of statements and symbols
    '''
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================")


def main ():
    '''
    line 74 is calling the function read_two_ints and storing the output into the variables x and y
    line 75 is calling the function compute_multadd that has arguements, x and y and storing the output into xy_multadd
    line 76 is calling the function print_fancy that has arguements x and y and xy_multadd
    '''
    x,y=read_two_ints() 
    xy_multadd=compute_multadd(x,y)
    print_fancy(x,y,xy_multadd)


    # ADD a Docstring for this function
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    # TODO: add your call instead of this line

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    # TODO: add your call instead of this line

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    # TODO: add your call instead of this line


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
