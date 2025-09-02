# a =33
# b = 33
# if b > a:
#     print("greater")

tasks = ['eat', 'task2', 'task3', 'task4', 'task5']
print(f"Before edit: {tasks}")
print('OIndex: ', tasks.index('eat'))

tasks.insert(tasks.index('eat'), 'shop')
print(f"After edit{ tasks}")