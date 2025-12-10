class Counter:
    def __init__(self, values, limits):
        self.values = values
        self.limits = limits
    def add_one(self):
        for i in reversed(range(0,len(self.values))):
            carry = False 
            x = self.values[i] + 1
            self.values[i] = x
            if x >= self.limits[i]:
                carry = True
                self.values[i] = 0
                # self.values[i-1]   
            if not carry:
                break
    def get_number(self):
        return self.values
    def percent(self):
        q = []
        for i, value in enumerate(self.values):
            q.append(value/self.limits[i])
        return q


domain = Counter([0,0,0,0,0,0,0], [21,5,21,5,21,5,21])
ip = Counter([1,0,0,0],[256,256,256,256])

i = 0
VIEW = 0000

while True:
    i += 1


    domain.add_one()
    ip.add_one()

    name = domain.get_number()
    name = "TKXVFJRA"[name[0]] + "UEOIA"[name[1]] + "QNZHWTKXVFJRDBLGSPYCM"[name[2]] + "EOIAU"[name[3]] + "KXVFJRDBLGSPYCMQNZHWT"[name[4]] + "IAUEO"[name[5]] + "BLGSPYCMQNZHWTKXVFJRD"[name[6]]


    #if i > VIEW:
    #    print(name.lower(), ".".join(map(str,ip.get_number())), ".".join(map(str,domain.get_number())))


    #
    #if i % 1000 == 0:
    if name[0] == "R" or i % 100000 == 0: print(name.lower(), ".".join(map(str,ip.get_number())))

    if name.lower() == "RATATAT":
        print(name, ip.get_number())
        break


# wehaziben
