# -*- coding: UTF8 -*-
# read and write file

# read sql txt

sql_path = r'd:\TEST\sql_collect\sql_file\sql_list.txt'
tree_path = r'd:\TEST\sql_collect\sql_file\tree_list.txt'

def read_sql_txt ( file_path = tree_path ):
    try:
        file_object = open(file_path, 'r')
    except IOError:
        print "The file don't exist, Please double check!"
        exit()
    try:
        all_the_text = file_object.read()
        if all_the_text:
            result = eval(all_the_text)
            return result
        else:
            return ''
    finally:
        file_object.close()


# 把文件中的代码写入到数据库中。
def insertIntoDB(db, file):
    for level1, value1 in file.items():
        for level2, value2 in value1.items():
            if value2:
                for level3, value3 in value2.items():
                    if  type(value3) == dict:
                        for name, sql in value3:
                            sql = changeCommon(sql)
                            insertDict(db, level1, level2, level3, name, sql)
                    else:
                        value3 = changeCommon(value3)
                        insertDict(db, level1, level2, 0, level3, value3)
            else:
                insertDict(db, level1, level2, 0, 0, 0)


def changeCommon(string):
    return string.replace('\'', '\'\'')


def insertDict(db, level1, level2, level3, name, sql_string):
    sql_string.strip()
    if sql_string.startswith('\''):
        sql_cmd = '''
        insert into sql(level_1, level_2, level_3, name, sql, comment, frequency)
                select '%s', '%s', '%s', '%s', %s, '', 0
            ''' % (level1, level2, level3, name, sql_string)
    else:
        sql_cmd = '''
            insert into sql(level_1, level_2, level_3, name, sql, comment, frequency)
            select '%s', '%s', '%s', '%s', '%s', '', 0
        ''' % (level1, level2, level3, name, sql_string)
    db.do_execute(sql_cmd)

def toDict(file_text):
    if file_text:
        return eval(file_text)
    else:
        return ''
    pass

# write data into file
def write_sql_txt ( file_path, data ):
    try:
        file_object = open(file_path, 'w')
    except IOError:
        print "The file don't exist, Please double check!"
        exit()

    file_object.write( data )
    file_object.close()
    pass

# if __name__ == '__main__':
#     file = read_sql_txt()
#     insertIntoDB(file)

# tree_string = "['here',['poi','area',['name','num'],'postcode'],'mid',['poi','area'],''tbl',['a','b']]"
# write_sql_txt( tree_path, tree_string)