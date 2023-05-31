class Hunian():
    def __init__(self, jenis, jml_penghuni = 1, jml_kamar = 1, foto_bangunan = "assets/house1.jpg"):
        self.jenis = jenis
        self.jml_penghuni = jml_penghuni
        self.jml_kamar = jml_kamar
        self.foto_bangunan = foto_bangunan

    def get_jenis(self):
        return self.jenis

    def get_jml_penghuni(self):
        return self.jml_penghuni

    def get_jml_kamar(self):
        return self.jml_kamar
    
    def get_foto_bangunan(self):
        return self.foto_bangunan

    def get_dokumen(self):
        pass

    def get_summary(self):
        return "Hunian "+ self.jenis +", ditempati oleh " + str(self.jml_penghuni) + " orang."