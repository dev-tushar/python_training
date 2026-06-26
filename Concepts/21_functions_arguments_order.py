"""
We can combine all type of arguments in one function
but
we need to follow the order
"""

"""
How to decide 
which is keyword argument and which is positional argument

1. Before the * argument, all arguments are treated as positional argument so we can pass only values
2. After the * argument, all arguments are treated as keyword argument so we need to specify argument name and value
ALSO
1. Before the *var_argument, all arguments are treated as positional argument so we can pass only values
2. After the *var_argument, all arguments are treated as keyword argument so we need to specify argument name and value
"""

"""
Variable keyword argument ie. **var_key_argument will be the last ARGUMENT
"""

"""

**********JUST REMEMBER THIS********
SUMMARY of the order

1st put all POSITIONAL argument IF ANY
then
put VARIABLE POSITIONAL argument IF ANY
then
put all KEYWORD argument IF ANY
then
put all VARIABLE KEYWORD argument IF ANY
    
Example--> func(a,*a,a=val,**a)
"""