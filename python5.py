"""
#
# Part : Loop
# Section: while Loop
#
"""
i = 1
while i <= 5:
    print("Hello Python", i)
    if i == 3:
        break
    i += 1

"""
#
# Part : Loop
# Section: For Loop
#
"""
this_list = ["apple", "banana", "cherry"]
for x in this_list:
    print(x)
    if x == "banana":
        break