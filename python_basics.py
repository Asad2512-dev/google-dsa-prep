# variables are dynamically typed in Python, meaning you don't need to declare their 
# type explicitly. The interpreter infers the type based on the value assigned to the variable.

n=0
print("n =" , n)

n ="abc"

print("n =" , n)

n,m = 1, "xyz"

n ,m ,z = 0.125 , "abc" , False

n= n+1  #good
n+=1    #good
# n++     #bad


n=4
n=None
print(n)




