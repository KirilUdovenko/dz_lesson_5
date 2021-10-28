my_list = [
    {"name": "John", "age": 15},
    {"name": "Joshua", "age": 18},
    {"name": "Jack", "age": 45}
]
result = []
for item in my_list:
    result.append(item["age"])
min_age = min(result)
print(result)
print(min_age)
