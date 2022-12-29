from tkinter import *
import random
root = Tk()
root.title("TESTING RANDOM FUNCTION")
root.geometry("400x400")

enter_element = Entry(root)
enter_element.place(relx=0.5 , rely=0.3 , anchor=CENTER)

gpl = Label(root)
gdpl = Label(root)


    
a3d = [[["I" , "J" , "K" , "L" , "M" , "N" , "O" , "P"] , ["King" , "Queen"] , ["!", "@" , "#" , "$" , "%" , "^" , "&" , "*"]]]
  
print(a3d[0][2][4])
def np():

    random_no_1 = random.randint(0,7)
    random_no_2 = random.randint(0,1)
    random_no_3 = random.randint(0,7)
    
    letter_1 = str(a3d[0][0][random_no_1])
    letter_2 = str(a3d[0][1][random_no_2])
    letter_3 = str(a3d[0][2][random_no_3])
    gpl["text"] = "Guessed Password : " + enter_element.get()
    gdpl["text"] = "Generated password : " + letter_1 + "" + letter_2 + "" +  letter_3
   
    
btn = Button(root , text="New Password" , command=np)
enter_element.place(relx=0.5 , rely=0.3 , anchor=CENTER)
btn.place(relx=0.5 , rely=0.5 , anchor=CENTER)
gpl.place(relx=0.5 , rely=0.4 , anchor=CENTER)
gdpl.place(relx=0.5 , rely=0.6 , anchor=CENTER)
root.mainloop()