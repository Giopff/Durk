try:
    import tkcalendar as tkc
except:
    pass
try:
    from PIL import ImageTk, Image
except:
    pass
from os import error
from parser_main import parse
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile 
from parser_main import orderify
from parser_main import parse_order


order=lambda name:orderify(parse_order(name),parse(name))
ParsedFile=parse('thefile.html')
methods=['text','button','input','image','img']
root_path=ParsedFile['html']['body']
root_path_real=order('thefile.html')
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
        # self.x1 = self.Input.get()
        # return self.x1

    def Comboboxx(self,values, current=None):
        self.Combobox=ttk.Combobox(self.root)
        self.Combobox['values']=values
        self.Combobox.current(current)
        self.Combobox.pack()

    def Checkbox(self,text):
        CBvar = tk.IntVar()
        CB = tk.Checkbutton(self.root, text=text,variable=CBvar, onvalue=1, offvalue=0)
        CB.pack()

    def Radio(self,text):
        R= tk.IntVar()
        RB = tk.Radiobutton(self.root, text=text, variable=R, value=1)
        RB.pack()

    def Date(self,text="Pick date"):
        # self.top = tk.Toplevel(self.root)

        # ttk.Label(self.top, text=text).pack() if you want some popup than this is a good option. i am gonna implement this feature soon
        try:
            self.cal = tkc.DateEntry() #top, width=12, background='darkblue', foreground='white', borderwidth=2 RANDOM PARAMEteRS LOL
        except NameError:
            exit("install the 'tkcalendar' library (pip install tkcalendar)")
        except ModuleNotFoundError:
            exit("install the 'tkcalendar' library (pip install tkcalendar)")
        self.cal.pack()

    def OpenFile(self):
        def open_file(): 
            file = askopenfile(mode ='r', filetypes =[('Python Files', '*.py')]) 
            if file is not None: 
                content = file.read()
  
        btn = tk.Button(self.root, text ='Open', command = lambda:open_file()) 
        btn.pack()

    def Image(self,path):
        try:
            
            self.img = ImageTk.PhotoImage(Image.open(path))

        except NameError:
            exit("install the 'PIL' library (pip install Pillow)")
        except ModuleNotFoundError:
            exit("install the 'PIL' library (pip install Pillow)")
        except:
            print(error)
        self.panel = tk.Label(self.root,image=self.img)
        self.panel.image=self.img
        self.panel.pack()

    def Execute(self):
        self.root.mainloop()

    def Packer(self,Class):
            for tag in root_path_real:
                for key in tag.keys():
                    if key in methods:
                        Check(key,Class,tag[key])
            Class.Execute()

def Check(string,Class,x):
    if string=="text":
        Class.Label(x['_text'])
    elif string=="button":
        Class.Button(x['_text'])
    elif string=="input":
        if "type" in x: #type checking
            # print(x)
            # email check if '@' not in email and '.' not in email:
            
            if x["type"]=="combobox":
                temp_list=[]
                for z in x['option']:
                        
                    temp_list.append(z['value'])
                Class.Comboboxx(temp_list)
                pass
                # continue
            elif x["type"]=="checkbox":

                for z in x['option']:

                    Class.Checkbox(z['value'])
                pass
                # continue
            elif x["type"]=="radio":

                for z in x['option']:

                    Class.Radio(z['value'])
                pass
                # continue
            elif x["type"]=="date":
                try:
                    Class.Date("bruh")
                except ModuleNotFoundError:
                    exit("install the 'tkcalendar' library (pip install tkcalendar)")
                pass
                # continue
            elif x["type"]=="file":
                Class.OpenFile()
                pass
                # continue 
                 
            
        Class.Input()
    elif string=="image" or string=="img":
        try:
            Class.Image(x["path"])
        except ModuleNotFoundError:
            exit("install the 'PIL' library (pip install Pillow)")
        
        

if __name__ == '__main__':
    x=Launch()
    x.Packer(x)

