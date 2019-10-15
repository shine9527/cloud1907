#!/usr/bin/env bash


# 正常的循环100个数字,使用shell
#for n in $(seq 100);do
#  echo ${n}
#done

# 循环1-100,当循环到54时,跳出循环: break
#for n in $(seq 100);do
#  if [ ${n} -eq 54 ];then
#    break
#  else
#    echo ${n}
#  fi
#done

# 找出规定网段内的所有活动地址
# 分析需求: 1.ping通的主机所拥有的IP地址就是活动地址: ping
#	    2.网段需要键盘输入来确定
#	    3.记录活动IP不记录非活动IP
read -p 'netip: ' netip
for i in $(seq 254);do
 { 
  ping -c1 -s0.5 ${netip}.${i} &>/dev/null
  if [ $? -eq 0 ];then
    echo "${netip}.${i}" >>/opt/iplist.txt
  fi
 }&
done
wait
echo "finish..."

