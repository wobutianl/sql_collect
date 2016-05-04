# -*- coding: UTF8 -*-
import nose


def setUp():
    print 'run at the beginning'

def tearDown():
    print 'run at the end'

import control.database_base

def testDBLoad():
    db = control.database_base.database()
    db.connect("localhost", db_name='sql_collect')
    sql = ''' select sql from sql where name = '所有数据库的名字' '''
    oneSQL = db.fetchone(sql)
    print oneSQL
    assert oneSQL == (' SELECT datname FROM pg_database;',)
    print 'test to load data from database'

def testDBInsert():
    import getValue
    db = control.database_base.database()
    db.connect("localhost", db_name='sql_collect')


    sql = '''
        insert into sql(level_1, level_2, level_3, name, sql, comment, frequency)
                select '%s', '%s', '%s', '%s', %s, '', 0
            ''' % (level1, level2, level3, name, sql_string)
    db.do_execute(sql)
    sql = 'select * from sql '
    oneSQL = db.fetchone(sql)
    print oneSQL
    assert oneSQL == (1, 'tbl', 'poi', 'name', 'find poi name by id', 'select * from tbl_poi_info join tbl_poi_name using(poi_id)', '', 0)

# def testFileToDB():
#     import read_file
#     file = read_file.read_sql_txt()
#
#     db = control.database_base.database()
#     db.connect("localhost", db_name='sql_collect')
#     read_file.insertIntoDB(db, file)
#     sql = ''' select sql from sql where name = '每个国家对应的area_0' '''
#     oneSQL = db.fetchone(sql)
#     print oneSQL
#     assert oneSQL == '''SELECT distinct area_0,name
#       FROM tbl_area_info
#       join tbl_area_name
#       using(area_id)
#       join tbl_area_country
#       using(area_id)
#     '''

if __name__ == '__main__':
    nose.runmodule()