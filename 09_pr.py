myDict={
       "Pankha":"Fan",
       "Dabba" :"Box",
       "Vastu" :"Item",
       "Unconventional":"not based on or conforming to what is generally done or believed.",
       "python": "a Poisonous snake"
}
print("Option are",myDict.keys())
a=input("Enter the urdu and hindi World/n:")
#print("The meaning of your Words is:",myDict[a])
print("The meaning of your Words is:",myDict.get(a))