# -*- coding: UTF8 -*-
# connect to database and do simple thing
# connect / fetch result / get all database name /

import psycopg2
class database( object ):

    def __init__(self ):
        self.connected = False

    def connect(self, host, db_name='postgres'):
        '''
        :param db_name: database name
        :param host:  host
        :return:
        '''
        if self.connected == True:
            return -1

        self.conn = psycopg2.connect(database=db_name, user="postgres", password="", host=host, port="5432")
        self.cur = self.conn.cursor()
        self.connected = True

    def fetchone(self):
        '''get one record'''
        return self.cur.fetchone()

    def fetchall(self, sqlcmd):
        '''
        :param sqlcmd:
        :return: all the result
        '''
        sql_result = self.do_execute( sqlcmd )
        if sql_result == 0:
            return self.cur.fetchall()
        else:
            return sql_result

    def do_execute(self, sqlcmd):
        sql_result = self.execute(sqlcmd)
        # if sql_result == 0:
        #     self.commit()
        #     return 0
        # else:

        self.commit()
        return sql_result


    def execute(self, sqlcmd, parameters = []):
        '''execute commands '''
        try:
            if parameters:
                self.cur.execute(sqlcmd, parameters)
            else:
                self.cur.execute(sqlcmd)
            #self.conn.commit()
            return 0
        except Exception,ex:
            return str(ex)
            # return '%s:%s' % (Exception, ex)
            # print 'SQL execute error:' + sqlcmd

    def commit(self):
        self.conn.commit()
        return 0

    def close(self):
        if self.connected == True:
            self.cur.close()
            self.conn.close()
            self.connected = False

    def get_db_name(self ):
        sqlcmd = ' SELECT datname FROM pg_database;'
        return self.fetchall(sqlcmd)

    def isconnected(self):
        return self.connected