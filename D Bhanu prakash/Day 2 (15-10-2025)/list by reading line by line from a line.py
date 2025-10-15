def file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            lines=[line.strip() for line in file] 
        return lines
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

filename="example.txt"
lines_list=file_to_list(filename)
print(lines_list)