class Orang:
    def __init__(self , FirstName, LastName, NumberID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.NumberID = NumberID
        
class Mahasiswa:
    def __init__(self, FirstName, LastName, nomerID, jenjang):
        self.FirstName = FirstName
        self.LastName = LastName
        self.nomerID = nomerID
        self.jenjang = jenjang
        self.matkul = []
        
    def enrol (self, mata_kuliah):
        self.matkul.append(mata_kuliah)
        
mahasiswa1 = Mahasiswa("lili", "esther", 532111, "sarjana")
mahasiswa1.enrol ("matematika")
mahasiswa1.enrol("fluida")
print(f"matkul yang diambil {mahasiswa1.FirstName}:{mahasiswa1.matkul}")
