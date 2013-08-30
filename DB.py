

def getOdbcCursor(driverStr, hostStr, uidStr, pwdStr, dbStr):
    import pyodbc
    cnxn = pyodbc.connect(driver=driverStr, server=hostStr, datbase=dbStr, uid=uidStr, pwd=pwdStr)
    return cnxn.cursor()

def getMySqlCursor(hostStr,uidStr,pwdStr,dbStr):
    import MySQLdb
    db = MySQLdb.connect(host = hostStr, user = uidStr, passwd = pwdStr, db = dbStr)
    return db.cursor()


