from Parser import parse
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

if __name__ == '__main__':
    x=Launch()
    # x.Label(ParsedFile['html']['body'][0]['text'][0]['_text'])
    for i in ParsedFile['html']['body']:
        for z in i['text']:
            x.Label(z['_text'])
    x.Execute()

