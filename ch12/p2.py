account=[]
path=r"ch12\계좌.txt"
mode="r"
encoding="utf-8"

# with open(path,mode,encoding=encoding) as f:
#     for read in f.readlines():
#         account.append(read[-14:])

with open(path,mode,encoding=encoding) as f:
    lines= f.readlines()
    accountlist=[]
    for line in lines:
        linelist=line.split()
        accountlist.append(linelist[1])
print(accountlist)
# mode="a"
# with open(path,mode,encoding=encoding) as f:
#     f.writelines(account)
        
