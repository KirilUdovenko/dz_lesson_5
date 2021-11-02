# persons = [{"name": "John", "age": 15},
#            {"name": "Kiril", "age": 25},
#            {"name": "Jackson", "age": 15},
#            {"name": "Jack", "age": 45},
#            {"name": "Gabriel", "age": 37}]
#
# ages = []
# names_lens = []
#
# for person_dict in persons:
#     ages.append(person_dict["age"])
#     names_lens.append(len(person_dict["name"]))
#
# print(ages, names_lens)
#
# min_age = min(ages)
# max_len_name = max(names_lens)
#
# for person_dict in persons:
#     if person_dict["age"] == min_age:
#         print(person_dict["name"])
#
# for person_dict in persons:
#     if len(person_dict["name"]) == max_len_name:
#         print(person_dict["name"])
#
# mean_age = sum(ages) / len(ages)
#
# print(mean_age)

#################

# my_dict_1 = {1: 1, 2: 2}
# my_dict_2 = {11: 11, 2: 22}
#
# result_1 = list(set(my_dict_1.keys()).intersection(set(my_dict_2.keys())))
# print(result_1)
#
# result_2 = list(set(my_dict_1.keys()).difference(set(my_dict_2.keys())))
# print(result_2)
#
# result_3 = {key: my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}
# print(result_3)
#
# result_4 = my_dict_1.copy()
# for key in my_dict_2:
#     if key in result_4:
#         result_4[key] = [result_4[key], my_dict_2[key]]
#     else:
#         result_4[key] = my_dict_2[key]
# print(result_4)

##############

# def change_list(my_list):
#     for index in range(0, len(my_list), 2):
#         my_list[index] = my_list[index][::-1]
#     return my_list
#
# my_list = ["qwe", "jer", "zxc", "957", "bet"]
# my_list = change_list(my_list)
# print(my_list)

############

# from random import randint, choice
# from string import ascii_lowercase as alphabet
#
# def create_email(domains, names):
#     name = choice(names)
#     domain = choice(domains)
#     number = randint(100, 999)
#     my_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
#     e_mail = f"{name}.{number}@sgdyyur.{domain}"
#     return e_mail
#
#
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
