new_set = {"apple", "banana", "cherry","apple"}
new_set.add("papaya")
print(new_set) #same value not show again and again and unorder printing
#update method
new_set.update(new_set)
print(new_set)
#remove items
new_set.remove("cherry")
print(new_set)
new_set.discard("apple")
print(new_set)
#pop for random 
new_set.pop()
print(new_set)
#clear all set
new_set.clear()
print(new_set)
#intersection method 
x={"apple", "banana"}
y={"banana", "cherry"}
z= x.intersection(y)
print(z)
#keep all, but not duplicates
f=x.intersection_difference(y)
print(f)