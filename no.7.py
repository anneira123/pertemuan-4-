class Pelajar:
    def __init__(self, FirstName, LastName, nomerID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.nomerID = nomerID
        self.mata_kuliah = []
        
    def enrol_mata_kuliah(self, matkul):
        self.mata_kuliah.append(matkul)

pelajar1 = Pelajar("Rizki", "Setiabudi", 987654)
pelajar1.enrol_mata_kuliah("Statik")

print(f"{pelajar1.FirstName} mengambil matakuliah {pelajar1.mata_kuliah}")
