# Here we fill an array
def fill_array(elements_quantity):
    result_array = []

    for i in range(elements_quantity):
        temp_num = int(input("Enter your number: "))
        result_array.append(temp_num)

        if elements_quantity - i - 1 > 0:
            print(f"{elements_quantity - i - 1} numbers left")

    print("\nThe array is filled: " + str(result_array))
    return result_array


# Here we find the special number
def find_special_number(array, d_number):
    for i in range(len(array) - 1):
        if array[i] + array[i + 1] < d_number:
            return i

    return -1


filled_array = fill_array(10)
result = find_special_number(filled_array, 17)

print(f"index of the number is {result}" if result != -1 else "The index of the number was not found :(")