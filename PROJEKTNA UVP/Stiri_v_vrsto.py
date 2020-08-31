ZMAGA_PLAVI = "pl"
ZMAGA_RDECI = "rd"
IZENACENO = "iz"
POTEKA = "pot"
ZACETEK = "zac"

class Igra():
    def __init__(self):
        self.stanje = ZACETEK
        self.poteza = 1
        self.matrika = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.undo = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

    def zmaga(self):
        matrika = self.matrika
        for vrstica in matrika:
            for stolpec in range(4):
                if vrstica[stolpec] != 0 and vrstica[stolpec] == vrstica[stolpec + 1] == vrstica[stolpec + 2] == vrstica[stolpec + 3]:
                    return True
        for vrstica in range(3):
            for stolpec in range(7):
                if matrika[vrstica][stolpec] != 0 and matrika[vrstica][stolpec] == matrika[vrstica + 1][stolpec] == matrika[vrstica + 2][stolpec] == matrika[vrstica + 3][stolpec]:
                    return True
        for vrstica in range(3):
            for stolpec in range(4):
                if matrika[vrstica][stolpec] != 0 and matrika[vrstica][stolpec] == matrika[vrstica + 1][stolpec + 1] == matrika[vrstica + 2][stolpec + 2] == matrika[vrstica + 3][stolpec + 3]:
                    return True
        for vrstica in range(3):
            for stolpec in range(4):
                if matrika[5 - vrstica][stolpec] != 0 and  matrika[5 - vrstica][stolpec] == matrika[4 - vrstica][stolpec + 1] ==  matrika[3 - vrstica][stolpec + 2] ==  matrika[2 - vrstica][stolpec + 3]:
                    return True
        else:
            return False
    
    def izenaceno(self):
        for i in self.matrika:
            for j in i:
                if j == 0:
                    return False
        else:
            return True

    def potek(self,n):
        matrika = self.matrika
        poteza = self.poteza
        for i in range(6):
            k = i
            if matrika[i][n] == 0:
                break
            if matrika[5][n] != 0:
                k = 7
                break
        if k < 7:
            matrika[k][n] = (poteza % 2) + 1
            self.undo[k][n] = poteza
            self.poteza += 1

        if self.zmaga():
            if (poteza % 2) == 0:
                self.stanje = ZMAGA_PLAVI
                return ZMAGA_PLAVI
            else:
                self.stanje = ZMAGA_RDECI
                return ZMAGA_RDECI
        if self.izenaceno():
            self.stanje = IZENACENO
            return IZENACENO
        self.stanje = POTEKA
        return POTEKA

    def nazaj(self):
        self.poteza
        self.undo
        for i in range(6):
            for j in range(7):
                if self.undo[i][j] == self.poteza - 1:
                    self.undo[i][j] = 0
                    self.matrika[i][j] = 0
                    break
        self.poteza -= 1
        self.stanje = POTEKA
        return POTEKA
        
                

    def nova_igra(self):
        self.stanje = ZACETEK
        self.poteza = 1
        self.matrika = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
        self.undo =[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]

        


