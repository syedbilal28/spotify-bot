
class Account:
    def __init__(self,email,password):
        self.email=email
        self.password=password
    def __str__(self):
        return self.email
class ChangeAccount:
    def __init__(self,old_account:Account,new_account:Account):
        self.current_account=old_account
        self.change_account=new_account

def CreateAccounts(accounts_file,to_change_file):
    accounts_file=open(accounts_file,"r")
    accounts_exist=accounts_file.readlines()
    old_accounts=[]
    for i in accounts_exist:
        temp=i.split(":")
        try:
            new_account=Account(temp[0],temp[1])
            old_accounts.append(new_account)
        except:
            pass
    accounts_file.close()

    change_file=open(to_change_file,"r")
    changes_exist=change_file.readlines()
    l=len(changes_exist)
    for i in range(l):
        changes_exist[i]=Account(changes_exist[i],None)
    change_file.close()
    
    to_change_accounts=[]
    for i in range(l):
        try:
            to_change_accounts.append(ChangeAccount(old_accounts[i],changes_exist[i]))
        except:
            pass
    
    return to_change_accounts

    

def get_proxies():
    infile=open("proxies.txt","r")
    content=infile.readlines()
    infile.close()
    proxies=[]
    for i in content:
        proxy=i.split(":")
        if len(proxy) >1:
            l=len(proxy)
            
            for j in range(l):
                
                proxy[j]=proxy[j].replace("\n","")
            
            proxies.append((proxy[0],int(proxy[1])))
    
    return proxies