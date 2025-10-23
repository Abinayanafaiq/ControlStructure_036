class persegiPanjang :
    def __init__(self, p, l):
        self.p = p
        self.l = l

    def luasPersegiPanjang(self): 
        return self.p * self.l
    
    def kelilingPersegiPanjang(self):
        return 2 * (self.p + self.l)
    
    def __str__(self):
        return f"Persegi Panjang dibuat dengan panjang = {self.p} dan lebar = {self.l}"
    


try : 
    panjang = int(input("isikan Panjang: "))
    lebar = int(input("Masukan lebar: "))

    pp = persegiPanjang(panjang, lebar)

    luas = pp.luasPersegiPanjang()
    print(f"Luas Persegi Panjang: {luas}")

    keliling = pp.kelilingPersegiPanjang()
    print(f"Keliling Persegi Panjang: {keliling}")

except ValueError as e: 
    print(f"Inputan harus berupa angka: {e}")
    exit()

finally:
    print("Program Selesai")

