# a=[1,2,3,4,5,6]
# l=6
# for i in range(l):
#     a.pop(0)
#     print(a)

email="asb@gmail.com"
password="askfnoasnfo"
outfile=open("test.txt","a")
outfile.write(f"{email}:{password}")
outfile.close()