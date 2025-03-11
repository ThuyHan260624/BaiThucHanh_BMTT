def xoa_phan_tu(dictionary, data):
    if data in dictionary:
        del dictionary[data]
        return True
    else:
        return False
my_dict = {'a': 1, 'b': 2, 'c': 3}
data_to_delete = 'b'
result = xoa_phan_tu(my_dict, data_to_delete)
if result:
    print(f"Dictionary sau khi xóa phần tử  là: {my_dict}")
else:
    print(f"Phần tử không tồn tại trong dictionary")