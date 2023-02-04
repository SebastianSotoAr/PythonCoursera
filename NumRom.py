
class NumRom:

    def Int_in_roman(self, num):
        
        self.contador = num
        self.num_inc = ""
        self.num_imp = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        self.sim_imp = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

        for m in range(len(self.num_imp)):

            while self.contador >= self.num_imp[m]:

                self.num_inc += self.sim_imp[m]
                self.contador -= self.num_imp[m]

        return self.num_inc

num_eli = NumRom()
X = num_eli.Int_in_roman
print(X(27), X(8), X(10), X(7), X(728))
