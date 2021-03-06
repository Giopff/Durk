try:
    import tkcalendar as tkc
except:
    pass
try:
    from PIL import ImageTk, Image
except:
    pass
from os import error
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfile 
import xml.etree.ElementTree as ET

xmlTree = ET.parse('thefile.html')
ROOT=xmlTree.getroot()

methods=['text','button','input','image','img']
class Launch():
    def __init__(self):
        try:
            ROOT.findall("./body")
        except:
            exit("bruh please write html file properly")
        self.root = tk.Tk()
        try:
            for item in ROOT.findall("./head/*"):
                check_head(self.root,item)
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
            for item in ROOT.findall("./body/*"):
                Check(item.tag,Class,item.text,item.attrib,item)
            Class.Execute()

def Check(string,Class,text,attribs,Root):
    if string=="text":
        Class.Label(text)
    elif string=="button":
        Class.Button(text)
    elif string=="input":
        if "type" in attribs: #type checking
            # email check if '@' not in email and '.' not in email:
            
            if attribs["type"]=="combobox":
                temp_list=[]
                for z in Root.findall("./*"):
                        
                    temp_list.append(z.attrib['value'])
                Class.Comboboxx(temp_list)
                pass

            elif attribs["type"]=="checkbox":

                for z in Root.findall("./*"):

                    Class.Checkbox(z.attrib['value'])
                pass

            elif attribs["type"]=="radio":

                for z in Root.findall("./*"):

                    Class.Radio(z.attrib['value'])
                pass

            elif attribs["type"]=="date":
                try:
                    Class.Date("bruh")
                except ModuleNotFoundError:
                    exit("install the 'tkcalendar' library (pip install tkcalendar)")
                pass

            elif attribs["type"]=="file":
                Class.OpenFile()
                pass
 
                 
        else:
            Class.Input()
    elif string=="image" or string=="img":
        try:
            Class.Image(attribs["path"])
        except ModuleNotFoundError:
            exit("install the 'PIL' library (pip install Pillow)")
        
def check_head(root,tag):
    if tag.tag =="title":
        root.title(tag.text)


if __name__ == '__main__':
    x=Launch()
    x.Packer(x)

