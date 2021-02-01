from parser_main import parse
import tkinter as tk
from tkinter.ttk import Combobox

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

    def Comboboxx(self,values, current=None):
        self.Combobox=Combobox(self.root)
        self.Combobox['values']=values
        self.Combobox.current(current)
        self.Combobox.pack()


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
    elif string=="button":
        for component in root_path:
            for x in component[string]:
                Class.Button(x['_text'])
    elif string=="input":
        for component in root_path:
            for x in component[string]:
                if "type" in x: #type checking
                    if x["type"]=="combobox":
                        temp_list=[]
                        for z in x['option']:
                            print(z)
                                
                            temp_list.append(z['value'])
                        Combobo=Class.Comboboxx(temp_list)
                        break
                Class.Input()
if __name__ == '__main__':
    x=Launch()
    x.Packer(x)

