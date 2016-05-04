# sql_collect
make a softerware to collect sql which used in daily work , and may reused one and one again 

## 功能需求
1. 更新，删除，添加 SQL代码到列表
2. 执行SQL代码
3. 显示SQL结果
4. 数据库连接
5. 备份代码文件

## 目前存在问题
1. 显示结果时，不能显示列名 ( 完成）
2. 没有添加 Port 选项 
3. 没有Sql代码搜索功能
4. 没有自定义路径选择
5. 需要重构

## 详细设计需要

### 背景
- 每次都要写重复的代码
- 每次都会进行Bug问题的调查
- 每次写完调查代码，不一定会保留，但是下一次可能还会遇到
- Check可能会有需要
- 对每个问题进行细致化的命名

### 目标
- Sql代码分类。
- 新加SQL代码，并加入指定分类
- 执行SQL代码，显示执行结果
- 可修改代码
- 可删除指定代码

### 功能
1. 数据库连接
2. 编辑代码
    - 新加
    - 删除
    - 修改
3. Sql代码执行
4. Sql代码显示

### 具体实现
1. 分类
    - 实现分类TreeCtrl （完成）
    - 实现通过点击TreeItem，显示对应的Sql字符串（完成）
2. 添加代码
    - 读取各层分类(over)
    - 写入文件(over)
3. 数据库
    - 获取数据库(over)
    - 按供应商获取数据库(over)
    - 连接数据库(over)
    - 执行数据库代码(over)
    - 显示结果
4. 其他
    - 读取List文件，显示在Tree中(over)
    - 新加Sql语句(over)
    - 检索目录