class FileManager:
    def __init__(self, filename, mode) -> None:
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        print('Opening file.')
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        print('Closing file.')
        # Handle exceptions if any
        if exc_type is not None:
            print(f'Exception: {exc_type}, {exc_val}')
        return True # Suppress exceptions
    

with FileManager('test.txt', 'w') as f:
    f.write('Hello, World!')
    raise Exception('Something went wrong!')
