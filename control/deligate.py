def singleton(cls, *args, **kw):    
    instances = {}    
    def _singleton():    
        if cls not in instances:    
            instances[cls] = cls(*args, **kw)    
        return instances[cls]    
    return _singleton    


@singleton    
class ShareData(object):
    a = 1
    def __init__(self):
        self.data = ''
        self.db = ''
        self.exeSQL = ''
        self.level1 = ''
        self.level2 = ''
        self.level3 = ''
        self.name = ''
        self.treeCtrl = ''

    def setTree(self, tree):
        self.tree = tree

    def getTree(self):
        return self.tree

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setDB(self, db):
        self.db = db

    def getDB(self):
        return self.db

    def setSQL(self, sql):
        self.exeSQL = sql

    def getSQL(self):
        return self.exeSQL

    def setL1(self, l1):
        self.level1 = l1

    def getL1(self):
        return self.level1

    def setL2(self, l2):
        self.level2 = l2

    def getL2(self):
        return self.level2

    def setL3(self, l3):
        self.level3 = l3

    def getL3(self):
        return self.level3

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

# a = ShareData()
# a.setDB(123)
#
# b = ShareData()
# print b.getDB()