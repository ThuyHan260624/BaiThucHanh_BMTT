def tinh_dao_nguoc_list(n):
    return n[::-1]
input_list = input("Nhập dãy số cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(',')))
dao_nguoc_list = tinh_dao_nguoc_list(numbers)
print(f"Dãy số sau khi đảo ngược là: {dao_nguoc_list}")
