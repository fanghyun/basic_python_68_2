"""
#
# Part : Functions
#
"""
def myFullName(firstName, lastName):
    fullName = firstName + "" + lastName
    return fullName

print(myFullName("Loid", "Forger"))
print(myFullName("Yor", "Forger"))
print(myFullName("Anya", "Forger"))
print(myFullName("Bond", "Forger"))

def redPotion(hp):
    hp += 50
    return hp

currentHp = 100
print("Current HP:", currentHp)
currentHp = redPotion(currentHp)
print("After ussing Red Potion, HP:", currentHp )