import ftplib

print '\t\t\t ######################################'
print '\t\t\t ##    Proudly Made By An INDIAN     ##'
print '\t\t\t ##   Author : Rohit Saxsena INDIA   ##'
print '\t\t\t ######################################'

def ftpLogin(hostName):
    try :
        ftp =  ftplib.FTP(hostName)
        ftp.login()
        print "\n\tAnonymous Login Sucessfully...!"
    except Exception,e :
        print "[-] Error :" ,e

host = raw_input("Enter Target IP :")
ftpLogin(host)
