import re

# bstr = "1+2-5-5-5-5+12"
# out = 0
# ret = bstr.split('+')

# for i in ret:
    # k = 0
    # for j in i.split('-'):
        # out = out + int(j) if k == 0 else out - int(j)
        # k += 1

# print(out)
# ^[^0-9]+
# substring = "a111AA+"
# pat = re.compile('A{0,1}')
# s = re.sub(pat, '', substring)
# print(s)

# print(re.split('[a-f]+', '0a3B9', flags=re.IGNORECASE))

# print(re.split('[^a-f]+', '0a3B9', flags=re.IGNORECASE))

# def dashrepl(matchobj):
    # if matchobj.group(0) == '-': return ' '
    # else: return '-'
# print(re.sub('-+', dashrepl, 'pro----gram-files'))



# f = 0

# def tst(matchobj):
    # global f
    # nm = [str(i) for i in range(10)]
    # if f == 1 and matchobj.group(0)[0] not in nm:
        # return ""
    # if matchobj.group(0)[0] == '-': 
        # f = 1
        # return "-"
    # if matchobj.group(0)[0] == '+':
        # f = 1
        # return "+"
    # if matchobj.group(0)[0] == '*': 
        # f = 1
        # return "*"
    # if matchobj.group(0)[0] == '/': 
        # f = 1
        # return "/"
    # s = ""
    # f = 0
    # for i in matchobj.group(0):
        # if i in nm:
            # s += str(i)
    # return s
    
# txtstr = '189++++2---++aa++****////////***'
# print(re.sub('[0-9]|[\-]+|[\+]+|[\*]+|[\/]+', tst, re.sub('[^0-9+-/*]','',txtstr)))



# print(re.sub('.[\-]?+',"","---4------"))

# global a, b
# a = 4
# b = 4
# def plus():
    # global a, b
    # return a+b
# def minus():
    # return a-b
# def mul():
    # return a*b
# def div():
    # return a//b

# dict_o = {'+': plus(), '-': minus(), '*': mul(), '/': div()}

# s = "5*60/2+1*4"
# ar = [int(i) for i in s.replace('+', ' ').replace('-', ' ').replace('*', ' ').replace('/', ' ').split()]
# print(ar)
# print(list(s))
# print(s.find('/'))

# #print(dict_o[s[1]](a=int(s[0]),b=int(s[2])))

# for i in range(1,len(s),2):
    # a = int(s[i-1])
    # b = int(s[i+1])
    # print(dict_o[s[i]])



# global a, b
# a = 4
# b = 4
# def plus():
#     global a, b
#     return a+b
# def minus():
#     global a, b
#     return a-b
# def mul():
#     return a*b
# def div():
#     return a//b
# out = 0
# dict_o = {'+': plus(), '-': minus(), '*': mul(), '/': div()}
# txt1 = '4+8+95-13'
# nums = re.findall('[0-9]+', txt1)
# operators = re.findall('[^0-9]', txt1)
# a=int(nums[0])
# print('a=',a)
# b=int(nums[1])
# print('b=',b)
# out+=dict_o[operators[0]]
# print('a+b=',out)
# for i in range(1,len(operators)):
#     a=out
#     b=nums[i+1]
#     out+=dict_o[operators[i]]
#
# print(out)


dict_o = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
          '*': lambda x, y: x * y, '/': lambda x, y: x / y}

print(dict_o['+'](2,3))