from tkinter import *
from tkinter import messagebox 
import customtkinter
import random
import numpy as np

root = customtkinter.CTk()

root.title('Farbige Boxen')

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
root.geometry("1300x720")
root.configure(bg='black')

color='red'

random_x = np.arange(0, 1291)
random_y = np.arange(0, 711)

def new_loc():
    button_1.place(x=random.choice(random_x), y=random.choice(random_y), height=10, width=10)
     
    
            
game_frame = customtkinter.CTkFrame(master=root,
                               width=1300,
                               height=800,
                               corner_radius=10,
                               bg='black',
                               fg_color='black',)


button_1 = customtkinter.CTkButton(root, command=new_loc, width=40,
                                height=20,
                                
                                text="",
                                fg_color=color,
                                text_font=('Times New Roman', 26),
                            bg_color='black',
                            hover_color=None
                                )




#Packing them on the screen

game_frame.place(x=0, y=0)

button_1.place(x=100, y=100, height=10, width=10)



root.mainloop()