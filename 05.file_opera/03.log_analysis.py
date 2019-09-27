# 打开文件
with open(file='./file/access_log', mode='r') as file:
    ips = {}
    for lines in file.readlines():
        if lines.split()[0] not in ips.keys():
            ips.setdefault(lines.split()[0], 1)
        else:
            ips[lines.split()[0]] += 1
    ip = []
    for items in ips.items():
        ip.append(items)
    for i in range(len(ip)):
        for j in range(len(ip) - 1):
            if ip[j][1] < ip[j+1][1]:
                ip[j], ip[j+1] = ip[j+1], ip[j]
    print(dict(ip[:10]))

