from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while True:
    print("Chuong quan ly sinh vien:")
    print("-------------------------")
    print("1. Nhap sinh vien")
    print("2. Cap nhat sinh vien theo ID")
    print("3. Xoa sinh vien theo ID")
    print("4. Tim kiem sinh vien theo ID")
    print("5. Sap xep sinh vien theo DTB")
    print("6. Sap xep sinh vien theo chuyen nganh")
    print("7. Hien thi danh sach sinh vien")
    print("0. Thoat chuong trinh")
    print("-------------------------")

    key = int(input("Nhap lua chon cua ban: "))
    if key == 1:
        print("Nhap thong tin sinh vien:")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong")
    elif key == 2:
        if qlsv.SoLuongSinhVien() > 0:
            print("\nCap nhat thong tin sinh vien:")
            print("Nhap ID")
            ID = int(input())
            if qlsv.updateSinhVien(ID):
                print("Cap nhat sinh vien thanh cong")
            else:
                print("Sinh vien khong ton tai")
        else:
            print("\nDanh sach sinh vien rong")
    elif key == 3:
        if qlsv.SoLuongSinhVien() > 0:
            print("\nXoa sinh vien theo ID:")
            print("Nhap ID")
            ID = int(input())
            if qlsv.deleteByID(ID):
                print("Xoa sinh vien thanh cong")
            else:
                print("Sinh vien khong ton tai")
        else:
            print("\nDanh sach sinh vien rong")
    elif key == 4:
        if qlsv.SoLuongSinhVien() > 0:
            print("\nTim kiem sinh vien theo ID:")
            print("Nhap ID")
            ID = int(input())
            searchResult = qlsv.findByID(ID)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien rong")
    elif key == 5:
        if qlsv.SoLuongSinhVien() > 0:
            print("\nSap xep sinh vien theo DTB:")
            qlsv.sortByDTB()
            qlsv.showDanhSachSinhVien()
        else:
            print("\nDanh sach sinh vien rong")
    elif key == 6:
        if qlsv.SoLuongSinhVien() > 0:
            print("\nSap xep sinh vien theo chuyen nganh:")
            qlsv.sortByName()
            qlsv.showDanhSachSinhVien()
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 7:
        if qlsv.SoLuongSinhVien() > 0:
            print("\nDanh sach sinh vien:")
            qlsv.showDanhSachSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong")
    elif key == 0:
        print("Thoat chuong trinh")
        break
    else:
        print("Lua chon khong hop le")
        print("Vui long chon lai")

class SinhVien:
    def __init__(self, id, name, dtb, chuyenNganh):
        self.id = id
        self.name = name
        self.dtb = dtb
        self.chuyenNganh = chuyenNganh

class QuanLySinhVien:
    def __init__(self):
        self.listSinhVien = []

    def generateID(self):
        if not self.listSinhVien:
            return 1
        maxId = self.listSinhVien[0].id
        for sv in self.listSinhVien:
            if sv.id > maxId:
                maxId = sv.id
        return maxId + 1

    def nhapSinhVien(self):
        id = self.generateID()
        name = input("Nhap ten sinh vien: ")
        dtb = float(input("Nhap diem trung binh: "))
        chuyenNganh = input("Nhap chuyen nganh: ")
        sv = SinhVien(id, name, dtb, chuyenNganh)
        self.listSinhVien.append(sv)

    def SoLuongSinhVien(self):
        return len(self.listSinhVien)

    def updateSinhVien(self, id):
        for sv in self.listSinhVien:
            if sv.id == id:
                sv.name = input("Nhap ten moi: ")
                sv.dtb = float(input("Nhap diem trung binh moi: "))
                sv.chuyenNganh = input("Nhap chuyen nganh moi: ")
                return True
        return False

    def deleteByID(self, id):
        for sv in self.listSinhVien:
            if sv.id == id:
                self.listSinhVien.remove(sv)
                return True
        return False

    def findByID(self, id):
        for sv in self.listSinhVien:
            if sv.id == id:
                return sv
        return None

    def showSinhVien(self, sv):
        if sv:
            print(f"ID: {sv.id}, Name: {sv.name}, DTB: {sv.dtb}, Chuyen nganh: {sv.chuyenNganh}")
        else:
            print("Sinh vien khong ton tai")

    def showDanhSachSinhVien(self, danhSach=None):
        if danhSach is None:
            danhSach = self.listSinhVien
        for sv in danhSach:
            print(f"ID: {sv.id}, Name: {sv.name}, DTB: {sv.dtb}, Chuyen nganh: {sv.chuyenNganh}")

    def sortByDTB(self):
        self.listSinhVien.sort(key=lambda sv: sv.dtb, reverse=True)

    def sortByName(self):
        self.listSinhVien.sort(key=lambda sv: sv.name)

    def getListSinhVien(self):
        return self.listSinhVien