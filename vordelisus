def vordelisus(eq_list):
    print(eq_list)

    results = []

    for k in range(len(eq_list['first_elements'])):
        k0 = eq_list.get('first_elements')[k] / eq_list.get('second_elements')[k]
        results.append(k0)

    print(results)

    print(all(x == results[0] for x in results))


first_numbers_list, second_numbers_list = [], []

numbers_dict = {"first_elements": first_numbers_list, "second_elements": second_numbers_list}

number_of_elements = int(input("Enter the number of elements: "))

while number_of_elements % 2 != 0:
    number_of_elements = int(input("Enter the number of elements: "))

rounded_number = round(number_of_elements / 2)

for i in range(rounded_number):
    first_element = float(input('first numbers: '))
    first_numbers_list.append(first_element)

for j in range(rounded_number):
    second_element = float(input('second numbers: '))
    second_numbers_list.append(second_element)

first_numbers_list.sort()
second_numbers_list.sort()

vordelisus(numbers_dict)
