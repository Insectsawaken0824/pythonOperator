# -*- coding:utf-8 -*-

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'hello')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('hello world!')

if match:
    # 使用Match获得分组信息
    print match.group()

# 以下两个正则表达式是等价的：
a = re.compile(r"""\d +  # the integral part 
                   \.    # the decimal point 
                   \d *  # some fractional digits""", re.X)
b = re.compile(r"\d+\.\d*")
# 这个例子可以简写为：
m = re.match(r'hello', 'hello world!')
print m.group()

# re模块还提供了一个方法escape(string)，用于将string中的正则表达式元字符如*/+/?等之前
# 加上转义符再返回，在需要大量匹配元字符时有那么一点用

# 当需要提取的内容只有一个，或是只需要获取第一次成功匹配的内容时，可以使用Match()方法。
# 当使用Match()方法时，只要在某一位置匹配成功，就不再继续尝试匹配，并返回一个Match类型的对象。
# 注意：Match只从位置0开始匹配，除非使用Pattern对象指定pos参数。在Pattern类的实例方法部分有详细说明。
m=re.match(r'a','ababa')
print m.group()
# 虽然Match()只是取一次匹配，但是可以通过捕获组来获取多个指定子串。
m=re.match(r'(a)(b)','ababa')
print m.groups()

# Match对象是一次匹配的结果，包含了很多关于此次匹配的信息，可以使用Match提供的可读属性或方法来获取这些信息。
# Match属性
# 1、string：匹配时使用的文本。
# 2、re：匹配时使用的Pattern对象。
# 3、pos：文本中正则表达式开始搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
# 4、endpos：文本中正则表达式结束搜索的索引。值与Pattern.match()和Pattern.seach()方法的同名参数相同。
# 5、lastindex：最后一个被捕获的分组在文本中的索引。如果没有被捕获的分组，将为None。
# 6、lastgroup：最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
# Match方法
# 1、group([group1, …])
# 获得一个或多个分组截获的字符串；指定多个参数时将以元组形式返回。group1可以使用编号也可以使用别名；
# 编号0代表整个匹配的子串；不填写参数时，返回group(0)；没有截获字符串的组返回None；
# 截获了多次的组返回最后一次截获的子串。
m=re.match(r'(\w{2})+','aabbcc')
print m.group(1)
# 再说明一下：search，找不到，则继续找，直到结束；如果一旦找到，则综止。而不管后面是否仍有内容匹配，都不在继续。
# a、group()等于group(0)，代表整个匹配的子串
# b、group(1)，代表编号为1的捕获组内容；group(2)代表编号为2的捕获组内容
# c、指定多个参数时，以tuple形式返回。
# d、普通捕获组与命名捕获组没有混合编号规则。捕获组的编号统一是按照“(”出现的顺序，从左到右，从1开始进行编号的。
# 总结：group就是返回捕获的内容。参数0或无参数表示整个正则表达式捕获的文本，1表示第1个括号匹配的内容，2表示第2个括号匹配的内容，以此类推。
s="1-abc,2-abc,3-abc"
pattern=r'(?P<name>\d)-(\w{3}),' #命名捕获组(?P<名字>) 注意：这里的P要大写
m=re.search(pattern,s)
print m.group(),m.group(0)
print m.group(1)
print m.group(2)
print m.group(1,2,0)
print m.group('name')

# 2、groups([default])
# 以元组形式返回全部分组截获的字符串。相当于调用group(1,2,…last)。
# default表示没有截获字符串的组以这个值替代，默认为None。
s="1-abc,2-abc,3-abc"
pattern=r'((?P<name>\d)-)(\w{3}),'
m=re.search(pattern,s)
print m.groups()

# 3、groupdict([default])
# 返回命名捕获组字典。以组名为键、以该组截获的子串为值，普通捕获组不包含在内。default含义同上。
m = re.match("(\w+) (\w+)", "hello world")
print m.groupdict()
# 通过上例可以看出，groupdict()对普通捕获组不起作用
m = re.match("(?P<first>\w+) (?P<secode>\w+)", "hello world")
print m.groupdict()

# 4、start([group])
# 返回指定的组截获的子串在string中的起始索引（子串第一个字符的索引）。group默认值为0。

# 5、end([group])
# 返回指定的组截获的子串在string中的结束索引（子串最后一个字符的索引+1）。group默认值为0。

# 6、span([group])
# 返回(start(group), end(group))。

# 7、expand(template)
# 将匹配到的分组代入template中然后返回。template中可以使用 \id 、\g<id> 、\g<name> 引用分组。id为捕获组的编号，name为命名捕获组的名字。
s="abcdefghijklmnopqrstuvwxyz"
pattern=r'(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)(\w)'
m=re.search(pattern,s)
print m.expand(r'\1'), m.expand(r'\10'), m.expand(r'\g<10>')

m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup
print ""
print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

