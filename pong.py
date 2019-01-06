from tkinter import *


#fenetre
pong = Tk()
pong.title('Le pong')
main_canvas = Canvas(pong,width=1000, height=600, bg='black')
main_canvas.grid()

    ##Paramètres##
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
Pos_bX = 490
Pos_bY = 290
#balle
balle = main_canvas.create_oval(Pos_bX, Pos_bY,Pos_bX+20,Pos_bY+20, fill='white')
#amplitude mouvement balle
dbx = -2
dby = 1

#Score
scoreJ1 = 0
scoreJ2 = 0



##Jeu##

def movement_balle():
    global dbx, dby
    #rebondissement bord map
    #a garder pour option
    """if (main_canvas.coords(balle)[0]>997) or (main_canvas.coords(balle)[2]==2):
        dbx=-1*dbx"""
    if (main_canvas.coords(balle)[1]>590) or (main_canvas.coords(balle)[3]==10):
        dby =- 1*dby
    #position balle
    main_canvas.move(balle,dbx,dby)
    #collision balle raquette
    if (main_canvas.coords(balle)[0] < main_canvas.coords(raquette_1)[2]) and (main_canvas.coords(balle)[3] < main_canvas.coords(raquette_1)[3]) and (main_canvas.coords(balle)[1] > main_canvas.coords(raquette_1)[1]):
        dbx =- 1*dbx
    if (main_canvas.coords(balle)[2] > main_canvas.coords(raquette_2)[0]) and (main_canvas.coords(balle)[3] < main_canvas.coords(raquette_2)[3]) and (main_canvas.coords(balle)[1] > main_canvas.coords(raquette_2)[1]):
        dbx =- 1*dbx
    #loop
    pong.after(10,movement_balle)

def movement_raquette1():

    #vérification dépassage raquette bordure haute
    if (main_canvas.coords(raquette_1)[1]<0):
        main_canvas.move(raquette_1, 0, 1)
    #vérification dépassage raquette bordure bassse
    if (main_canvas.coords(raquette_1)[3]>600):
        main_canvas.move(raquette_1, 0, -1)
    #Score J1
    if (main_canvas.coords(balle)[0]>997):
        scoreJ1 += 1 
    #Score J2
    if (main_canvas.coords(balle)[2]<2):
        scoreJ2 += 1


    #deplacement raquette 1
    def haut(event):
        main_canvas.move(raquette_1, 0, -10)
    def bas(event):
        main_canvas.move(raquette_1, 0, 10)
    main_canvas.bind_all("z", haut)
    main_canvas.bind_all("s", bas)

    pong.after(1,movement_raquette1)

def movement_raquette2():
    #vérification dépassage raquette bordure haute
    if (main_canvas.coords(raquette_2)[1]<0):
        main_canvas.move(raquette_2, 0, 1)
    #vérification dépassage raquette bordure basse
    if (main_canvas.coords(raquette_2)[3]>600):
        main_canvas.move(raquette_2, 0, -1)
    #déplacement raquette 2
    def haut2(event):
            main_canvas.move(raquette_2, 0, -10)
    def bas2(event):
        main_canvas.move(raquette_2, 0, 10)
    main_canvas.bind_all("<Up>", haut2)
    main_canvas.bind_all("<Down>", bas2)

    pong.after(1,movement_raquette2)

def menu():
    btn_jeu.grid()

def jeu():
    btn_jeu.place_forget()
    movement_balle()
    movement_raquette1()
    movement_raquette2()
    btn_quitter.grid()

##Boutton##

btn_quitter = Button(pong, text="Quitter", width = 10, height= 2, command = pong.destroy)
btn_jeu = Button(pong, text = "Jouer", command = jeu)

#appelle fonction

menu()
pong.mainloop()