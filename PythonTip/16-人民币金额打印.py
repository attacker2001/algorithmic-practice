# coding=utf-8

"""
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<1,0000,0000), 打印出人民币大写表示.
注意：请以Unicode的形式输出答案。你可以通过decode("utf8")来将utf8格式的字符串解码为Unicode，例如你要输出ans = "零圆", print ans.decode("utf8").
Note：数据已于2013-11-19日加强，原来通过的代码可能不能再次通过。
"""
a = 123456
# #################_Submitted code as follows_###########################
# num = u'零壹贰叁肆伍陆柒捌玖'
# chara = list(u'仟佰拾万仟佰拾圆')
#
# index = -1
# for i in str(a)[::-1]:
#     chara.insert(index, num[int(i)])
#     index -= 2
#
#
# print ''.join(chara[8 - len(str(a)):])

# 没搞出来 改天继续
