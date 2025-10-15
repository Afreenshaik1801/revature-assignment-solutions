def find_longest_words(filename):
    try:
        with open(filename, 'r') as file:
            words=file.read().split() 
        if not words:
            return "File is empty."
        max_length=max(len(word) for word in words)
        longest_words=[word for word in words if len(word)==max_length]
        return longest_words
    except FileNotFoundError:
        return "Error: File not found."
    except Exception as e:
        return f"Error: {e}"

filename = "example.txt"
print("Longest word(s):", find_longest_words(filename))