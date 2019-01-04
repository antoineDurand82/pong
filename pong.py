from tkinter import *

def movement_balle():
    global dbx, dby
    #rebondissement bord map
    if (main_canvas.coords(balle)[0]>997) or (main_canvas.coords(balle)[2]==2):
        dbx=-1*dbx
    if (main_canvas.coords(balle)[1]>600) or (main_canvas.coords(balle)[3]==0):
        dby=-1*dby
    #position
    main_canvas.move(balle,dbx,dby)
    #loop
    pong.after(10,movement_balle)

def movement_raquette():
    if (main_canvas.coords(raquette_1)[1]<600) or (main_canvas.coords(raquette_1)[3]==0):
        def haut(event):
            main_canvas.move(raquette_1, 0, -10)
        def bas(event):
            main_canvas.move(raquette_1, 0, 10)
        main_canvas.bind_all("z", haut)
        main_canvas.bind_all("s", bas)
        
    if (main_canvas.coords(raquette_2)[1]<600) or (main_canvas.coords(raquette_2)[3]==0):
        def haut2(event):
            main_canvas.move(raquette_2, 0, -10)
        def bas2(event):
            main_canvas.move(raquette_2, 0, 10)
        main_canvas.bind_all("<Up>", haut2)
        main_canvas.bind_all("<Down>", bas2)









pong = Tk()

#fenetre
main_canvas = Canvas(pong,width=1000, height=600, bg='black')
main_canvas.grid()

#position raquette 1
Pos_rX1 = 10
Pos_rY1 = 250
#position raquette 2
Pos_rX2 = 990
Pos_rY2 = 250
#raquette
raquette_1 = main_canvas.create_rectangle(Pos_rX1,Pos_rY1,Pos_rX1+10, Pos_rY1+70, fill='white', outline='white')
raquette_2 = main_canvas.create_rectangle(Pos_rX2,Pos_rY2,Pos_rX2-10, Pos_rY2+70, fill='white', outline='white')
#touche mouvement

#position balle
Pos_bX = 500
Pos_bY = 300
#balle
balle = main_canvas.create_oval(Pos_bX, Pos_bY,Pos_bX+20,Pos_bY+20, fill='white')
#amplitude mouvement balle
dbx = 4
dby = 2

#appelle fonction
movement_balle()
movement_raquette()
pong.mainloop()