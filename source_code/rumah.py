from hunian import Hunian

class Rumah(Hunian):
    def __init__(self, nama_pemilik, jml_penghuni, jml_kamar, foto_bangunan):
        super().__init__("Rumah", jml_penghuni, jml_kamar, foto_bangunan)
        self.nama_pemilik = nama_pemilik

    def get_dokumen(self):
        return "Izin Mendirikan Bangunan (IMB) a/n " + self.nama_pemilik

    def get_nama_pemilik(self):
        return self.nama_pemilik
   
    def get_detail(self):
        return "Pemilik : " + self.nama_pemilik + "\nJumlah Penghuni : " + str(self.jml_penghuni) + "\nJumlah Kamar : " + str(self.jml_kamar) + "\nPajak : " + str(self.get_pajak()) + "\n"

    def get_pajak(self):
        return self.jml_kamar * 500000