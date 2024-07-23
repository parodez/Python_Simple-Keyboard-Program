from tkinter import *

class Window(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):
        self.master.title("My Keyboard")

        alphaUC = "QWERTYUIOPASDFGHJKLZXCVBNM"
        nums = "0123456789"

        self.btnAlpha = [None for _ in range(26)]
        self.btnNums = [None for _ in range(10)]

        frmAlpha = Frame(self)

        r = 0
        y = 0

        for i in range(26):
            self.btnAlpha[i] = Button(frmAlpha, text = alphaUC[i], font = "times 20 bold", width = 4, height = 1, command = lambda i = i:self.addChar(i))
            self.btnAlpha[i].grid(row = r, column = y)

            y+=1

            if i!= 0 and (i + 1) % 10 == 0:
                r+=1
                y = 0
                if r == 2:
                    y = 2

        frmNums = Frame(self)

        r = 0
        y = 0

        for i in range(10):
            self.btnNums[i] = Button(frmNums, text = nums[i], font = "times 20 bold", width = 4, height = 1, command = lambda i = i:self.addNum(i))
            self.btnNums[i].grid(row = r, column = y)

            y+=1
            
            if i == 7:
                r = 1
                y = 3
                
        btnClear = Button(frmNums, text = "CLEAR", font = "times 20 bold", width = 8, command = self.clearText)
        btnClear.grid(row = 1, column = y, columnspan = 2)
            
        self.lblResult = Label(self, relief = RIDGE, width = 70, height = 5, font = "times 15 bold", fg = "white", bg = "blue")

        frmAlpha.pack()
        frmNums.pack()
        self.lblResult.pack()
        self.pack()

    def addNum(self, i):
        newText = self.lblResult["text"] + self.btnNums[i]["text"]
        self.lblResult.config(text = newText)

    def addChar(self, i):
        newText = self.lblResult["text"] + self.btnAlpha[i]["text"]
        self.lblResult.config(text = newText)

    def clearText(self):
        self.lblResult.config(text = "")

root = Tk()
root.geometry("850x400")
app = Window(root)
root.mainloop()
