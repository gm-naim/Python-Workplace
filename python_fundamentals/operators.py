#########  Identity Operators


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z) # returns True because z is the same object as x

print(x is y) # returns False because x is not the same object as y, even if they have the same content

print(x == y)  

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y


### Assignment Operators

# Right Shift (>>=)

x = 16
x >>= 2
print(x)

# Left shift(<<=)

x = 5
x <<= 2
print(x)


##  Membership Operators

text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)



####              Bitwise Operators

a = 5

print(~a)     #rule for int. -a=-(a+1)