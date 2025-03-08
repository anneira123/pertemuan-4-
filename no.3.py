class Orang:
    def __init__(self , FirstName, LastName, NumberID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.NumberID = NumberID
        
class Karyawan:
    def __init__(self, FirstName, LastName, nomerID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.nomerID = nomerID
    def status (self,status):
        self.status = status
karyawan1 = Karyawan('Adi', 'wijaya', 2007)
karyawan1.status ("tetap")
print (f"status {karyawan1.FirstName} sebagai karyawan {karyawan1.status}")