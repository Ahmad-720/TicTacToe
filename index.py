from tkinter import *

class View:
    def __init__(self):
        self.root = Tk()
        self.root.title("TicTacToe")

        self.reset_button = Button(self.root,text="RESET", bg="red",padx=20,pady=15,command=self.reset_clicked)
        
        self.buttons = [[],[],[]]

        self.buttons[0].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(0)))
        self.buttons[0].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(1)))
        self.buttons[0].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(2)))
        self.buttons[1].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(3)))
        self.buttons[1].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(4)))
        self.buttons[1].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(5)))
        self.buttons[2].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(6)))
        self.buttons[2].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(7)))
        self.buttons[2].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(8)))

        self.display_buttons()
        self.display_reset_button()

    def display_reset_button(self):
        self.reset_button.grid(row=0,column=3)

    def display_buttons(self):

        for ro in range(len(self.buttons)):
            for co in range(len(self.buttons[ro])):
                self.buttons[ro][co].grid(row=ro,column=co,padx=5,pady=5)
    
    def remove_button(self,i):
        if i >= 0 and i <= 2:
            self.buttons[0][i].grid_forget()
        elif i >= 3 and i <= 5:
            self.buttons[1][i%3].grid_forget()
        elif i >= 6 and i <= 8:
            self.buttons[2][i%6].grid_forget()

    def set_label(self,i,player):
        if i >= 0 and i <= 2:
            self.buttons[0][i] = Label(self.root,text=player,padx=50,pady=45,fg='black',bg="red")
            self.buttons[0][i].grid(row=0,column=i,padx=5,pady=5)
        elif i >= 3 and i <= 5:
            self.buttons[1][i%3] = Label(self.root,text=player,padx=50,pady=45,fg='black',bg="red")
            self.buttons[1][i%3].grid(row=1,column=i%3,padx=5,pady=5)
        elif i >= 6 and i <= 8:
            self.buttons[2][i%6] = Label(self.root,text=player,padx=50,pady=45,fg='black',bg="red")
            self.buttons[2][i%6].grid(row=2,column=i%6,padx=5,pady=5)

    def reset_clicked(self):
        for i in range(9):
            self.remove_button(i)
        
        self.buttons = [[],[],[]]

        self.buttons[0].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(0)))
        self.buttons[0].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(1)))
        self.buttons[0].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(2)))
        self.buttons[1].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(3)))
        self.buttons[1].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(4)))
        self.buttons[1].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(5)))
        self.buttons[2].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(6)))
        self.buttons[2].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(7)))
        self.buttons[2].append(Button(self.root,padx=50,pady=45,command=lambda:self.controller.button_clicked(8)))

        self.display_buttons()

    

class Controller:
    def __init__(self,view_,model_):
        self.view = view_

        self.model = model_

        self.player = "X"

    def button_clicked(self,i):
        self.view.remove_button(i)

        self.view.set_label(i,self.player)

        self.model.button_clicked(i,self.player)

        if self.player == 'X':
            self.player = 'O'
        else:
            self.player = 'X'
    


class Model:
    def __init__(self):
        self.board = [['-','-','-'],['-','-','-'],['-','-','-']]

    def button_clicked(self,i,player):
        if i >= 0 and i <= 2:
            self.board[0][i] = player
        elif i >= 3 and i <= 5:
            self.board[1][i%3] = player
        elif i >= 6 and i <= 8:
            self.board[2][i%6] = player

        print(self.board)
        


view_ = View()

model_ = Model()

controller_ = Controller(view_,model_)

view_.controller = controller_

model_.controller = controller_

view_.root.mainloop()