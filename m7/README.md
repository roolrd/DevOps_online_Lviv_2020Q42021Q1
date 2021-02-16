## Task. Linux administration with bash.  

#### A. Create a script that uses the following keys:  

```
#!/bin/bash

subnet_ip=`curl http://169.254.169.254/latest/meta-data/network/interfaces/macs/06:bb:e2:68:c8:e0/subnet-ipv4-cidr-block 2>/dev/null`
#echo $subnet_ip


all() {
sudo nmap -T4 -sn -oG - $subnet_ip | gawk '/Up/{print $2,$3}'
#sudo nmap -T4 -sn -oG - $subnet_ip | grep Up | expand | cut -d ' ' -f 2,3
}

target() {
ip_up_hosts=`sudo nmap -T4 -sn -oG - $subnet_ip | gawk '/Up/{print $2}'`
#sudo ss -tpln
for i in $ip_up_hosts
do
 echo '=======================START===================================='
 echo "Opened TCP ports on host $i"
 sudo nmap $i
 echo '=======================FINISH==================================='
 echo
done
}

if [ -z "$1" ]
then
  echo "Usage: 7a [--all displays the IP addresses and symbolic names of all hosts in the current subnet]
          [--target displays a list of open system TCP ports]"
else
 while [ -n "$1" ]
 do
   case "$1" in
      --all) all ;;
   --target) target ;;
          *) echo "7a: invalid option -- $1" ;;
  esac
  shift
 done
```

```
ubuntu@ip-172-31-33-124:~/EPAM/Univer$ ./7a
Usage: 7a [--all displays the IP addresses and symbolic names of all hosts in the current subnet]
          [--target displays a list of open system TCP ports]
###################################################################
ubuntu@ip-172-31-33-124:~/EPAM/Univer$ ./7a -a
7a: invalid option -- -a
###################################################################
ubuntu@ip-172-31-33-124:~/EPAM/Univer$ ./7a --all
172.31.32.1 (ip-172-31-32-1.eu-central-1.compute.internal)
172.31.42.168 (ip-172-31-42-168.eu-central-1.compute.internal)
172.31.46.205 (ip-172-31-46-205.eu-central-1.compute.internal)
172.31.33.124 (ip-172-31-33-124.eu-central-1.compute.internal)
####################################################################
ubuntu@ip-172-31-33-124:~/EPAM/Univer$ ./7a --target
=======================START====================================
Opened TCP ports on host 172.31.32.1

Starting Nmap 7.01 ( https://nmap.org ) at 2021-02-16 21:12 UTC
Nmap scan report for ip-172-31-32-1.eu-central-1.compute.internal (172.31.32.1)
Host is up (0.00013s latency).
All 1000 scanned ports on ip-172-31-32-1.eu-central-1.compute.internal (172.31.32.1) are filtered
MAC Address: 06:9F:17:A8:82:2E (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 21.29 seconds
=======================FINISH===================================

=======================START====================================
Opened TCP ports on host 172.31.42.168

Starting Nmap 7.01 ( https://nmap.org ) at 2021-02-16 21:13 UTC
Nmap scan report for ip-172-31-42-168.eu-central-1.compute.internal (172.31.42.168)
Host is up (0.00040s latency).
Not shown: 997 filtered ports
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   closed http
8080/tcp closed http-proxy
MAC Address: 06:58:3B:2C:F1:D0 (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 10.25 seconds
=======================FINISH===================================

=======================START====================================
Opened TCP ports on host 172.31.46.205

Starting Nmap 7.01 ( https://nmap.org ) at 2021-02-16 21:13 UTC
Nmap scan report for ip-172-31-46-205.eu-central-1.compute.internal (172.31.46.205)
Host is up (0.00038s latency).
Not shown: 997 filtered ports
PORT     STATE  SERVICE
22/tcp   open   ssh
80/tcp   closed http
8080/tcp closed http-proxy
MAC Address: 06:23:1D:CF:E2:BE (Unknown)

Nmap done: 1 IP address (1 host up) scanned in 10.25 seconds
=======================FINISH===================================

=======================START====================================
Opened TCP ports on host 172.31.33.124

Starting Nmap 7.01 ( https://nmap.org ) at 2021-02-16 21:13 UTC
Nmap scan report for ip-172-31-33-124.eu-central-1.compute.internal (172.31.33.124)
Host is up (0.0000090s latency).
Not shown: 996 closed ports
PORT     STATE SERVICE
22/tcp   open  ssh
3306/tcp open  mysql
8080/tcp open  http-proxy
9100/tcp open  jetdirect

Nmap done: 1 IP address (1 host up) scanned in 1.58 seconds
=======================FINISH===================================

