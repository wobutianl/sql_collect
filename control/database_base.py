# -*- coding: UTF8 -*-
# connect to database and do simple thing
# connect / fetch result / get all database name /

import psycopg2
class database( object ):

    def __init__(self ):
        self.connected = False

    def connect(self, host, port='5432', db_name='postgres'):
        '''
        :param db_name: database name
        :param host:  host
        :return:
        '''
        if self.connected == True:
            return -1

        self.port = port
        self.conn = psycopg2.connect(database=db_name, user="postgres", password="", host=host, port = self.port)
        self.cur = self.conn.cursor()
        self.connected = True

    def fetchone(self, sqlcmd):
        '''get one record'''
        sql_result = self.do_execute(sqlcmd)

        if sql_result == 0:
            self.result = self.cur.fetchone()
            return self.result
        else:
            return sql_result

    def fetchall(self, sqlcmd):
        '''
        :param sqlcmd:
        :return: all the result
        '''
        sql_result = self.do_execute( sqlcmd )
        if sql_result == 0:
            self.result = self.cur.fetchall()
            return self.result
        else:
            return sql_result

    def get_column_name(self):
        result = []
        if self.cur and self.result:
            for i, value in enumerate(self.result[0]):
                result.append(self.cur.description[i][0])
            return result
        else:
            return result


    def do_execute(self, sqlcmd):
        sql_result = self.execute(sqlcmd)

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