#Run from this file and see the difference
import Func2

def f1():
    if __name__ == '__main__':
        print ("3: Execute the file itself as = " + __name__)
        Func2.hello_world()
    else:
        print ("4: Imported this file inside other file and invoked from there ")
        print ("Current execution happen inside File  = " + __name__)
        Func2.hello_world()



#Calling from the same file
if __name__ == '__main__':
    f1()