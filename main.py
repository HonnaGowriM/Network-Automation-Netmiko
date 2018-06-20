import sshInfo
import validateIP
import connectivity
import bgp

filename='sshinfo.csv'
Handle1=sshInfo.verification(filename)
print("List of IP")
IP_list=Handle1.getIPlist()
print("*"*50)
print("User name List")
USER_list=Handle1.getuser()
print("*"*50)
print("Password list")
PASSWORD_list=Handle1.getpassword()
print("*"*50)


Handle2=validateIP.Validate(IP_list)
Handle2.checkip()
VALID_IPlist=Handle2.getValidIP()
print("Valid IP list")
print(VALID_IPlist)
print("*"*50)

Handle3=connectivity.Connectivity(VALID_IPlist)
print("Connectivity test results for valid Ip")
Handle3.connect()
print("*"*50)

Handle4=bgp.Classy(VALID_IPlist,USER_list,PASSWORD_list)
Handle4.start()
print("Neighbour output")
print("\n")
Handle4.FILE()
print("*"*50)


print("sh run output")
print("\n")
Handle4.RUN()
print("*"*50)


