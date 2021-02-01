from parser_main import parse
import tkinter as tk
ParsedFile=parse('thefile.html')
methods=['text','button','input']
root_path=ParsedFile['html']['body']
class Launch():
    def __init__(self):
        try:
            ParsedFile['html']['body']
        except:
            exit("bruh please write html file properly")
        self.root = tk.Tk()
        try:
            self.root.title(ParsedFile['html']['head'][0]['title'][0]['_text'])
        except:
            self.root.title("Durk App")
        
        
    def Label(self, text):
        self.label=tk.Label(self.root,text=text)
        self.label.pack()

    def Button(self,text):
        self.button=tk.Button(self.root,text=text)
        self.button.pack()

    def Input(self,width=10):
        self.Input = tk.Entry(self.root,width=width)
        self.Input.pack()


    def Execute(self):
        self.root.mainloop()

    def Packer(self,Class):
            for tag in root_path:
                for key in tag.keys():
                    if key in methods:
                        Check(key,Class)
            Class.Execute()

def Check(string,Class):
    if string=="text":
        for component in root_path:
            # print(component)
            for x in component[string]:
                Class.Label(x['_text'])
    if string=="button":
        for component in root_path:
            for x in component[string]:
                Class.Button(x['_text'])
    if string=="input":
        for component in root_path:
            for x in component[string]:
                Class.Input()
        # Class.Execute()
if __name__ == '__main__':
    x=Launch()
    # x.Label(ParsedFile['html']['body'][0]['text'][0]['_text'])
    x.Packer(x)

    # for i in ParsedFile['html']['body']:
    #     for z in i['text']:
    #         x.Label(z['_text'])
    # x.Execute()

