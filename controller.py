from pyfirmata import Arduino, SERVO

board = Arduino('COM5')
for i in range(7,12):
    board.digital[i].mode=SERVO

def led(fingers):
    if fingers[0] == 1:
        board.digital[7].write(80)
    else:
        board.digital[7].write(160)


    if fingers[1] == 1:
        print("2 - Ishladi")
        board.digital[8].write(180)
    else:
        board.digital[8].write(0)
    
    
    if fingers[2] == 1:
        board.digital[9].write(115)
    else:
        board.digital[9].write(0)
    

    if fingers[3] == 1:
        print("4 - Ishladi")
        board.digital[10].write(160)
    else:
        board.digital[10].write(20)
    


    if fingers[4] == 1:
        print("5 - Ishladi")
        board.digital[11].write(110)
    else:
        board.digital[11].write(10)
    