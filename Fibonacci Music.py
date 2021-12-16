import webbrowser as wb
import time

n = int(input("How many fibonacci notes do you want to hear: "))
gap  = float(input("How much time gap (in sceonds) do you want between the notes: "))

fib_1 = 0
fib_2 = 1

li_fib = [fib_1, fib_2]

for i in range(n-2):
    fib_3 = fib_1 + fib_2
    li_fib.append(fib_3)
    fib_1 = fib_2
    fib_2 = fib_3

li_notes = ["C1", "D1", "E1", "F1", "G1", "A1", "B1", "C2", "D2", "E2"]


for j in li_fib:
    for k in str(j):
        note = int(k)
        print("  "*note + li_notes[note])
        
        if note == 0:    
            wb.open("C_0.mp3")
            
        elif note == 1:
            wb.open("D_1.mp3")
            
        elif note == 2:   
            wb.open("E_2.mp3")
            
        elif note == 3: 
            wb.open("F_3.mp3")
            
        elif note == 4:   
            wb.open("G_4.mp3")
            
        elif note == 5:   
            wb.open("A_5.mp3")
        
        elif note == 6:   
            wb.open("B_6.mp3")
           
        elif note == 7:   
            wb.open("C_7.mp3")
        
        elif note == 8:   
            wb.open("D_8.mp3")
        
        elif note == 9:   
            wb.open("E_9.mp3")
            
        time.sleep(gap)