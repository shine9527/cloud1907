#!/usr/bin/env bash

while :
do
cat <<-HLIONS
	+------------------+
        |  system tools    |
        +------------------+
        | a.查看用户数量   |
        | b.查看进程数量   |
        | c.退出           |
        +------------------+
HLIONS
read -p "please choose: " choose
case ${choose} in
  a)
   number=$(wc -l /etc/passwd)
   echo "用户的数量为: ${number:0:3}"
   ;;
  b)
   number=$(ps aux | wc -l)
   echo "进程的数量为: ${number}"
   ;;
  c)
   exit
   ;;
  *)
   echo "your choose must be in (a, b, c), 你个憨批"
   ;;
esac
done



