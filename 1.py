from pyfirmata import Arduino,SERVO,util
from time import sleep

port= "COM5"
pin = 10
board= Arduino(port)

board.digital[pin].mode=SERVO

def cevir_servo(pin,angle):
    board.digital[pin].write(angle)
    sleep(0.001)


while True:
    x=input('sayı giriniz: ')   

    if x == "1":
        for i in range(0,45):
            cevir_servo(pin,i)

    elif x=='2':        
        for i in range(0,90):
            cevir_servo(pin,i)

    elif x=='3':
        for i in range(0,180):
            cevir_servo(pin,i)

