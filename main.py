import tkinter, PyPDF2
from tkinter import filedialog


def open_file():
    filename = filedialog.askopenfilename(title="Open PDF file",
                                          initialdir='/Users/sharmaaman030/Downloads',
                                          filetypes=[('PDF files', '*.pdf')])
    print(filename)

    filename_label.configure(text=filename)
    outputfile_text.delete("1.0", tkinter.END)
    reader = PyPDF2.PdfReader(filename)
    for i in range(len(reader.pages)):
        current_text = reader.pages[i].extract_text()
        outputfile_text.insert(tkinter.END, current_text)


root = tkinter.Tk()
root.title("PDF Text Extractor")

filename_label = tkinter.Label(root, text="No File Selected")
outputfile_text = tkinter.Text(root)
openfile_button = tkinter.Button(root, text="Open PDF File", command=open_file)

filename_label.pack()
outputfile_text.pack()
openfile_button.pack()

root.mainloop()