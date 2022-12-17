import pymysql  # 一种写好的库，可自己pip安装，类似的库很多可以自行查找
import os
def menu_1():
    print("1.INSERT")
    print("2.SELECT")
    print("3.SELECTALL")
    print("4.DELET")
    print("5.Update")
    print("6.CLS")
    print("0.QUIT")

def menu_2():
    print("1.CREATE TABLE")
    print("2.DROP TABLE")
    print("3.OPERATE")
    print("4.INNER JOIN")
    print("5.LEFT JOIN")
    print("6.CLS")
    print("0.QUIT")

def my_create(table,style):
    # 这是在执行sql语句，execute里面的为删除数据表的语句
    sql1 = """DROP TABLE IF EXISTS {table}""".format(table=table)
    try:
        cursor.execute(sql1)
        db.commit()
    except:
        db.rollback()
    # 创建表的sql语句
    create_table_sql1 = """CREATE TABLE {table}(NAME  VARCHAR(20) NOT NULL,AGE INT )""".format(table=table)
    create_table_sql2 = """CREATE TABLE {table}(NAME  VARCHAR(20) NOT NULL,SUBJECT  VARCHAR(20) NOT NULL,SCORE INT )""".format(table=table)
    try:
        if style=='1':
            cursor.execute(create_table_sql1)
        elif style=='2':
            cursor.execute(create_table_sql2)
        db.commit()
    except:
        db.rollback()

def my_drop(table):
    drop_sql = """DROP TABLE IF EXISTS {table}""".format(table=table)
    try:
        cursor.execute(drop_sql)
        db.commit();
    except:
        db.rollback()

def my_INSERT(table,style,a,b,c=0):
    insert_sql1 = """Insert Into {table}(NAME,AGE)VALUES(%s,%s)""".format(table=table)
    insert_sql2 = """Insert Into {table}(NAME,SUBJECT,SCORE)VALUES(%s,%s,%s)""".format(table=table)
    try:
        if style=='1':
            cursor.execute(insert_sql1,(a,b))
        elif style=='2':
            cursor.execute(insert_sql2,(a,b,c))
        db.commit();
    except:
        db.rollback()

def my_select(a,table):
    select_sql =""" SELECT DISTINCT * from {table} WHERE name=%s""".format(table=table)
    try:
        cursor.execute(select_sql,a)
        result=cursor.fetchone()
        print(result)
        db.commit()
        return result
    except:
        db.rollback()

def my_selectall(table):
    selectall_sql = """SELECT * FROM {table}""".format(table=table)
    try:
        cursor.execute(selectall_sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
        return result
    except:
        db.rollback()

def my_delet(a,table,s):
    delet_sql1 = """DELETE FROM {table} WHERE name=%s OR age=%s;""".format(table=table)
    delet_sql2 = """DELETE FROM {table} WHERE name=%s OR age=%s;""".format(table=table)
    try:
        if s == '1':
            cursor.execute(delet_sql1,(a,a))
        elif s == '2':
            cursor.execute(delet_sql2,(a,a))
        db.commit()
    except:
        db.rollback()

def my_update(n_name,n_age,o_name,table,o_age=0,n_subject=0,n_score=0):
    update_sql1 = """UPDATE {table} SET NAME=%s,AGE=%s WHERE NAME=%s AND AGE=%s""".format(table=table)
    update_sql2 = """UPDATE {table} SET NAME=%s,SUBJECT=%s,SCORE=%s WHERE NAME=%s """.format(table=table)
    try:
        if s == '1':
            cursor.execute(update_sql1,(n_name,n_age,o_name,o_age))
        elif s == '2':
            cursor.execute(update_sql2,(n_name,n_subject,n_score,o_name))
        db.commit()
    except:
        db.rollback()

def my_innerjoin(table1,table2):
    innerjoin_sql = """SELECT {table1}.name,age,subject,score FROM {table1} INNER JOIN {table2} ON {table1}.name = {table2}.name""".format(table1=table1,table2=table2)
    try:
        cursor.execute(innerjoin_sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except:
        db.rollback()

def my_leftjoin(table1,table2):
    leftjoin_sql = """SELECT table1.name,age,subject,score FROM {table1} LEFT JOIN {table2} ON {table1}.name={table2}.name""".format(table1=table1,table2=table2)
    try:
        cursor.execute(leftjoin_sql)
        result = cursor.fetchall()
        print(result)
        db.commit()
    except:
        db.rollback()

param = {
    'host': 'localhost',  # 本机
    'port': 3306,  # 端口号，一般mysql为3306
    'db': 'huawei',  # 数据库名
    'user': 'root',  # 登陆用户
    'password': '110120zzh',  # 登陆用户的密码
    'charset': 'utf8',  # 字符编码
}
db = pymysql.connect(**param)  # 建立连接对象
cursor = db.cursor()  # 使用cursor()方法创建一个游标对象cur（不理解没关系）

menu_2()
op = input("input:")
while( op != '0' ):
    if op == '1':
        a=input("input table name:")
        s=input("input style:")
        my_create(a,s)
    elif op=='2':
        a = input("input table name:")
        my_drop(a)
    elif op=='3':
        table = input("input table name:")
        s=input("input style:")
        menu_1()
        op = input("input:")
        while (op != '0'):
            if op == '1':
                if s=='1':
                    a = input("input name:")
                    b = input("input age:")
                    my_INSERT(table,s,a,b)
                elif s=='2':
                    a = input("input name:")
                    b = input("input subject:")
                    c = input("input score:")
                    my_INSERT(table,s,a,b,c)
            elif op == '2':
                a = input("input name:")
                my_select(a,table)
            elif op == '3':
                my_selectall(table)
            elif op == '4':
                a = input("input name or age:")
                my_delet(a,table)
            elif op == '5':
                if s=='1':
                    a = input("input n_name:")
                    b = input("input n_age:")
                    c = input("input o_name:")
                    d = input("input o_age:")
                    my_update(a, b, c,table,d)
                elif s=='2':
                    a = input("input n_name:")
                    b = input("input n_subject:")
                    d = input("input n_score:")
                    c = input("input o_name:")
                    my_update(a,0,c,table,0,b,d)
            elif op == '6':
                i = os.system("cls")
                menu_1()
            op = input("input order:")
    elif op=='4':
        a = input("input table1:")
        b = input("input table1:")
        my_innerjoin(a,b)
    elif op == '5':
        a = input("input table1:")
        b = input("input table1:")
        my_leftjoin(a, b)
    elif op=='6':
        i = os.system("cls")
        menu_2()
    op = input("input order:")
print("BYE!")
# 关闭数据库连接
db.close()
