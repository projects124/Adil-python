myDict={
  "Fast":"In a quick manner",
  "Adil": "A coder ",
  "Marks":[1,2,5],
  "Anotherdict": {'Adil':'player'},
   1:2
}
#Dictionary Methods
print(list (myDict.keys()))
print((myDict.values()))
print( myDict.items())
print(myDict)
updateDict={
   "Lovish":"Friend",
    "Adil" :"Friend",   
    "Ahmed" :"A dancer"
}
myDict.update(updateDict)
print(myDict)

print(myDict.get("Adil"))
print(myDict["Adil"])
print(myDict.get("Adil"))
print(myDict["Adil"])

