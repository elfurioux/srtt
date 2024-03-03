from srtt import RESDIR,TRADDIR
import os

def rmfile(filename,path):
    p = os.path.join(path,filename)
    if not os.path.isfile(p): return

    os.remove(p)
    print("removed:",p)

def main():
    for file in os.listdir(RESDIR):
        rmfile(file,RESDIR)
    for file in os.listdir(TRADDIR):
        rmfile(file,TRADDIR)

if __name__=="__main__": main()
