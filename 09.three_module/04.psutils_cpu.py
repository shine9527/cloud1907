import psutil


# # cpu info
# print('CPU的逻辑核心数为: {}'.format(psutil.cpu_count()))
# print('CPU整体占用百分比情况为: {}'.format(psutil.cpu_percent(interval=1, percpu=False)))
# print('CPU各个核心所占用的百分比情况: {}'.format(psutil.cpu_percent(interval=1, percpu=True)))
# print('CPU整体占用时间情况: {}'.format(psutil.cpu_times(True)))
# print('CPU整体占用时间的百分比情况: {}'.format(psutil.cpu_times_percent(interval=3, percpu=True)))
#
#
# # memory info
# print(psutil.virtual_memory())
# print(psutil.swap_memory())
#
# # disk info
# print(psutil.disk_partitions(True))
# print(psutil.disk_usage('/'))

# # network info
# print(psutil.net_io_counters())
# # print(psutil.net_connections(kind='inet'))
# print(psutil.net_if_stats())

print(psutil.pids())
process = psutil.Process(pid=15886)
print(process.name())               # 获取进程名字
print(process.exe())                # 获取进程执行路径
print(process.status())             # 获取进程状态
print(process.num_threads())        # 获取进程开启的线程数
print(process.create_time())        # 获取进程创建时间
print(process.cpu_times())          # 获取user、system两个 CPU 时间
print(process.memory_percent())     # 获取进程内存利用率
print(process.memory_info())        # 获取进程内存rss、vms信息
