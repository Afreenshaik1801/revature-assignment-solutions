def count_lines_in_file(filename):
    try:
        with open(filename, 'r') as file:
            count=sum(1 for line in file)
        return count
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

filename="example.txt"
print("Number of lines:", count_lines_in_file(filename))