import tkinter as tk
import tkinter.messagebox,sys
last_check=True

root = tk.Tk()
root.geometry("300x300+1000+200")
root.title("Tic Tac Toe")
root.resizable(False, False)

player = "O"

def flip_player():
    global player
    if player == "X":
        player = "O"
    elif player == "O":
        player = "X"


def draw_text(buton):
    flip_player()
    buton["text"] = player
    buton.config(state="disabled")
    check_winner()
    if last_check:
        check_done()


def check_done():
    if buton1["state"] == buton2["state"] == buton3["state"] == buton4["state"] == buton5["state"] == buton6["state"] == \
            buton7["state"] == buton8["state"] == buton9["state"] == "disabled":
        tkinter.messagebox.showinfo(message="Berabere",title="GameOver")
        sys.exit()

def check_winner():
    global last_check
    if buton1["text"] == buton2["text"] == buton3["text"] != " " or buton4["text"] == buton5["text"] == buton6["text"] != " " or \
            buton7["text"] == buton8["text"] == buton9["text"] != " ":
        tkinter.messagebox.showinfo(title="Winner",message="Winner : {}".format(player))
        last_check=False
        sys.exit()

    elif buton1["text"] == buton4["text"] == buton7["text"] != " " or buton2["text"] == buton5["text"] == buton8["text"] != " " or \
            buton3["text"] == buton6["text"] == buton9["text"] != " ":
        tkinter.messagebox.showinfo(title="Winner", message="Winner : {}".format(player))
        last_check = False
        sys.exit()

    elif buton1["text"] == buton5["text"] == buton9["text"] != " " or buton3["text"] == buton5["text"] == buton7["text"] != " ":
        tkinter.messagebox.showinfo(title="Winner", message="Winner : {}".format(player))
        last_check = False
        sys.exit()


buton1 = tk.Button(text=" ",font="Arial 40 bold" ,command=lambda: draw_text(buton1))
buton1.place(x=0, y=0, width=100, height=100)

buton2 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton2))
buton2.place(x=100, y=0, width=100, height=100)

buton3 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton3))
buton3.place(x=200, y=0, width=100, height=100)

buton4 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton4))
buton4.place(x=0, y=100, width=100, height=100)

buton5 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton5))
buton5.place(x=100, y=100, width=100, height=100)

buton6 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton6))
buton6.place(x=200, y=100, width=100, height=100)

buton7 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton7))
buton7.place(x=0, y=200, width=100, height=100)

buton8 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton8))
buton8.place(x=100, y=200, width=100, height=100)

buton9 = tk.Button(text=" ", font="Arial 40 bold" ,command=lambda: draw_text(buton9))
buton9.place(x=200, y=200, width=100, height=100)


root.mainloop()
