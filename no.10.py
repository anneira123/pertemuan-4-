class Orang:
    def __init__(self , FirstName, LastName, NumberID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.NumberID = NumberID
    def orang(self):
        return f"Nama: {self.FirstName} {self.LastName}, ID: {self.NumberID}"

class Pelajar:
    def __init__(self, FirstName, LastName, nomerID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.nomerID = nomerID
        self.mata_kuliah = []
    def pelajar(self):
        return f"Pelajar: {self.FirstName} {self.LastName}, ID: {self.nomerID}, Mata Kuliah: {', '.join(self.mata_kuliah)}"

class Pengajar:
    def __init__(self):
        self.matkul_yang_diajar = []
    def pengajar(self):
        return f"Mata Kuliah yang Diajar: {', '.join(self.matkul_yang_diajar)}"

class Asdos(Orang, Pelajar, Pengajar):
    def __init__(self, FirstName, LastName, NumberID):
        Orang.__init__(self, FirstName, LastName, NumberID)
        Pelajar.__init__(self, FirstName, LastName, NumberID)
        Pengajar.__init__(self)

    def asdos (self):
        return f"{self.orang()}, {self.pelajar()}, {self.pengajar()}"
    
asdos1 = Asdos("uswatun", "khasanah", 456456)
asdos1.mata_kuliah.append("big data")
asdos1.matkul_yang_diajar.append("kecerdasan artifisial")

print(asdos1.asdos())