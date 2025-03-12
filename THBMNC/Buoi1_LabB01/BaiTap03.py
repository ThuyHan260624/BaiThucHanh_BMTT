def tuple_list(n):
    return tuple(n)
input_list = input("Nhập dãy số cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(',')))
tuple_numbers = tuple_list(numbers)
print(f"Dãy số sau khi chuyển sang tuple là: {tuple_numbers}")