# -*- coding: UTF8 -*-
# read and write file

# read sql txt
import os

sql_path = r'd:\TEST\sql_collect\sql_file\sql_list.txt'
tree_path = r'd:\TEST\sql_collect\sql_file\tree_list.txt'

import control.database_base
from control import deligate

class getData:
    def __init__(self,):
        self.db = control.database_base.database()
        self.db.connect("192.168.8.18", port=35432, db_name='sql_collect')
        # self.getAllData()
        pass

    def getAllData(self):
        sql = '''
            select * from sql
            where del_flag != 1
        '''
        self.data = self.db.fetchall(sql)
        return self.data

    def getTreeDict(self):
        tree_dict = {}
        for list in self.data:
            if tree_dict.has_key(list[1])==False:
                tree_dict[list[1]] = {}
            if tree_dict[list[1]].has_key(list[2])==False:
                tree_dict[list[1]][list[2]] = {}
            if tree_dict[list[1]][list[2]].has_key(list[4]) == False:
                tree_dict[list[1]][list[2]][list[4]] = {}
            tree_dict[list[1]][list[2]][list[4]] = list[5]
        return tree_dict
        pass

    def getLevel1(self, n = 1):
        level = [sql[n] for sql in self.data]
        level = set(level)
        level = [i for i in level]
        return level

    def getLevel2(self, level_name):
        level = [sql[2] for sql in self.data if sql[1] == level_name]
        level = set(level)
        level = [i for i in level]
        return level

    def getLevel3(self, level1_name, level2_name):
        level = [sql[3] for sql in self.data if sql[1]==level1_name and sql[2]==level2_name]
        level = set(level)
        level = [i for i in level]
        return level

    def getName(self, level1_name, level2_name, level3_name):
        level = [sql[4] for sql in self.data if sql[1]==level1_name and sql[2]==level2_name and sql[3] in (level3_name,'0')]
        level = set(level)
        level = [i for i in level]
        return level


    def getSQLInfo(self, level1_name, level2_name, level3_name, name):
        sql = [sql for sql in self.data if
                 sql[1] == level1_name and sql[2] == level2_name and sql[3] in (level3_name, '0') and sql[4]==name]
        return sql[0][5],sql[0][6],sql[0][7]

    def insertSQL(self, level1, level2, level3, name, sql, comment='', fre=0):
        sql = self.changeCommon(sql)
        sql_cmd = '''
            insert into sql(level_1, level_2, level_3, name, sql, comment, frequency)
            select '%s', '%s', '%s', '%s', '%s', '%s', 0
        '''% (level1, level2, level3, name, sql, comment)
        print sql_cmd
        self.db.do_execute(sql_cmd)
        pass

    def delSQL(self, level1, level2, level3, name ):
        sql_cmd = '''
                update sql
                set del_flag = 1
                where level_1 = '%s' and  level_2 = '%s' and level_3 in( '%s','0')
                    and name = '%s'
            ''' % (level1, level2, level3, name)
        self.db.do_execute(sql_cmd)

    def updateSQL(self, level1, level2, level3, name, sql):
        sql_cmd = '''
                update sql
                set sql = %s
                where level_1 = '%s' and  level_2 = '%s' and level_3 in( '%s','0')
                    and name = '%s'
            ''' % (sql, level1, level2, level3, name)
        self.db.do_execute(sql_cmd)

    def changeCommon(self, string):
        return string.replace('\'', '\'\'')

# if __name__ == '__main__':
#     data = getData()
#     # print data.getAllData()
#     # print data.getLevel2('tbl')
#     # print data.getLevel3('tbl','poi')
#     # print data.getName('tbl','poi','')
#     # print data.getSQLInfo('tbl','poi','',u'通过Poi名字找到其地址')
#     print data.getTreeDict()