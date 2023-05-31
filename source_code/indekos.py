from hunian import Hunian

class Indekos(Hunian):
    def __init__(self, nama_pemilik, nama_penghuni, foto_bangunan, biaya_kontrak):
        super().__init__("Indekos", 1, 1, foto_bangunan)
        self.nama_pemilik = nama_pemilik
        self.nama_penghuni = nama_penghuni
        self.biaya_kontrak = biaya_kontrak

    def get_dokumen(self):
        return "Bukti kontrak indekos oleh " + self.nama_penghuni + " dari " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik

    def get_nama_penghuni(self):
        return self.nama_penghuni
    
    def get_biaya_kontrak(self):
        return self.biaya_kontrak

    def get_summary(self):
        return "Hunian Indekos."
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nNama Penghuni : " + str(self.nama_penghuni) + "\nBiaya Kontrak : " + str(self.biaya_kontrak) + "\n"