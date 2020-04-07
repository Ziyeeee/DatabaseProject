import pymysql


# 查询直接领导为ENAME的员工编号
def Select1(cursor):
    sql = "SELECT essn FROM employee e1 WHERE e1.superssn = (SELECT essn FROM employee e2 WHERE e2.ename = "
    ename = input("直接领导姓名：")
    sql = sql + "\"" + ename + "\");"
    print(sql)
    try:
        cursor.execute(sql)
        print("直接领导为" + ename + "的员工编号:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询项目所在地为PLOCATION的部门名称
def Select2(cursor):
    sql = "SELECT dname FROM department WHERE department.dno in (SELECT dno FROM project WHERE project.plocation = "
    plocation = input("项目所在地：")
    sql = sql + "\"" + plocation + "\");"
    print(sql)
    try:
        cursor.execute(sql)
        print("项目所在地为" + plocation + "的部门名称:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询参与PNAME项目的所有工作人员的名字和居住地址
def Select3(cursor):
    sql = "SELECT ename, address FROM employee WHERE employee.essn in (SELECT essn FROM works_on WHERE works_on.pno = (SELECT pno FROM project WHERE project.pname = "
    pname = input("项目名：")
    sql = sql + "\"" + pname + "\"));"
    print(sql)
    try:
        cursor.execute(sql)
        print("参与" + pname + "项目的所有工作人员的名字和居住地址:")
        data = cursor.fetchall()
        for row in data:
            print(row[0] + "\t" + row[1])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询部门领导居住地在ADDRESS且工资不低于SALARY元的员工姓名和居住地
def Select4(cursor):
    sql = "SELECT ename, address FROM employee e1 WHERE e1.dno in (SELECT dno FROM department WHERE department.mgrssn in (SELECT essn FROM employee e2 WHERE e2.address like "
    address = input("部门领导居住地：")
    sql = sql + "\"%" + address + "%\")) and e1.salary >= "
    salary = input("最低工资：")
    sql = sql + "\"" + salary + "\";"
    print(sql)
    try:
        cursor.execute(sql)
        print("部门领导居住地在" + address + "且工资不低于" + salary + "元的员工姓名和居住地:")
        data = cursor.fetchall()
        for row in data:
            print(row[0] + "\t" + row[1])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询没有参加项目编号为PNO的项目的员工姓名
def Select5(cursor):
    sql = "SELECT ename FROM employee WHERE employee.essn not in (SELECT essn FROM works_on WHERE works_on.pno = "
    pno = input("项目编号：")
    sql = sql + "\"" + pno + "\");"
    print(sql)
    try:
        cursor.execute(sql)
        print("没有参加" + pno + "项目编号为PNO的项目的员工姓名:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询部门领导工作日期在MGRSTARTDATE之后的部门名
def Select6(cursor):
    sql = "SELECT dname FROM department WHERE date(mgrstartdate) > date("
    date = input("部门领导工作日期(YYYY-MM-DD)：")
    sql = sql + "\"" + date + "\");"
    print(sql)
    try:
        cursor.execute(sql)
        print("部门领导工作日期在" + date + "之后的部门名:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询总工作量大于HOURS小时的项目名称
def Select7(cursor):
    sql = "SELECT pname FROM project WHERE (SELECT sum(hours) FROM works_on WHERE works_on.pno = project.pno) > "
    hours = input("总工作量大于：")
    sql = sql + hours + ";"
    print(sql)
    try:
        cursor.execute(sql)
        print("总工作量大于" + hours + "小时的项目名称:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询员工平均工作时间低于HOURS小时的项目名称
def Select8(cursor):
    sql = "SELECT pname FROM project WHERE ((SELECT sum(hours) FROM works_on WHERE works_on.pno = project.pno) / (SELECT count(essn) FROM works_on WHERE works_on.pno = project.pno)) < "
    hours = input("员工平均工作时间低于：")
    sql = sql + hours + ";"
    print(sql)
    try:
        cursor.execute(sql)
        print("员工平均工作时间低于" + hours + "小时的项目名称:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 查询至少参与了N个项目并且工作总时间超过HOURS小时的员工名字
def Select9(cursor):
    sql = "SELECT ename FROM employee WHERE (SELECT count(pno) FROM works_on WHERE works_on.essn = employee.essn) >= "
    n = input("至少参与的项目数：")
    sql = sql + n + " and (SELECT sum(hours) FROM works_on WHERE works_on.essn = employee.essn) > "
    hours = input("工作总时间超过:")
    sql = sql + hours + ";"
    print(sql)
    try:
        cursor.execute(sql)
        print("查询至少参与了" + n + "个项目并且工作总时间超过" + hours + "小时的员工名字:")
        data = cursor.fetchall()
        for row in data:
            print(row[0])
        print("共" + str(len(data)) + "条")
    except:
        print("Error in \"" + sql + "\"")


# 在employee表新增记录1条记录；
def Insert(db, cursor):
    sql = "insert into employee(essn, ename, address, salary, superssn, dno) "
    essn = input("员工编号：")
    ename = input("员工姓名：")
    address = input("员工地址：")
    salary = input("员工工资：")
    superssn = input("员工直接领导：")
    dno = input("员工所在部门编号：")
    sql = sql + "value(\'" + essn + "\', \'" + ename + "\', \'" + address + "\', " + salary + ", \'" + superssn + "\', \'" + dno + "\');"
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("已提交编号为" + essn + "的员工信息")
    except:
        print("Error in \"" + sql + "\"")
        db.rollback()


# 更新员工信息
def Update(db, cursor):
    running = True
    essn = input("需更改信息的员工编号：")
    print("--------------------------------")
    print("请选择需要修改的信息：\n"
          "1.员工姓名\n"
          "2.员工地址\n"
          "3.员工工资\n"
          "4.员工直接领导\n"
          "5.员工所在部门编号\n"
          "6.退出")
    print("--------------------------------")
    choose = input()
    while running:
        sql = "UPDATE employee "
        if choose == "1":
            ename = input("请输入新的员工姓名：")
            sql = sql + "set ename = \'" + ename + "\' "
            break
        elif choose == "2":
            address = input("请输入新的员工地址：")
            sql = sql + "set address = \'" + address + "\' "
            break
        elif choose == "3":
            salary = input("请输入新的员工工资：")
            sql = sql + "set salary = " + salary + " "
            break
        elif choose == "4":
            superssn = input("请输入新的员工直接领导：")
            sql = sql + "set superssn = \'" + superssn + "\' "
            break
        elif choose == "5":
            dno = input("请输入新的员工所在部门编号：")
            sql = sql + "set dno = \'" + dno + "\' "
            break
        elif choose == "6":
            running = False
        else:
            continue
    if running == True:
        sql = sql + "WHERE essn = \'" + essn + "\';"
        print(sql)
        try:
            cursor.execute(sql)
            db.commit()
            print("已更新编号为" + essn + "的员工信息")
        except:
            print("Error in \"" + sql + "\"")
            db.rollback()


# 删除员工记录
def Delete(db, cursor):
    sql = "DELETE FROM employee WHERE essn = "
    essn = input("要删除的员工编号：")
    sql = sql + "\'" + essn + "\';"
    print(sql)
    try:
        cursor.execute(sql)
        db.commit()
        print("已删除编号为" + essn + "的员工信息")
    except:
        print("Error in \"" + sql + "\"")
        db.rollback()


def main():

    db = pymysql.connect("******", "******", "******", "******")
    cursor = db.cursor()

    running = True
    runningSub = True
    while running:
        print("--------------------------------")
        print("1.查询\n2.增添\n3.更新\n4.删除\n5.退出")
        print("--------------------------------")
        chooseFunction = input()
        if chooseFunction == "1":
            while runningSub:
                print("-----------------------------------------------------------------------------")
                print("1.查询直接领导为ENAME的员工编号\n"
                      "2.查询项目所在地为PLOCATION的部门名称\n"
                      "3.查询参与PNAME项目的所有工作人员的名字和居住地址\n"
                      "4.查询部门领导居住地在ADDRESS且工资不低于SALARY元的员工姓名和居住地\n"
                      "5.查询没有参加项目编号为PNO的项目的员工姓名\n"
                      "6.查询部门领导工作日期在MGRSTARTDATE之后的部门名\n"
                      "7.查询总工作量大于HOURS小时的项目名称\n"
                      "8.查询员工平均工作时间低于HOURS的项目名称\n"
                      "9.查询至少参与了N个项目并且工作总时间超过HOURS小时的员工名字\n"
                      "10.退出")
                print("-----------------------------------------------------------------------------")
                chooseSubFunction = input()
                if chooseSubFunction == "1":
                    Select1(cursor)
                elif chooseSubFunction == "2":
                    Select2(cursor)
                elif chooseSubFunction == "3":
                    Select3(cursor)
                elif chooseSubFunction == "4":
                    Select4(cursor)
                elif chooseSubFunction == "5":
                    Select5(cursor)
                elif chooseSubFunction == "6":
                    Select6(cursor)
                elif chooseSubFunction == "7":
                    Select7(cursor)
                elif chooseSubFunction == "8":
                    Select8(cursor)
                elif chooseSubFunction == "9":
                    Select9(cursor)
                elif chooseSubFunction == "10":
                    runningSub = False
                else:
                    continue
        elif chooseFunction == "2":
            print("--------------------------------")
            print("在employee表新增记录2条记录")
            print("--------------------------------")
            print("第一条记录：")
            Insert(db, cursor)
            print("--------------------------------")
            print("第二条记录：")
            Insert(db, cursor)
            print("--------------------------------")
        elif chooseFunction == "3":
            Update(db, cursor)
        elif chooseFunction == "4":
            Delete(db, cursor)
        elif chooseFunction == "5":
            running = False
        else:
            continue
    db.close()


main()
