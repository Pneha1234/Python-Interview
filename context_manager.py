with open("test.txt", "w") as f:
    f.write("Hello, World!")


class OpenFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()


# Example usage
with OpenFile("test.txt", "w") as f:
    f.write("Hello, World!")
    # The file will be automatically closed after this block

from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()

with open_file("test.txt", "w") as f:
    f.write("Hello, World!")
    # The file will be automatically closed after this block
