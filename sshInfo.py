import sys
import os
import csv

class verification():

    def __init__(self,filename):
        self.filename=filename
        self.IP_LIST=[]
        self.USERNAME=[]
        self.PASSWORD=[]

        check = os.path.isfile(self.filename)
        #print(check)
        if check == True:
           self.readfile()
        else:
            print("Config file not present. Exiting the program.")
            sys.exit(1)

    def readfile(self):
        app=[]
        file= open(self.filename,'r')
        openfile=csv.reader(file)
        next(openfile) #Skips the first row
        for i in openfile:
            if i:
                self.IP_LIST.append(i[0])
                self.USERNAME.append(i[1])
                self.PASSWORD.append(i[2])
        #print("The IP's of the routers are: "+ str(self.IP_LIST))
        #print("The Username for SSH is: "+ str(self.USERNAME))
        #print("The Password for SSH is: "+ str(self.PASSWORD))

    def getIPlist(self):
        print self.IP_LIST
        return self.IP_LIST

    def getuser(self):
        print self.USERNAME
        return self.USERNAME

    def getpassword(self):
        print self.PASSWORD
        return self.PASSWORD



'''
if __name__=='__main__':
    filename='sshinfo.csv'
    check=verification(filename)
    check.getIPlist()
    check.getuser()
    check.getpassword()

'''
