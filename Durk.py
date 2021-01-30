from parser import parse
import tkinter as tk
ParsedFile=parse('thefile.html')

class Launch():
    def __init__(self):
        try:
            ParsedFile['html']['body']
        except:
            exit("bruh please write html file properly")
        self.root = tk.Tk()
    def Label(self, text):
        self.label=tk.Label(self.root,text=text)
        self.label.pack()

    def Execute(self):
        self.root.mainloop()




# a = tk.Label(root, text ="Hello World") 
# a.pack() 
  
# root.mainloop()

x=Launch()
x.Label(ParsedFile['html']['body'][0]['text'][0]['_text'])
x.Execute()

# print(ParsedFile['html']['body'][0]['text'][0]['_text'])