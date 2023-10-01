#BANAR, JUDE MICHAEL P.
#BSIS-2A

from tkinter import *
from tkinter import messagebox

class GAME(Frame):

    def __init__(self):

        Frame.__init__(self)
        self.master.title("Game Character Creator")
        self.pack()

        self.label = Label(self, text = "Create your own Character!" , fg = "Orange", font = ("Comic Sans MS", 20, "bold"), width = 30)
        self.label.pack(padx = 5)
        self.label.pack(pady = 5)

        self.btn = Button(self, text = "Select a Role", fg = "Red", font = ("Comic Sans MS", 10, "bold"), command = self.role)
        self.label.pack(padx = 20)
        self.btn.pack(pady = 10)

    def role(self):

        self.label = Label(self, text = "Select a role below.", fg = "Gray", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.rb1 = IntVar()

        self.radiobtn = Radiobutton(self, text="Wizard", font = ("Comic Sans MS", 10), padx = 20, variable=self.rb1, value=1, command = self.wizard)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Knight", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb1, value=2, command = self.knight)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Archer", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb1, value=3, command = self.archer)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Assassin", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb1, value=4, command = self.assassin)
        self.radiobtn.pack()

    def wizard(self):

        self.label = Label(self, text = "Select a weapon below.", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.rb2 = IntVar()

        self.radiobtn = Radiobutton(self, text="Wizard Staff", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=1, command = self.wizard_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Sword", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=2, command = self.wizard_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Bow & Arrow", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=3, command = self.wizard_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Katar", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=4, command = self.wizard_abilities)
        self.radiobtn.pack()

    def knight(self):
        
        self.label = Label(self, text = "Select a weapon below.", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.rb2 = IntVar()

        self.radiobtn = Radiobutton(self, text="Wizard Staff", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=1, command = self.knight_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Sword", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=2, command = self.knight_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Bow & Arrow", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=3, command = self.knight_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Katar", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=4, command = self.knight_abilities)
        self.radiobtn.pack()

    def archer(self):

        self.label = Label(self, text = "Select a weapon below.", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.rb2 = IntVar()

        self.radiobtn = Radiobutton(self, text="Wizard Staff", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=1, command = self.archer_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Sword", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=2, command = self.archer_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Bow & Arrow", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=3, command = self.archer_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Katar", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=4, command = self.archer_abilities)
        self.radiobtn.pack()

    def assassin(self):

        self.label = Label(self, text = "Select a weapon below.", fg = "Gray", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.rb2 = IntVar()

        self.radiobtn = Radiobutton(self, text="Wizard Staff", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=1, command = self.archer_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Sword", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=2, command = self.archer_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Bow & Arrow", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=3, command = self.archer_abilities)
        self.radiobtn.pack()

        self.radiobtn = Radiobutton(self, text="Katar", font = ("Comic Sans MS", 10),padx = 20, variable=self.rb2, value=4, command = self.archer_abilities)
        self.radiobtn.pack()

    def wizard_abilities(self):

        self.label = Label(self, text = "Select an ability below.", fg = "Gray", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.label = Label(self, text = "[1]Energy Ball [2]Dragon Breath [3]Crown of Flame [4]Hail Storm", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.ability1 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability1)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability2 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability2)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability3 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability3)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.btn = Button(self, text = "Next", fg = "Blue", font = ("Comic Sans", 8, "bold"), command = self.final)
        self.label.pack(padx = 20)
        self.btn.pack(pady = 10)

    def knight_abilities(self):

        self.label = Label(self, text = "Select an ability below.", fg = "Gray", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.label = Label(self, text = "[1]Fire Slash [2]Power Slash [3]Gigantic Storm [4]Chaotic Disaster", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.ability1 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability1)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability2 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability2)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability3 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability3)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.btn = Button(self, text = "Next", fg = "Blue", font = ("Comic Sans", 8, "bold"), command = self.final)
        self.label.pack(padx = 20)
        self.btn.pack(pady = 10)

    def archer_abilities(self):

        self.label = Label(self, text = "Select an ability below.", fg = "Gray", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.label = Label(self, text = "[1]Take Aim [2]Quick Shot [3]Blazing Arrow [4]Frost Arrow", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.ability1 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability1)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability2 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability2)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability3 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability3)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.btn = Button(self, text = "Next", fg = "Blue", font = ("Comic Sans", 8, "bold"), command = self.final)
        self.label.pack(padx = 20)
        self.btn.pack(pady = 10)

    def assassin_abilities(self):

        self.label = Label(self, text = "Select an ability below.", fg = "Gray", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.label = Label(self, text = "[1]Cloaking [2]Enchant Poison [3]Sonic Acceleration [4]Meteor Assault", fg = "Black", font = ("Comic Sans MS", 10))
        self.label.pack()

        self.ability1 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability1)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability2 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability2)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.ability3 = Variable()
        self.entry1 = Entry(self, font = ("Comic Sans Ms", 15), textvariable = self.ability3)
        self.label.pack(padx = 5)
        self.entry1.pack(pady = 10)

        self.btn = Button(self, text = "Next", fg = "Blue", font = ("Comic Sans", 8, "bold"), command = self.final)
        self.label.pack(padx = 20)
        self.btn.pack(pady = 10)

    def final(self):
        try:
            role = ""
            if (self.rb1.get()==1):
                role = "Wizard"
            elif (self.rb1.get()==2):
                role = "Knight"
            elif (self.rb1.get()==3):
                role = "Archer"
            elif (self.rb1.get()==4):
                role = "Assassin"

            weapon = ""
            if (self.rb2.get()==1):
                weapon = "Wizard Staff"
            elif (self.rb2.get()==2):
                weapon = "Knight Sword"
            elif (self.rb2.get()==3):
                weapon = "Bow & Arrow"
            elif (self.rb2.get()==4):
                weapon = "Katar"

            if (self.rb1.get()==1):
                ability1 = ""
                if (self.ability1.get()=='1'):
                    ability1 = "Energy Ball"
                elif (self.ability1.get()=='2'):
                    ability1 = "Dragon Breath"
                elif (self.ability1.get()=='3'):
                    ability1 = "Crown of Flame"
                elif (self.ability1.get()=='4'):
                    ability1 = "Hail Storm"
                    
                ability2 = ""
                if (self.ability2.get()=='1'):
                    ability2 = "Energy Ball"
                elif (self.ability2.get()=='2'):
                    ability2 = "Dragon Breath"
                elif (self.ability2.get()=='3'):
                    ability2 = "Crown of Flame"
                elif (self.ability2.get()=='4'):
                    ability2 = "Hail Storm"

                ability3 = ""
                if (self.ability3.get()=='1'):
                    ability3 = "Energy Ball"
                elif (self.ability3.get()=='2'):
                    ability3 = "Dragon Breath"
                elif (self.ability3.get()=='3'):
                    ability3 = "Crown of Flame"
                elif (self.ability3.get()=='4'):
                    ability3 = "Hail Storm"

            if (self.rb1.get()==2):
                ability1 = ""
                if (self.ability1.get()=='1'):
                    ability1 = "Fire Splash"
                elif (self.ability1.get()=='2'):
                    ability1 = "Power Splash"
                elif (self.ability1.get()=='3'):
                    ability1 = "Gigantic Storm"
                elif (self.ability1.get()=='4'):
                    ability1 = "Chaotic Disaster"
                    
                ability2 = ""
                if (self.ability2.get()=='1'):
                    ability2 = "Fire Splash"
                elif (self.ability2.get()=='2'):
                    ability2 = "Power Splash"
                elif (self.ability2.get()=='3'):
                    ability2 = "Gigantic Storm"
                elif (self.ability2.get()=='4'):
                    ability2 = "Chaotic Disaster"

                ability3 = ""
                if (self.ability3.get()=='1'):
                    ability3 = "Fire Splash"
                elif (self.ability3.get()=='2'):
                    ability3 = "Power Splash"
                elif (self.ability3.get()=='3'):
                    ability3 = "Gigantic Storm"
                elif (self.ability3.get()=='4'):
                    ability3 = "Chaotic Disaster"

            if (self.rb1.get()==3):
                ability1 = ""
                if (self.ability1.get()=='1'):
                    ability1 = "Take Aim"
                elif (self.ability1.get()=='2'):
                    ability1 = "Quick Shot"
                elif (self.ability1.get()=='3'):
                    ability1 = "Blazing Arrow"
                elif (self.ability1.get()=='4'):
                    ability1 = "Frost Arrow"
                    
                ability2 = ""
                if (self.ability2.get()=='1'):
                    ability2 = "Take Aim"
                elif (self.ability2.get()=='2'):
                    ability2 = "Quick Shot"
                elif (self.ability2.get()=='3'):
                    ability2 = "Blazing Arrow"
                elif (self.ability2.get()=='4'):
                    ability2 = "Frost Arrow"

                ability3 = ""
                if (self.ability3.get()=='1'):
                    ability3 = "Take Aim"
                elif (self.ability3.get()=='2'):
                    ability3 = "Quick Shot"
                elif (self.ability3.get()=='3'):
                    ability3 = "Blazing Arrow"
                elif (self.ability3.get()=='4'):
                    ability3 = "Frost Arrow"

            if (self.rb1.get()==4):
                ability1 = ""
                if (self.ability1.get()=='1'):
                    ability1 = "Cloaking"
                elif (self.ability1.get()=='2'):
                    ability1 = "Enchant Poison"
                elif (self.ability1.get()=='3'):
                    ability1 = "Sonic Acceleration"
                elif (self.ability1.get()=='4'):
                    ability1 = "Meteor Assault"
                    
                ability2 = ""
                if (self.ability2.get()=='1'):
                    ability2 = "Cloaking"
                elif (self.ability2.get()=='2'):
                    ability2 = "Enchant Poison"
                elif (self.ability2.get()=='3'):
                    ability2 = "Sonic Acceleration"
                elif (self.ability2.get()=='4'):
                    ability2 = "Mateor Assault"

                ability3 = ""
                if (self.ability3.get()=='1'):
                    ability3 = "Cloaking"
                elif (self.ability3.get()=='2'):
                    ability3 = "Enchant Poison"
                elif (self.ability3.get()=='3'):
                    ability3 = "Sonic Acceleration"
                elif (self.ability3.get()=='4'):
                    ability3 = "Meteor Assault"
        
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid message.")

        messagebox.showinfo("Character Succesfully Created", f"Congratulations!\n\nRole: {role}\n\n Weapon: {weapon}\n\n Abilities:\n     {ability1}\n     {ability2}\n     {ability3}")

def main():

    GAME().mainloop()
main()