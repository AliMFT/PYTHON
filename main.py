#Q1
# name = ["Tarteel", "Asmaa", "Ahmed"]

# #_1_
# name.insert(0, "Sabrin")
# print(name)

##_2_
# name.pop()
# print(name)

##_3_
# name.append("Hamda")
# print(name)

##_4_
# del name[2]
# print(name)


#Q2
# friends = ["Adel", "Ahmed"]
# employees = ["Samah", "Amjad"]
# school = ["Ali", "Basma"]
#
# joined_list = []
# joined_list.extend(friends)
# joined_list.extend(employees)
# joined_list.extend(school)
#
# print(joined_list)


#Q3
# dict1 = {1: 10, 2: 20}
# dict2 = {3: 30, 4: 40}
# dict3 = {5: 50, 6: 60}
#
# # Concatenate dictionaries
# concatenated_dict = {}
# for dict in (dict1, dict2, dict3):
#     concatenated_dict.update(dict)
#
# print(concatenated_dict)


#Q4
# squared_dict = {}
#
# for num in range(1, 16):
#     squared_dict[num] = num ** 2
#
# print(squared_dict)


#Q5
# dict1 = {"a": 100, "b": 200, "c": 300}
# dict2 = {"a": 150, "b": 200, "d": 400}
#
# combined_dict = dict1.copy()  # Create a copy of dict1
#
# for key, value in dict2.items():
#     if key in combined_dict:
#         combined_dict[key] += value
#     else:
#         combined_dict[key] = value
#
# print(combined_dict)


#Q6
# list1 = ["Ten", "Twenty", "Thirty"]
# list2 = [10,20, 30]
#
# final_dictionary = {}
# for i in range(len(list1)):
#     dictionary[list1[i]] = list2[i]
#
# print(dictionary)


#Q7
# sampleDict = {
#     "class": {
#         "student": {
#             "name": "mike",
#             "mark": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
#
# output = sampleDict["class"]["student"]["mark"]["history"]
#
# print(output)


#Q8
# myDict = {
#     1: "Alaa",
#     5: "Hadeel",
#     7: "Hanin",
#     13: "Malak",
# }
#
# # Print values for keys less than 10
# value_key = "->".join(
#                     value for key, value in myDict.items()
#                         if key < 10
#                     )
#
# print(value_key)
