from mysql_handle import mysql_handle
import time
def updata():
    f=open('db\\result.txt')
    all_line=(t.strip() for t in f)
    new=mysql_handle('localhost','root','','urldata')
    if(new.mysql_connect()):
        new.mysql_cursor()
        #new.mysql_construct_table()
        for i in all_line:
            data="insert into url (url,time) values('%s','%s')"%(i.strip(),time.strftime('%Y.%m.%d-%H.%M.%S'))
            new.mysql_query(data)

if __name__=="__main__":
    updata()