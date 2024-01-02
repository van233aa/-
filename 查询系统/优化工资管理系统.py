import time

f_name=input("请输入要查询的文件名字")
with open(f"{f_name}.txt","r",encoding="gbk") as s:
    salary_txt=s.read()
    salary_list=salary_txt.split()
print(salary_list)


dictm_txt = {}
count = 0
#将列表转化成字典
for i in salary_list:
    count += 1
    if count % 2!= 0:
        key_txt = i
        # print(key_txt)
    else:
        value_txt = i
        # print(value_txt)
        dictm_txt.setdefault(key_txt, value_txt)
        # dict_txt[key_txt]=value_txt和上面一样添加键值对
print(dictm_txt)


def function():

    print("------员工工资查询系统------")
    print("------1.查询工资和更改工资------")
    print("------2.新增信息------")
    print("------3.删除信息------")


def run():
    number=int(input("根据您的需要，请输入序号执行内容"))
    if number==1:
        print("执行查询和更改工资")
        search_f()
    elif number==2:
        print("执行新增信息")
        add_f()
    elif number==3:
        print("执行删除信息")
        del_f()



# 查询工资和更改工资
def search_f():

    name = input('请输入你要查询的人名：')
    salary = input('是否需要更改此员工工资，如果不需要就回复否,需要更改直接填写数字单位元：')
    if name=="N"or salary=="N":
        exit()
    elif salary == '否':
        print(f"{name}的工资是："+dictm_txt[name])
    else:
        dictm_txt[name] = salary
        print('{}更改后的工资为{}'.format(name, salary))
        with open('优化文本库.txt', 'w') as f:
            for i, b in dictm_txt.items():
                f.write(str(i) + ' ')
                f.write(str(b) + ' ')
                print(i,b, end=' ', )
# search_f()

# 新增信息
def add_f():
    newname = input('请输入新增加的员工信息：')
    new_salary = input('请输入新增加的员工工资：')
    if newname=="N"or new_salary=="N":
        exit()
    else:
        dictm_txt[newname] = new_salary
        print("{}工资{}已添加".format(newname, new_salary))
        with open('优化文本库.txt', 'w') as f:
            for i, b in dictm_txt.items():
                f.write(str(i) + ' ')
                f.write(str(b) + ' ')
                print(i,b, end=' ',)
# add_f()

#删除信息
def del_f():
    del_name = input('请输入要删除的员工名字：')
    if del_name  == "N" :
        exit()
    else:
        del dictm_txt[del_name]
        print("{}信息已删除".format(del_name))
        with open('优化文本库.txt', 'w') as f:
            for i, b in dictm_txt.items():
                f.write(str(i) + ' ')
                f.write(str(b) + ' ')
                print(i, b, end=' ', )
# del_f()

if __name__=="__main__":
    function()
    run()
    time.sleep(5)
    print("是否还要继续进行")
    n=int(input("进行按1 不进行按2："))
    while 1==1:
        if n == 1:
            function()
            run()
            time.sleep(5)
            n = int(input("\n进行按1 不进行按2："))
        elif n ==2:
            exit()
