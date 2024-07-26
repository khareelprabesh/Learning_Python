marks = {
    "Anita": 100,
    "Mausham": 75,
    "Ankit" : 54,
    0 : "Prabesh"
    }
print (marks.items())
print (marks.keys())
print (marks.values())
marks.update ({"Anita": 99, "Nishant": 100})
print (marks)
# # print (marks.get("Anita2")) # Prints none!
# # print (marks["Anita2"]) # Returns an error! 
Mausham = marks.pop("Mausham")
print (Mausham) # Prints only the marks of Mausham
print (marks) # Prints all of them except the Mausham
item = marks.popitem()
print (item)
print (marks)
