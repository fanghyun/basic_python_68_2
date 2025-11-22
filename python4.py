"""
#
# Part : Conditional Statements
#
"""
x = 10
y = 20
if x < y : #if เช็คถ้าจริงจะหยุด ถ้าไม่เข้าเงื่อนไข จะไปเลื่อนไขต่อไปเรื่อยๆ
    print("x is less than y")
    print(1)
elif x > y:
    print("x is greater than y")
    print(2)
elif x == y:
    print("x is equal to y")
    print(3)
else:
    print("error")
    print(4)