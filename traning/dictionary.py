thisdict = {
    "brand" : "ford",
    "electric": "wire",
    "cost ": "2344",
    "model":  "purana"
}
x = thisdict["model"]
print(x)
if "model" in thisdict:
    print("yes, 'model' is present ")
    thisdict.update({"cost" : 3455})
    print(thisdict)

# same method pop, remove, popitems, del , clear
#copy dictionary
#dict2 = dict1
