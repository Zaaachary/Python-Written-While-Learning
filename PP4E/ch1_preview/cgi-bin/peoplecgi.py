"""
实现用来查看和更新保存在shelve中类实例的基于Web的界面，
shelve保存在服务器上（如果是本地机器的话就是同一个机器）
"""
import cgi, shelve, sys, os                 # cig.test()转储输入
shelvename = 'class-shelve'                 # shelve文件在当前工作目录
fieldnames = ('name', 'age', 'job', 'pay')

form = cgi.FieldStorage()                   # 解析表单数据
print('Content-type: text/html')            # 响应html中的hdr和空行
sys.path.insert(0, os.getcwd())             # 为了这个和pickler查找person getcwd获得绝对路径

# 主html模板
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
    <table>
    <tr><th>key<td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
    <p>
    <input type=submit value="Fetch",  name=action>
    <input type=submit value="Update", name=action>
</form>
</body></html>
"""

# 为$ROWS$的数据行插入html
# 以rowhtml为模板 生成每一个fieldname的行html
rowhtml  = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)   # 文本替换

def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:                    # 值可能包含&，>等字符
        value = new[field]                      # 作为代码显示：被引号引起
        new[field] = cgi.escape(repr(value))    # 转义html字符
    return new

def fetchRecord(db, form):
    try:
        key = form['key'].value
        record = db[key]
        fields = record.__dict__                # 使用属性字典
        fields['key'] = key                     # 填充响应字符串
    except:
        fields = dict.fromkeys(fieldname, '?')
        fields['key'] = 'Missing of invalid key!'
    return fields

def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]                       # 更新已有记录
        else:
            from person import Person              # 为键值创建/保存新记录
            record = Person(name='?', age='?')     # 字符串必须被引号引起
        for field in fieldnames:
            setattr(record, field, eval(form[field].value))
        db[key] = record
        fields = record.__dict__
        fields['key'] = key
    return fields


db = shelve.open(shelvename)
action = form['action'].value if 'action' in form else None
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')        # 错误的提交按钮值
    fields['key'] = 'Missing or invalid action!'
db.close()
print(replyhtml % htmlize(fields))                 # 使用dict来填充响应
