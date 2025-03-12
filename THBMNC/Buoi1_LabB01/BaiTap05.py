def dem_so_lan_xuat_hien(n):
    count_dict = {}
    for num in n:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    return count_dict
input_list = input("Nhập dãy số cách nhau bằng dấu cách: ")
word_list = input_list.split(',')
so_lan_xuat_hien = dem_so_lan_xuat_hien(word_list)
print(f"Số lần xuất hiện của các phần tử trong dãy số là: {so_lan_xuat_hien}")
