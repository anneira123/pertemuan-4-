class Pengajar:
    def __init__(self):
        self.matkul_yang_diajar = []

    def mengajar(self, mata_kuliah):
        self.matkul_yang_diajar.append(mata_kuliah)

pengajar1 = Pengajar()
pengajar1.mengajar("Matematika")
pengajar1.mengajar("Fisika")

print(pengajar1.matkul_yang_diajar)