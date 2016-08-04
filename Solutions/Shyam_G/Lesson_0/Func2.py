#Run from this file and see the difference

def hello_world():
    print ("5: Inside the function hello_world ")
    if __name__ == '__main__':
        print ("6: Execute the file itself as  = " + __name__)
    else:
        print ("7: Imported this file inside other file and invoked from there ")
        print ("Current execution happen inside File  = " + __name__)



#Calling from the same file
if __name__ == '__main__':
    hello_world()

