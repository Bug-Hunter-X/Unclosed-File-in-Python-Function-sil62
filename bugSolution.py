def function_with_closed_file(filename):
    try:
        with open(filename, 'r') as f:
            # ... some code that processes the file ... 
            return some_value
    except FileNotFoundError:
        return None # Handle cases where the file might not exist