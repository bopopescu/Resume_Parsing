from tkinter import *
from tkinter import filedialog as fd, ttk
from tkinter.ttk import *
import sys
import re
import codecs
from docx import *
from io import StringIO
def openFile(*args):
    filename = fd.askopenfilename()
    location = str(filename)
    document = Document(location)
    s = ""
    for paragraph in document.paragraphs:
        s += str(paragraph.text.encode(errors='ignore'))
    print(s)
    #print("\n")
    #Extract phone number
    regular_expression = re.compile(r"\(?"  # open parenthesis
                                    r"(\d{3})?"  # area code
                                    r"\)?"  # close parenthesis
                                    r"[\s\.-]{0,2}?"  # area code, phone separator
                                    r"(\d{3})"  # 3 digit exchange
                                    r"[\s\.-]{0,2}"  # separator bbetween 3 digit exchange, 4 digit local
                                    r"(\d{4})",  # 4 digit local
                                    re.IGNORECASE)
    result = re.search(regular_expression, s)
    if result:
        result = result.groups()
        result = "-".join(result)
    print(result)

    #Extract email
    regular_expression = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}", re.IGNORECASE)
    result = re.search(regular_expression, s)
    if result:
        result = result.group()
    print(result)

    #Extract skills------------
    #Use scikit learn library



def win_deleted():
    print("window closed ")
    root.destroy()
    sys.exit()

root = Tk()
root.title("Catering Analytics")

s = Style()
s.configure('My.TFrame', background='grey')


mainframe = ttk.Frame(root, padding="12 12 12 12",style='My.TFrame')
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
#mainframe.columnconfigure(0, weight=2)
#mainframe.rowconfigure(0, weight=2)
mainframe['borderwidth'] = 2
mainframe['relief'] = 'sunken'


ttk.Button(mainframe, text = "Open File" ,command = openFile).grid(column = 0,row = 2,columnspan=3,  padx = 3, pady = 3)

root.protocol("WM_DELETE_WINDOW", win_deleted)


root.mainloop()
