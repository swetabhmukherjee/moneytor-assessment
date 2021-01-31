# function to implement exponent

def exponent(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*exponent(base,exp-1))

# driver function

a = exponent(5,3)
print(a)
