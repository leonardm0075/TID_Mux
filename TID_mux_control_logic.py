import RPi.GPIO as GPIO
import time


class Transistor:
    def __init__(self, x_binary, y_binary, x_dec, y_dec,x1, x2, x3, x4, x5, y1, y2, y3, y4, y5):
        self.x_binary = x_binary
        self.y_binary = y_binary
        self.x_dec = x_dec
        self.y_dec = y_dec
        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4
        self.x5 = x5
        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4
        self.y5 = y5
   
    def print_tran(self):
        print("x binary: " + self.x_binary)
        print("y binary: " + self.y_binary)
        print("x1: " + self.x1)
        print("x2: " + self.x2)
        print("x3: " + self.x3)
        print("x4: " + self.x4) 
        print("x5: " + self.x5)
        print("----------")
        print("y1: " + self.y1)
        print("y2: " + self.y2)
        print("y3: " + self.y3)
        print("y4: " + self.y4)
        print("y5: " + self.y5)

def decimalToBinary(n):
    binary = bin(n).replace('0b', '')
    x = binary[::-1]
    while len(x) < 5:
        x+='0'
    binary = x[::-1]
    return binary

def getTran(tran_list):
    tran_num = input("Enter desired transistor number: ")
    print(" ")
    return tran_list[int(tran_num) - 1]

def main():
    
    transistor_list = []
    
    for x in range(1,33):     
        for y in range(1,25):
            x_binary = decimalToBinary(x)
            y_binary = decimalToBinary(y)
            transistor_list.append(Transistor(str(x_binary), str(y_binary), str(x), str(y), x_binary[0], x_binary[1], x_binary[2], x_binary[3], x_binary[4], y_binary[0], y_binary[1], y_binary[2], y_binary[3], y_binary[4]))
       


# MSB     LSB
# x1      x5
# y1      y5

    while True: 
        print("0: Iterate over all transistors row by row")
        print("1: Find specific transistor")
        sel = input("Enter choice: ")
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(21, GPIO.OUT)
        GPIO.setup(20, GPIO.OUT)
        GPIO.setup(16, GPIO.OUT)
        GPIO.setup(12, GPIO.OUT)
        GPIO.setup(1, GPIO.OUT)
        GPIO.setup(7, GPIO.OUT)
        GPIO.setup(8, GPIO.OUT)
        GPIO.setup(25, GPIO.OUT)
        GPIO.setup(24, GPIO.OUT)
        GPIO.setup(23, GPIO.OUT) 
        
        if sel == "0":
        
            for x in transistor_list:
                if x.x1 == "1":
                    print("x1: " + x.x1)
                    GPIO.output(21, GPIO.HIGH)
                else:
                    print("x1: " + x.x1)
                    GPIO.output(21, GPIO.LOW)
                if x.x2 == "1":
                    print("x2: " + x.x2)
                    GPIO.output(20, GPIO.HIGH)
                else:
                    print("x2: " + x.x2)
                    GPIO.output(20, GPIO.LOW)
                if x.x3 == "1":
                    print("x3: " + x.x3)
                    GPIO.output(16, GPIO.HIGH)
                else:
                    print("x3: " + x.x3)
                    GPIO.output(16, GPIO.LOW)
                if x.x4 == "1":
                    print("x4: " + x.x4)
                    GPIO.output(12, GPIO.HIGH)
                else:
                    print("x4: " + x.x4)
                    GPIO.output(12, GPIO.LOW)
                if x.x5 == "1":
                    print("x5: " + x.x5)
                    GPIO.output(1, GPIO.HIGH)
                else:
                    print("x5: " + x.x5)
                    GPIO.output(1, GPIO.LOW)
                
                print("----------")
                if x.y1 == "1":
                    print("y1: " + x.y1)
                    GPIO.output(7, GPIO.HIGH)
                else:
                    print("y1: " + x.y1)
                    GPIO.output(7, GPIO.LOW)
                if x.y2 == "1":
                    print("y2: " + x.y2)
                    GPIO.output(8, GPIO.HIGH)
                else:
                    print("y2: " + x.y2)
                    GPIO.output(8, GPIO.LOW)
                if x.y3 == "1":
                    print("y3: " + x.y3)
                    GPIO.output(25, GPIO.HIGH)
                else:
                    print("y3: " + x.y3)
                    GPIO.output(25, GPIO.LOW)
                if x.y4 == "1":
                    print("y4: " + x.y4)
                    GPIO.output(24, GPIO.HIGH)
                else:
                    print("y4: " + x.y4)
                    GPIO.output(24, GPIO.LOW)
                if x.y5 == "1":
                    print("y5: " + x.y5)
                    GPIO.output(23, GPIO.HIGH)
                else:
                    print("y5: " + x.y5)
                    GPIO.output(23, GPIO.LOW)
                         
                print( " ")
                print(" ")
                time.sleep(.01)
        
        if sel == "1":
            x = getTran(transistor_list)
            x.print_tran()
            print(" ")
            if x.x1 == "1":
                print("x1: " + x.x1)
                GPIO.output(21, GPIO.HIGH)
            else:
                print("x1: " + x.x1)
                GPIO.output(21, GPIO.LOW)
            if x.x2 == "1":
                print("x2: " + x.x2)
                GPIO.output(20, GPIO.HIGH)
            else:
                print("x2: " + x.x2)
                GPIO.output(20, GPIO.LOW)
            if x.x3 == "1":
                print("x3: " + x.x3)
                GPIO.output(16, GPIO.HIGH)
            else:
                print("x3: " + x.x3)
                GPIO.output(16, GPIO.LOW)
            if x.x4 == "1":
                print("x4: " + x.x4)
                GPIO.output(12, GPIO.HIGH)
            else:
                print("x4: " + x.x4)
                GPIO.output(12, GPIO.LOW)
            if x.x5 == "1":
                print("x5: " + x.x5)
                GPIO.output(1, GPIO.HIGH)
            else:
                print("x5: " + x.x5)
                GPIO.output(1, GPIO.LOW)
            
            print("----------")
            if x.y1 == "1":
                print("y1: " + x.y1)
                GPIO.output(7, GPIO.HIGH)
            else:
                print("y1: " + x.y1)
                GPIO.output(7, GPIO.LOW)
            if x.y2 == "1":
                print("y2: " + x.y2)
                GPIO.output(8, GPIO.HIGH)
            else:
                print("y2: " + x.y2)
                GPIO.output(8, GPIO.LOW)
            if x.y3 == "1":
                print("y3: " + x.y3)
                GPIO.output(25, GPIO.HIGH)
            else:
                print("y3: " + x.y3)
                GPIO.output(25, GPIO.LOW)
            if x.y4 == "1":
                print("y4: " + x.y4)
                GPIO.output(24, GPIO.HIGH)
            else:
                print("y4: " + x.y4)
                GPIO.output(24, GPIO.LOW)
            if x.y5 == "1":
                print("y5: " + x.y5)
                GPIO.output(23, GPIO.HIGH)
            else:
                print("y5: " + x.y5)
                GPIO.output(23, GPIO.LOW)
                     
            print( " ")
            print(" ")
            time.sleep(1)
        
        
    

    

if __name__ == "__main__":
    main()
