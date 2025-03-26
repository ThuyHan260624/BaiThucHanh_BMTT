def dao_nguoc_chuoi(chuoi):
    return chuoi[::-1]
input_String = input("Nhap mot chuoi:")
print("Chuoi sau khi dao nguoc la:", dao_nguoc_chuoi(input_String))
