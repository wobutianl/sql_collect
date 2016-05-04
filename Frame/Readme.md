frame :主框架
subMain: 包括连接数据库和执行SQL的次框架
mainSplit: 包括TreeCtrl, exeSQL, addSQL 三个界面

splitSQL : 包括 treeCtrl, exeSQL

addSQL: 添加SQL语句的界面
exeSQL：执行SQL语句的界面
treeCtrl：树形结构的界面

Frame
    toolBar
    subMain
        connectDB
        splitSQL
            treeCtrl
            exeSQL
                richText
                wxGrid
        addSQL