class Rumah:
    alamat = ""
    atap = ""

    def deskripsi(self):
        print("Ini adalah sebuah rumah.")

class Apartemen(Rumah):
    def deskripsi(self):  
        super().deskripsi()
        print("Ini adalah sebuah apartemen.")

    def display(self):
        print("Alamat apartemen ini adalah:", self.alamat)

    def bentuk(self):
        print("Atap apartemen ini adalah:", self.atap)
    
    def fasilitas(self):
        print("Apartemen ini memiliki kolam renang dan gym.")

class Villa(Rumah):
    def deskripsi(self):  
        super().deskripsi()
        print("Ini adalah sebuah villa.")

    def display(self):
        print("Alamat villa ini adalah:", self.alamat)

    def bentuk(self):
        print("Atap villa ini adalah:", self.atap)
    
    def fasilitas(self):
        print("Villa ini memiliki taman pribadi dan area BBQ.")


apartemen_jakarta = Apartemen()
apartemen_jakarta.atap = "Coklat"
apartemen_jakarta.alamat = "Jl. Sudirman No. 10, Jakarta"
apartemen_jakarta.deskripsi()  
apartemen_jakarta.display()
apartemen_jakarta.bentuk()
apartemen_jakarta.fasilitas()


villa_bali = Villa()
villa_bali.atap = "Hitam"
villa_bali.alamat = "Jl. Diponegoro No. 15, Bali"
villa_bali.deskripsi()  
villa_bali.display()
villa_bali.bentuk()
villa_bali.fasilitas()
