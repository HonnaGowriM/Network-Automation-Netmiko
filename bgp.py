import sshInfo
import validateIP
import connectivity
import configparser
from netmiko import ConnectHandler

class Classy():

    def __init__(self,validip,USERNAME,PASSWORD):
        self.validip=validip
        self.USERNAME=USERNAME
        self.PASSWORD=PASSWORD
        self.config=configparser.ConfigParser()
        self.config.read('bgp.conf')
        self.n=0
        self.R1={}
        self.R2={}
        self.command1=[]
        self.command2=[]
        self.L1=[]
        self.L2=[]
        self.COMMAND=[]


    def start(self):
        final_list=[]
        routers=self.config.sections()
        for router in routers:
            if router:
                test={}
                for key in self.config[router]:
                    test[key]=self.config[router][key]
                final_list.append(test)
        self.R1={}
        self.R2={}
        self.R1=final_list[0].copy()
        self.R2=final_list[1].copy()
        #print(self.R1)
        #print(self.R2)
        #print(self.R1['networklisttoadvertise'])
        self.L1=self.R1['networklisttoadvertise'].split(",")
        self.L2=self.R2['networklisttoadvertise'].split(",")

        self.command1=['router bgp '+str(self.R1['localas_number']),
            'network '+str(self.L1[0]) +' mask 255.255.255.0',
            'network '+str(self.L1[1]) +' mask 255.255.255.0',
            'neighbor '+str(self.validip[1])+' remote-as '+ str(self.R1['neighborremoteas'])]
        self.command2=['router bgp '+str(self.R2['localas_number']),
            'network '+str(self.L2[0]) +' mask 255.255.255.0',
            'network '+str(self.L2[1]) +' mask 255.255.255.0',
            'neighbor '+str(self.validip[0])+' remote-as '+ str(self.R2['neighborremoteas'])]

        print("COnfiguration of R1")
        print(self.command1)
        print("*"*50)
        print("COnfiguration of R2")
        print(self.command2)
        print("*"*50)
        self.COMMAND.append(self.command1)
        self.COMMAND.append(self.command2)
        #print(self.COMMAND)
        self.SSH(self.COMMAND)

    def SSH(self,COMMAND):
        n=0
        for num,name,pwd in zip(self.validip,self.USERNAME,self.PASSWORD):
            if num:
                CISCO_ROUTER={
                    'device_type':'cisco_ios',
                    'ip':num,
                    'username':name,
                    'password':pwd,
                     }

                #print(CISCO_ROUTER)
                conn=ConnectHandler(**CISCO_ROUTER)
                output = conn.send_config_set(COMMAND[n])
                out=conn.send_command("show ip bgp neigh")
                if "% Invalid input" in out:
                    print("COMMAND ENTERTED NEEDS TO BE VERIFIED. KINDLY RE-ENTER THE RIGHT COMMAND.")
                else:
                    #print(out)
                    openhandle=open('bgpout.txt','a')
                    openhandle.write(out)
                    openhandle.write("\n")
                    openhandle.write("*"*50)
                    openhandle.write("\n")
                    openhandle.close()
                n=n+1
                #print("*"*50)

    def FILE(self):
        BGP=[]
        STATE=[]
        file=open('bgpout.txt','r')
        handle=file.readlines()
        for i in handle:
            if i:
                if "BGP neighbor" in i:
                    BGP.append(i)
                if "BGP state" in i:
                    STATE.append(i)
        AS=[]
        Neig=[]
        for i in BGP:
            BGP_FINAL=i.split(",")
            for i in BGP_FINAL:
                #print(i)
                if"BGP neighbor" in i:
                    Neig.append(i.split()[3])
                if "remote AS" in i:
                    AS.append(i.split()[2])
        #print(Neig)
        #print(AS)

        BGPSTATE=[]
        for i in STATE:
            BGPTATE=i.split(",")
            for i in BGPTATE:
                #print(i)
                if "BGP state" in i:
                    BGPSTATE.append(i.split("=")[1])
        #print(BGPSTATE)
        print("RESULTS FOR R1")
        print("*"*70)
        print ("BGP Neighbor IP" +'      '+  "BGP Neighbor AS" + '              ' + "BGP Neighbor State" )
        print("*"*70)
        print(str(Neig[0]) +'             '+ str(AS[0])  + '                ' +  str(BGPSTATE[0]))
        print("\n")

        print("RESULTS FOR R2")
        print("*"*70)
        print ("BGP Neighbor IP" +'      '+  "BGP Neighbor AS" + '              ' + "BGP Neighbor State" )
        print("*"*70)
        print(str(Neig[1]) +'             '+ str(AS[1])  + '                ' +  str(BGPSTATE[1]))
        print("\n")

    def RUN(self):
        n=0
        for num,name,pwd in zip(self.validip,self.USERNAME,self.PASSWORD):
            if num:
                CISCO_ROUTER={
                    'device_type':'cisco_ios',
                    'ip':num,
                    'username':name,
                    'password':pwd,
                     }

                #print(CISCO_ROUTER)
                conn=ConnectHandler(**CISCO_ROUTER)
                out=conn.send_command("show run")
                #print(out)
                openhandle=open('showrun.txt','a')
                openhandle.write(out)
                openhandle.write("*"*50)
                openhandle.write("\n")
                openhandle.close()
        print(" The show run of both the routers is saved in the name showrun.txt")

'''
if __name__=='__main__':

    filename='sshinfo.csv'
    Start=sshInfo.verification(filename)
    IP=Start.getIPlist()
    val=validateIP.Validate(IP)
    val.checkip()
    lst1 = val.getValidIP()
    user=Start.getuser()
    pswd=Start.getpassword()
    Check=Classy(lst1,user,pswd)
    #Check.start()
    Check.RUN()
'''
