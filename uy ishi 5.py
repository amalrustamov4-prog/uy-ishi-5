# Asosiy klass
class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def get_info(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"


# Fan klassi
class Fan:
    def __init__(self, nomi):
        self.nomi = nomi

    def get_info(self):
        return f"Fan: {self.nomi}"


# Talaba klassi
class Talaba(Shaxs):
    def __init__(self, ism, yosh):
        super().__init__(ism, yosh)
        self.fanlar = []

    def fanga_yozil(self, fan):
        self.fanlar.append(fan)

    def remove_fan(self, fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
            print(f"{fan.nomi} fani o'chirildi.")
        else:
            print("Siz bu fanga yozilmagansiz.")

    def get_info(self):
        fanlar = ", ".join([fan.nomi for fan in self.fanlar])
        return f"Talaba: {self.ism}, Yosh: {self.yosh}, Fanlar: {fanlar}"


# Professor klassi
class Professor(Shaxs):
    def __init__(self, ism, yosh, kafedra):
        super().__init__(ism, yosh)
        self.kafedra = kafedra

    def get_info(self):
        return f"Professor: {self.ism}, Yosh: {self.yosh}, Kafedra: {self.kafedra}"


# Foydalanuvchi klassi
class Foydalanuvchi(Shaxs):
    def __init__(self, ism, yosh, login):
        super().__init__(ism, yosh)
        self.login = login

    def get_info(self):
        return f"Foydalanuvchi: {self.ism}, Login: {self.login}"


# Admin klassi (Foydalanuvchidan voris)
class Admin(Foydalanuvchi):
    def __init__(self, ism, yosh, login):
        super().__init__(ism, yosh, login)

    def ban_user(self):
        print("Foydalanuvchi bloklandi")

    def get_info(self):
        return f"Admin: {self.ism}, Login: {self.login}"


# Sotuvchi klassi
class Sotuvchi(Shaxs):
    def __init__(self, ism, yosh, dokon):
        super().__init__(ism, yosh)
        self.dokon = dokon

    def get_info(self):
        return f"Sotuvchi: {self.ism}, Do'kon: {self.dokon}"


# Mijoz klassi
class Mijoz(Shaxs):
    def __init__(self, ism, yosh, balans):
        super().__init__(ism, yosh)
        self.balans = balans

    def get_info(self):
        return f"Mijoz: {self.ism}, Balans: {self.balans}"


# ==========================
# Obyektlar yaratish
# ==========================

mat = Fan("Matematika")
fiz = Fan("Fizika")
ing = Fan("Ingliz tili")

talaba = Talaba("Ali", 20)
talaba.fanga_yozil(mat)
talaba.fanga_yozil(fiz)

print(talaba.get_info())

talaba.remove_fan(mat)
print(talaba.get_info())

talaba.remove_fan(ing)

prof = Professor("Karimov", 45, "Informatika")
print(prof.get_info())

foyd = Foydalanuvchi("Vali", 30, "vali123")
print(foyd.get_info())

admin = Admin("Admin", 35, "admin01")
print(admin.get_info())
admin.ban_user()

sotuvchi = Sotuvchi("Hasan", 40, "Tech Market")
print(sotuvchi.get_info())

mijoz = Mijoz("Olim", 25, 500000)
print(mijoz.get_info())