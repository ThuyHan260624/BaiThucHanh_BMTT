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
