import tkinter
# Let's create the Tkinter window
window = tkinter.Tk()
window.title("GUI")
window.geometry("600x400+300+300")
# You will create two text labels namely 'username' and 'password' and and two input labels for them



def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = tkinter.Button(window, text ="Hello", command = helloCallBack)

B.pack()
#B.place(bordermode=OUTSIDE, height=100, width=100)

window.mainloop()