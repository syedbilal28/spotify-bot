
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
        new_account=Account(temp[0],temp[1])
        old_accounts.append(new_account)
    accounts_file.close()

    change_file=open(to_change_file,"r")
    changes_exist=change_file.readlines()
    l=len(changes_exist)
    for i in range(l):
        changes_exist[i]=Account(changes_exist[i],None)
    change_file.close()
    print(len(old_accounts),len(changes_exist))
    to_change_accounts=[]
    for i in range(l):
        to_change_accounts.append(ChangeAccount(old_accounts[i],changes_exist[i]))
    print(len(old_accounts))
    print(len(changes_exist))
    return to_change_accounts

    print(len(to_change_accounts))

