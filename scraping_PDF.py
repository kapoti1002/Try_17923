import PyPDF2

# importing required modules 
import PyPDF2 
 
# creating a pdf file object 
pdfFileObj = open(r'C:\Users\sulagna.parida\Documents\Python_cheat_sheet_by_interviewbit_1668746971.pdf', 'rb') 
 
# creating a pdf reader object 
pdfReader = PyPDF2.PdfReader(pdfFileObj)
# creating a page object 
pageObj = pdfReader.read(0) 
 
# extracting text from page 
print(pageObj.extractText()) 
 
# closing the pdf file object 
pdfFileObj.close()