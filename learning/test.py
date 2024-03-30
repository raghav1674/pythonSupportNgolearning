class MyFileContextManager():
    def __init__(self,file_name):
        self.file_name = file_name
        self.fp = None

    def __enter__(self):
        print(f"opening file {self.file_name}.....")
        self.fp = open(self.file_name,"w")
        return self.fp

    def __exit__(self, exception_type, exc_val, traceback):
        print(f"closing file {self.file_name}...")
        self.fp.close()

from contextlib import contextmanager

@contextmanager
def my_file_context_manager(file_name):
    fp = None
    try:
        print(f"opening file {file_name}.....")
        fp = open(file_name,"w")
        yield fp
    finally:
        print(f"closing file {file_name}...")
        fp.close()

with MyFileContextManager("abc.txt") as fp:
    fp.write("abc")
    print("Written to file")


with my_file_context_manager("xyz.txt") as fp:
    fp.write("xyz")
    print("Written to file")