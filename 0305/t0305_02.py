stu = {"학번":1,"이름":"홍길동","학과":"컴퓨터공학과"}

print(stu.keys())
print(type(stu.keys()))

stu_list = list(stu.keys())
print(stu_list)

print(stu.values())
print(type(stu.values()))

for key in stu.keys():
    print(stu[key])