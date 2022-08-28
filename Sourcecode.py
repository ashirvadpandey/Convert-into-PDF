
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

#===============doc to pdf

doc = aw.Document("Insertfile")                      #Insert the doc or docx file
doc.save("PDF.pdf")                                  # Save the file
