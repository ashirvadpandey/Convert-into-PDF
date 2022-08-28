import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
import aspose.words as aw
root = tk.Tk()
root.geometry("750x250")
root.title("pdf convertor")


def UploadAction(event=None):
  global filename
  filename = filedialog.askopenfilename()
  print('Selected:', filename)


def convert(event=None):
  #if (filename.endwith(".doc") or filename.endwith(".docx")):  #  for multiple types of file
  doc = aw.Document(filename)

  # Save as PDF
  doc.save("PDF.pdf")
  print("done")
  import tkinter.messagebox
  tkinter.messagebox.showinfo('Conversion completed','File saved')
  root.mainloop()
  

#Create a button
button = tk.Button(root, text='convert', command=convert)
button.place(x=225, y=125)
button = tk.Button(root, text='Choose the file', command=UploadAction)
button.place(x=325, y=125)

root.mainloop()

# have to add in application
from fpdf import FPDF 
import  jpype     
jpype.startJVM() 
from asposecells.api import Workbook
import aspose.words as aw
 #======csv and txt to pdf
 
pdf = FPDF() 
 
pdf.add_page() 
pdf.set_font("Arial", size = 25) 
file = open("INputfile.csv", "r")                   # Insert a cse or txt file
for g in file: 
    pdf.cell(200, 10, txt = g, ln = 1, align = 'C') 
pdf.output("Outputfile.pdf")                        #Save the file

####======Doc file to pdf

pdf = FPDF() 
pdf.add_page() 
pdf.set_font("Arial", size = 25) 
file = open("Insert file", "r")                     #insert the doc or docx file
for g in file: 
    pdf.cell(200, 10, txt = g, ln = 1, align = 'C') 
pdf.output("PDF.pdf")                               #Save the file


 #========excel to pdf

workbook = Workbook("Insertfile")                   #insert Excel file
workbook.save("Output.pdf")                         # Save the file
jpype.shutdownJVM()
