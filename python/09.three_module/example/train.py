# 1. 有这样一个句子: "this is my house", 需要你利用代码实现句子反转, 反转后的效果是: "house my is this"
jz = 'this is my house'
result = jz.split()
result.reverse()
jz_reverse = ''
for element in result:
    s = ' ' + element
    jz_reverse += s
print(jz_reverse.lstrip())

# 2. 敏感字符替换, 如句子中存在有特殊的敏感词汇,直接把敏感词汇替换成"*"号
# search = input('search: ')
# if '敏感词' in search:
#     print(search.replace('敏感词', '***'))
# else:
#     print(search)

# 3. 现在有这样一个元组("string", "world", 1, 2, 3, 4, 6, 9, 10), 把其中的数字提取到一个列表中
n = ("string", "world", 1, 2, 3, 3.14, 4, 6, 9, 10)
m = []
for element in n:
    if type(element) in (int, float):
        m.append(element)
print(m)

# 4. list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
# 转换成["string", "tuple", "list", 1, 2, 3, 4, 5, 6, 7]
list01 = ["string", "tuple", "list", (1, 2, 3, 4, 5), [6, 7]]
list02 = []
for element in list01:
    if type(element) in (int, float, str, bool):
        list02.append(element)
    else:
        for i in element:
            list02.append(i)
print(list02)

# 5. 对[23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]进行排序, 要求使用for循环
number = [23, 12, 15, 11, 29, 24, 57, 21, 80, 99, 45]
for i in range(len(number)):
    for j in range(len(number) - 1):
        if number[j] < number[j + 1]:
            number[j], number[j+1] = number[j+1], number[j]
print(number)

# 7. 快速去除掉[1, 3, 2, 4, 1,3, 2, 4, 9, 15, 22, 15, 18, 19, 17, 22, 43]中相同的元素, 并生成一个新的列表.
number = [1, 3, 2, 4, 1, 3, 2, 4, 9, 15, 22, 15, 18, 19, 17, 22, 43]
print(list(set(number)))

# 8. 在tkings.txt中统计所有三国时期有名武器的出现次数;所有主公名字出现的次数;
with open(file='tkings.txt', mode='r') as file:
    content = file.read().replace('\n', '').replace(' ', '')
    search = input('请输入你要查找的内容(结果为该内容出现的次数): ')
    number = content.count(search)
    print('{} 出现的次数为: {}'.format(search, number))

# 计步器
def aaa(step=0):
    def bbb():
        nonlocal step
        step += 1
        return step
    return bbb


step = aaa(0)
# 你走了一步
current_step = step()
print('当前步数为 {}'.format(current_step))
# 你又走了一步
current_step = step()
print('当前步数为 {}'.format(current_step))

print('你之前走了15000步, 此时你又走了一步')
step = aaa(15000)
current_step = step()
print('当前步数为 {}'.format(current_step))
