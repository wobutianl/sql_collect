# -*- coding: UTF8 -*-
# read and write file

# read sql txt
import os

sql_path = r'd:\TEST\sql_collect\sql_file\sql_list.txt'
tree_path = r'd:\TEST\sql_collect\sql_file\tree_list.txt'

def read_sql_txt ( file_path ):
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



# read_sql_txt(sql_path)


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

# tree_string = "['here',['poi','area',['name','num'],'postcode'],'mid',['poi','area'],''tbl',['a','b']]"
# write_sql_txt( tree_path, tree_string)