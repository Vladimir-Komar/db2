
def handle_numbers(a, b, c):
    result = 0
    if a == 0:
        result = 1
    while a != b:
        a = a + 1
        if a % c == 0:
            result += 1
    return result


print (handle_numbers(1, 10, 2))


def handle_string(value):
    letter = 0
    str = 0
    for char in value:
        if char.isalpha():
            letter += 1
        if char.isdigit():
            str += 1
    return letter, str


print(handle_string("Hello world! 123!"))


def handle_list_of_tuples(parametr, list):
    if parametr == "name":
        number = 0
    elif parametr == "age":
        number = 1
    elif parametr == "height":
        number = 2
    elif parametr == "weight":
        number = 3
    list.sort(key=lambda tup: tup[number])
    return list


print (handle_list_of_tuples("name", [
    ("Tom", "19", "167", "54"),
    ("Jony", "24", "180", "69"),
    ("Json", "21", "185", "75"),
    ("John", "27", "190", "87"),
    ("Jony", "24", "191", "98"),
    ]))
