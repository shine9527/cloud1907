# 请统计出tkings.txt中, 『关羽』、『曹操』、『刘备』、『张飞』、『赵云』出现的次数
# 并用字典存储, 形式为: {人物01：次数, 人物02：次数, ...}

file = open(file='./file/tkings.txt', mode='r', encoding='utf8')

content = file.read().replace('\n', '')

character = {}
user = ('关羽', '曹操', '刘备', '张飞', '赵云')

for i in user:
    if i not in character.keys():
        character.setdefault(i, content.count(i))
print(character)

file.close()
