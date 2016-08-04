#Run from this file and see the difference
import Func1

if __name__ == '__main__':
    print ("1: Execute the file itself as = " + __name__ )
    Func1.f1()
else:
    print ("2: called from other file named as " + __name__ )
    Func1.f1()