# Pattern对象是一个编译好的正则表达式，通过Pattern提供的一系列方法可以对文本进行匹配查找。
# Pattern不能直接实例化，必须使用re.compile()进行构造。
# Pattern属性
# 1、pattern：编译时用的正则表达式字符串。
# 2、flags：编译时用的匹配模式。数字形式。
# 3、groups：表达式中分组的数量。
# 4、groupindex：以表达式中有别名的组的别名为键、以该组对应的编号为值的字典，没有别名的组不包含在内。
p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
print "p.pattern:", p.pattern
print "p.flags:", p.flags
print "p.groups:", p.groups
print "p.groupindex:", p.groupindex
# Pattern方法
# 1、pattern.match(string[, pos[, endpos]]) | re.match(pattern, string[, flags])
# →匹配成功返回string，失败返回None
# 这个方法将从string的pos下标处起尝试匹配pattern；如果pattern结束时仍可匹配，则返回一个Match对象；
# 如果匹配过程中pattern无法匹配，或者匹配未结束就已到达endpos，则返回None。
# pos和endpos的默认值分别为0和len(string)；re.match()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。
# 注意1：这个方法并不是完全匹配。当pattern结束时若string还有剩余字符，仍然视为成功。想要完全匹配，可以在表达式末尾加上边界匹配符'$'。
# 注意2：只要匹配成功就不再继续匹配。
# 比较下面两个例子：
pattern = re.compile(r'h')
match = pattern.match('hi,hello world!')
if match:
    print match.group()
pattern = re.compile(r'e')
match = pattern.match('hi,hello world!')
if match:
    print match.group()

# 2、pattern.search(string[, pos[, endpos]]) | re.search(pattern, string[, flags])
# → 匹配成功返回string对象，失败返回None
# 这个方法用于查找字符串中可以匹配成功的子串。从string的pos下标处起尝试匹配pattern。如果pattern结束时仍可匹配，
# 则返回一个Match对象（即如果找到一个匹配就返回一个MatchObject对象。而不会继续往下匹配。）；
# 若无法匹配，则将pos加1后重新尝试匹配；直到pos=endpos时仍无法匹配则返回None。
# pos和endpos的默认值分别为0和len(string))；re.search()无法指定这两个参数，参数flags用于编译pattern时指定匹配模式。
m=re.search("abcd", '1abcd2abcd')
print m.group()  #找到即返回一个match object，然后根据该对象的方法，查找匹配到的结果。
print m.start()
print m.end()

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'world')
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None
# 这个例子中使用match()无法成功匹配
match = pattern.search('hello world!')
if match:
    # 使用Match获得分组信息
    print match.group()
# 了解match方法与search方法的区别
# match方法总是默认从字符串的起始位置开始匹配。就像模式字符串的第一个元素是/A一样。
# 如果关心发生在字符串的任意位置的匹配，而不是仅发生在字符串首部的匹配，Python管这种操作叫search，为是为了和match有所区别而取的新术语。

# 3、pattern.split(string[, maxsplit]) | re.split(pattern, string[, maxsplit])
# → 返回list对象
# 按照能够匹配的子串做为分割符将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割。
# 如果匹配失败，则返回仅有一个值的列表，该值为string字符串。
p = re.compile(r'\d+') #测试匹配失败的结果，将 \d+ 改为下划线 _
print p.split('one1two2three3four4')

# 4、pattern.findall(string[, pos[, endpos]]) | re.findall(pattern, string[, flags])
# → 返回list对象
# 搜索string，以列表形式返回全部能匹配的子串。如果匹配失败，返回空列表[]
p = re.compile(r'\d+')
print p.findall('one1two2three3four4')

# 5、pattern.finditer(string[, pos[, endpos]]) | re.finditer(pattern, string[, flags])
# → 返回callable-iterator对象
# 搜索string，返回一个顺序访问每一个匹配结果（Match对象）的迭代器。
p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group(),
print

# 6、pattern.sub(repl, string[, count=0]) | re.sub(pattern, repl, string[, count=0])
# → 返回字符串对象
# 返回字符串string的一个拷贝，该串中的所有匹配均被替换成了repl。 当repl是一个字符串时，可以使用 \id 或\g<id> 、\g<name> 引用分组，但不能使用编号0。 当repl是一个方法时，这个方法应当只接受一个参数（Match对象），并返回一个字符串用于替换（返回的字符串中不能再引用分组）。 count默认为0，表示所有的匹配都被替换。如果count大于0时，只有前count个匹配被替换。
# 如果匹配失败，则返回原string。
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print p.sub(r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print p.sub(func, s)

# 7、pattern.subn(repl, string[, count]) |re.subn(pattern, repl, string[, count])
# → 返回tuple对象
# subn 与 sub 相同, 只是 subn 返回一个元组 (new_string, n) ,这里 n 是替换的个数
# 如果匹配失败，返回tuple对象，new_string值为原字符串string，n值为0
p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
print p.subn(r'\2 \1', s)

def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()

print p.subn(func, s)
