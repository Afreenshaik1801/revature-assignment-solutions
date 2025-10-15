def read_last_n_lines(filename, n):
    try:
        with open(filename, 'r') as file:
            lines=file.readlines()
            last_lines=lines[-n:]
            return ''.join(last_lines)
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

filename = "sample.txt"
n=5  
print(read_last_n_lines(filename, n))
