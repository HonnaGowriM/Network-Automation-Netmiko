import sshInfo
import validateIP
import os

class Connectivity():

    def __init__(self,validip):
        self.validip=validip
        #self.ssh()

    def connect(self):
        for Ips in self.validip:
            a=os.system("ping -c 2 "+ Ips + '>> ping.txt')
            if a==0:
                print(str(Ips)+ " is reachable")
            else:
                print(str(Ips)+ " is unreachable")

'''
if __name__=='__main__':
    filename='sshinfo.csv'
    Start=sshInfo.verification(filename)
    IP=Start.getIPlist()
    val=validateIP.Validate(IP)
    val.checkip()
    lst1 = val.getValidIP()
    calling=Connectivity(lst1)
    calling.connect()
'''
