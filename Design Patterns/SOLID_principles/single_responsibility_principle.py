# SRP- Single Responsibility Principle states that:- A class should have only one reason to change
# This mean that a class should have only one responsibility, as expressed through its methods. If a class takes care of
# more than one tasks, then you should separate those tasks into separate classes.

# this principle is closely related to the concept of separation of concerns, which suggests that you should split your
# program into different sections. Each section must address a separate concern

# Example

from pathlib import Path
from zipfile import ZipFile


class FileManager:
    def __int__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        return self.path.write_text(data, encoding)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()


# this class violates the single-responsibility principle because it has two reason for changing its internal implementation.
# to fix this issue and make you design more robust, you can split the class into two smaller, more focused classes,
# each with its own specific concern:

class FileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def read(self, encoding="utf-8"):
        return self.path.read_text(encoding)

    def write(self, data, encoding="utf-8"):
        self.path.write_text(data, encoding)


class ZipFileManager:
    def __init__(self, filename):
        self.path = Path(filename)

    def compress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="w") as archive:
            archive.write(self.path)

    def decompress(self):
        with ZipFile(self.path.with_suffix(".zip"), mode="r") as archive:
            archive.extractall()
