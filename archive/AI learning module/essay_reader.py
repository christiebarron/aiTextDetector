filename = input("Enter the name of the file: ")
try:
    with open(filename, "r") as file:
        contents = file.read()
        lines = contents.split('\n')
        num_lines = len(lines)
        num_words = sum(len(line.split()) for line in lines)
        print(f"The file '{filename}' has {num_lines} lines and {num_words} words.")
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
