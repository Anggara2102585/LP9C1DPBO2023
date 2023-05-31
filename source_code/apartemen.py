from hunian import Hunian

class Apartemen(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, foto_bangunan):
        super().__init__("Apartemen", jml_penghuni, jml_kamar, foto_bangunan)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Sertifikat Hak Milik Atas Satuan Rumah Susun (SHMSRS) a/n " + self.nama_pemilik + "."

    def get_nama_pemilik(self):
        return self.nama_pemilik
    
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\n"

    def is_kosong(self):
        if (self.jml_penghuni == 0):
            return True
        else:
            return False