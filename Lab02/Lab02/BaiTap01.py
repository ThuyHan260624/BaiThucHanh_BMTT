def tinh_tong_chan(n):
    tong =0
    for num in n:
        if num % 2 == 0:
            tong += num
    return tong
input_list = input("Nhập dãy số cách nhau bằng dấu cách: ")
numbers = list(map(int, input_list.split(',')))
tong_chan = tinh_tong_chan(numbers)
print(f"Tổng các số chẵn trong dãy số là: {tong_chan}")
