# python class to convert integer to roman numeral

class Roman:
    def int_to_roman(self, num):
        val = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
        sym = ["M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"]
        romanNum = ''
        i = 0
        while(num>0):
            for _ in range(num//val[i]):
                romanNum+=sym[i]
                num-=val[i]
            i+=1
        return romanNum

number = int(input("Enter number for changing : "))
print(Roman().int_to_roman(number))

