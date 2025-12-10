file_name = input("Enter file: ")

if file_name.endswith((".pdf",".txt",".docx")):
    print(True)
else:
    print(False)