print("Nhap cac dong van ban(Nhap done de ket thuc):")
lines = []
while True:
    line = input()
    if line == "done":
        break
    lines.append(line)
print("\n Cac dong sau khi nhap se chuyen thanh chhu hoa")
for line in lines:
    print(line.upper())