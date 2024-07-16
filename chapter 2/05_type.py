a = 100
type (a) # class <int>
print (type(a))

b = 199.99
type (b) # class <float>
print (type(b))

c = "prabesh"
type (c) # class <str>
print (type(c))

a = "100.99"
b = float (a) # a type should be in float
type (b) # class <float>
print (type(b))

a = 100.99
b = str (a) # a type should be in string
type (b) # class <str>
print (type(b))
