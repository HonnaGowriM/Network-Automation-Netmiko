import sshInfo

class Validate():

    def __init__(self,IP):
        self.IP_LIST=IP
        self.validip=[]

    def checkip(self):
        #print(self.IP_LIST)
        for i in self.IP_LIST:
            #print("loop start")
            #print(i)
            res=self.testing(i)
            #print res

    def testing(self,err):
        #self.i=err
        test=err.split(".")
        n=0
        False_Flag=False

        if len(test)!= 4:
            False_Flag=True
        for loop in test:
            if int(loop)>256 or int(loop)<0:
                False_Flag=True
                break

        if False_Flag == True:
            return("Invalid IP "+ err)
        else:
            self.validip.append(err)
            return("Valid IP " + err)

    def getValidIP(self):
        return self.validip


'''

if __name__=='__main__':
    filename='sshinfo.csv'
    Start=sshInfo.verification(filename)
    IP=Start.getIPlist()
    val=Validate(IP)
    val.checkip()
'''
