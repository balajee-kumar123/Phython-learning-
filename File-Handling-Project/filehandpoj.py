# crud
from pathlib import Path
def createfile():
    try:
        filename = input("enter your file name with extension " + "Example = hello.txt")
        path1= Path(filename)
        if  not path1.exists():
            with open(filename,"w") as c:
                data = input("Write what you want in your file: \n ")
                c.write(data)
            print("File is creted sucessfully")
        else:
            print("file already existed")
    except Exception as err:
        print(f"an error occured {err}")

def readfile():
    try:
        filename = input("enter your file name with extension and File must existed " + "Example = hello.txt \n")

        with open(filename,"r") as r:
            data = r.read()
            print(data)
    except Exception as err:
        print(f"an error occured {err}")

def updatefile():
    try:
        filename = input("enter your file name with extension " + "Example = hello.txt \n")
        with open(filename,"a") as u:
            data = input("update your file: ")
            u.write(data)
    except Exception as err:
        print(f"an error occured {err}")

def deletefile():
    filename = input("enter your file name with extension " + 'Example "hello.txt"\n')
    path = Path(filename)
    if path.exists:
        path.unlink()
        print("file deleted successfully")
    elif not path.exists(filename):
        print("file is not existed \n")
        with open(filename,"w") as f:
            f.write("File is created, write what you want \n")
        
        

print("Press 1 for Creating file:")
print("Press 2 for Reading file:")
print("Press 3 for Updating file:")
print("Press 4 for Deleting file:")

r = int(input("Enter your response: "))
if r == 1:
    createfile()
if r == 2:
    readfile()
if r == 3:
    updatefile()
if r == 4:
    deletefile()        


