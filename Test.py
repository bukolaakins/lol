#print (1 + 2) #check if they are all numbers

a = 'rice and beans'
b = "egg"
c = "{}"
d = "but do not have the money"

print("I want to eat", a, "but I do not have the money.")
print("I want to {}.".format(a))
print(c.format("I want beans"))

from sys import argv
ScriptName, first, second, third, fourth, fifth, sixth = argv

print("What is your fourth variable?")
fourth = input()
print("What is your fifth variable?")
fifth = input()
print("What is your sixth variable?")
sixth = input()

print("The script is called: ", ScriptName)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
print("Your third variable is: ", third)
print("Your fourth variable is: ", fourth)
print("Your fifth variable is: ", fifth)
print("Your sixth variable is: ", sixth)
