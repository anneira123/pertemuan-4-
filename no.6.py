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
dosen1 = Dosen("Rizki", "Setiabudi", 987654)
dosen1.mengajar ('statik')
dosen1.status('Tetap')
print(f"{dosen1.FirstName} mengajar matkul {dosen1.matkul_yang_diajar} status: dosen {dosen1.status}")