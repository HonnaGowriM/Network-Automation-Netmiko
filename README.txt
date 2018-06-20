The classes imported to the main program are explained below

*********sshInfo.py*********
> This class checks for the configuration file.
> Gets a list of IP's, username and passsword from the config file.

*********ValidateIP.py*********
> This program imports sshInfo class
> The program validates the IPV4 address that has been extracted from the configuration file.

*********Connectivity.py*********
> This program imports both sshInfo and validateIP class
> The program checks the rechability of the IP by initiating PING and prints out the results.

*********BGP.py*********
> This program imports sshInfo, ValidateIP, Connectivity class
> The program configures the routers using netmiko

*********Main.py*********
> This program imports all of the above class
> This program is used to evoke the rest of the classes in the program
