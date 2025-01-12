def function_with_closed_file(filename):
    with open(filename, 'r') as f:
        # ... some code that processes the file ... 
        contents = f.read()
        # File is automatically closed when exiting the 'with' block
    return contents