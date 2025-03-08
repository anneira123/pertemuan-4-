class Karyawan:
    def __init__(self, FirstName, LastName, nomerID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.nomerID = nomerID
    def status (self,status):
        self.status = status
class Dosen:
    def __init__(self, FirstName, LastName, nomerID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.nomerID = nomerID
        self.matkul_yang_diajar = []
    
    def mengajar (self, matkul):
        self.matkul_yang_diajar.append(matkul)
    def status (self,status):
        self.status = status
dosen1 = Dosen("laila", "moon", 43312)
dosen1.mengajar ('matematika')
dosen1.mengajar('fisika murni')
dosen1.mengajar('fluida')
dosen1.status('Tidak Tetap')
print(f"{dosen1.FirstName} mengajar matkul {dosen1.matkul_yang_diajar} status: dosen {dosen1.status}")