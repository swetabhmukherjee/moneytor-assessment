# function to implement exponent

def exponent(base,exp):
    if((base>=1) and (exp<=10)):
        if(exp==1):
            return(base)
        if(exp!=1):
            return(base*exponent(base,exp-1))
    else:
        return "out of bounds"

# driver function

a = exponent(5,11)
print(a)
