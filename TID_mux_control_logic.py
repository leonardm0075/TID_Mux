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
    return tran_list[int(tran_num) - 1]

def main():
    
    transistor_list = []
    
    for x in range(1,33):     
        for y in range(1,25):
            x_binary = decimalToBinary(x)
            y_binary = decimalToBinary(y)
            transistor_list.append(Transistor(str(x_binary), str(y_binary), str(x), str(y), x_binary[0], x_binary[1], x_binary[2], x_binary[3], x_binary[4], y_binary[0], y_binary[1], y_binary[2], y_binary[3], y_binary[4]))
        
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(21, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(1, GPIO.OUT)
    #GPIO.setup(21, GPIO.OUT)
    #GPIO.setup(21, GPIO.OUT)
    #GPIO.setup(21, GPIO.OUT)
    #GPIO.setup(21, GPIO.OUT)
    #GPIO.setup(21, GPIO.OUT) 

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
                 
        print( " ")
        print(" ")
        time.sleep(.1)
    


    #for x in range(len(transistor_list)):
        # Add whatever else iterating functionality here
        #print("Transistor " + str(x+1) + ": " + "x binary adr: " + transistor_list[x].x_binary + " || " + "y binary adr: " + transistor_list[x].y_binary)
    #temp_tran = getTran(transistor_list) 
    #print(temp_tran.x_binary)
    #print(temp_tran.y_binary)
    

if __name__ == "__main__":
    main()
