# Python Writting files(.text,.json,.csv)

txt_data = "This is a sample text file.\nIt contains multiple lines of text.\nThis is the third line."

file_path = "output.txt"

with open(file_path, "w") as file: # a = append, w = write, r = read
    file.write(txt_data)
    print(f"Text data written to {file_path}")
    