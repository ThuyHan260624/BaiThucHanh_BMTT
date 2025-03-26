def truy_cap_phan_tu(tuple_data):
    first_element = tuple_data[0]
    last_element = tuple_data[-1]
    return first_element, last_element
input_list = input("Nhập dãy số cách nhau bằng dấu cách: ")
first, last = truy_cap_phan_tu(tuple(map(int, input_list.split(','))))
print(f"Phần tử đầu tiên trong tuple là: {first}")
print(f"Phần tử cuối cùng trong tuple là: {last}")
