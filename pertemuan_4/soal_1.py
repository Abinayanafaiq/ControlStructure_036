class Karyawan: 
    def __init__(self, nama, gaji:int, jabatan, tambah):  
        self.nama = nama
        self.gaji = gaji
        self.jabatan = jabatan
        self.tambah = tambah
    def tampilkan_info(self):
        return f"Nama: {self.nama}, Gaji: {self.gaji}, Jabatan: {self.jabatan}"
    
    def naikkan_gaji(self):
         self.gaji += self.tambah
         return self.gaji



try: 
    gaji = int(input("kasih Gaji Awal Pertama: "))
    tambah = int(200000)
    nama = str(input("Tambahkan Nama karyawan: "))
    jabatan = str(input("Tambahkan Jabatan: "))

    karyawan = Karyawan(nama, gaji, jabatan, tambah)
    
    print("--INFORMASI Karyawan--")
    print(karyawan.tampilkan_info())
    print(f"GAJI AWAL : {gaji}")
    print("--SETELAH NAIK GAJI--")
    print(karyawan.naikkan_gaji())

    
except ValueError as e: 
    print(f"Salah lagi {e}")

finally: 
    print("program selesai")