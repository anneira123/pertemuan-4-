class Orang:
    def __init__(self , FirstName, LastName, NumberID):
        self.FirstName = FirstName
        self.LastName = LastName
        self.NumberID = NumberID

lili = Orang ('lili', 'esther', 2006)

print((lili.FirstName) + str(lili.LastName) + str(lili.NumberID))
    
        