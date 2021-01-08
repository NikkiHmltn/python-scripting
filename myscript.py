# hello_file = open("hello.txt", "w")
# ga_intro = "Hello GA"
# hello_file.write(ga_intro)
# # print(hello_file.read())
# hello_file.close()

# car_file = open("car.txt", "w")
# new_car_list = "Tesla Model S\nMercedes C300\nToyota Camry"
# car_file.write(new_car_list)
# # print(car_file.read())
# car_file.close()

# my_new_file = open('person.txt', 'r+')
# my_new_file.write("nikki\nruben\nsimone")
# # print(my_new_file.readlines())
# my_new_file.close()

# with open('person.txt') as peoples:
#     people_list= peoples.readlines()

#     for each_person in people_list:
#         print(each_person)



# person_file = open('person.txt')
# print(person_file.read())
# person_file.close()

# with open('person.txt', 'w') as person_file:
#     person_file.write('Ruben')

# #append to a file
# with open('person.txt', 'a') as person_file:
#     person_file.write('\nRome')

# with open('person.txt', 'r+') as person_file:
#     # print(person_file.read())
#     # person_file.write('\nYvonne')
#     print(person_file.read())

# with open('hello.txt', 'w+') as hello_file:
#     print(hello_file.read())

with open('one_to_hundred.txt') as numbers:
    number_list = numbers.readlines()
    result = []
    for each_number in number_list:
        if 'Five' in each_number:
            result.append(each_number)
        elif 'Fifteen' in each_number:
            result.append(each_number)
        else: continue
    print(result)

# with open('prime_numbers.txt') as numbers:
#     number_list = numbers.readlines()

#     for each_number in number_list:
#         new_num = (int(each_number) * 2)
#         print(new_num)