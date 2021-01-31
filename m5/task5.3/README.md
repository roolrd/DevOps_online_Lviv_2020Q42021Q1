### Task 5.3  

#### 1. How many states could has a process in Linux?  

Basically, there are Five main process states - Running (R), Interruptible sleep (S) - process is waiting for some event, Stop (T) - process is stopped, Zombie (Z) - state between (exit) and (wait) , Uninterruptible sleep (D) - process is waiting for fo input-output after it's requested somewhere.  

#### 2. Examine the pstree command.  
```
buntu@ip-172-31-33-124:~$ pstree
systemd─┬─accounts-daemon─┬─{gdbus}
        │                 └─{gmain}
        ├─acpid
        ├─2*[agetty]
        ├─amazon-ssm-agen─┬─ssm-agent-worke───8*[{ssm-agent-worke}]
        │                 └─7*[{amazon-ssm-agen}]
        ├─atd
        ├─containerd───8*[{containerd}]
        ├─cron
        ├─dbus-daemon
        ├─dhclient
        ├─dockerd─┬─docker-containe─┬─docker-containe─┬─docker-volume-s───3*[{docker-volume-s}]
        │         │                 │                 └─8*[{docker-containe}]
        │         │                 └─9*[{docker-containe}]
        │         └─12*[{dockerd}]
        ├─gitlab-runner───7*[{gitlab-runner}]
        ├─2*[iscsid]
        ├─lvmetad
        ├─lxcfs───10*[{lxcfs}]
        ├─mdadm
        ├─mysqld─┬─36*[{mysqld}]
        │        ├─{xpl_worker0}
        │        └─{xpl_worker1}
        ├─node_exporter───3*[{node_exporter}]
        ├─polkitd─┬─{gdbus}
        │         └─{gmain}
        ├─rsyslogd─┬─{in:imklog}
        │          ├─{in:imuxsock}
        │          └─{rs:main Q:Reg}
        ├─snapd───8*[{snapd}]
        ├─sshd─┬─sshd───sshd───bash───pstree
        │      └─sshd───sshd───sftp-server
        ├─systemd───(sd-pam)
        ├─systemd-journal
        ├─systemd-logind
        ├─systemd-timesyn───{sd-resolve}
        ├─systemd-udevd
        └─unattended-upgr───{gmain}

ubuntu@ip-172-31-33-124:~$ pstree -h | grep bash
        |-sshd-+-sshd---sshd---bash-+-grep
```

#### 3. What is a proc file system?  
The filesystem /proc stores information about processes on the OS.  

#### 4. Print information about the processor  
```
ubuntu@ip-172-31-33-124:~$ lscpu
Architecture:          x86_64
CPU op-mode(s):        32-bit, 64-bit
Byte Order:            Little Endian
CPU(s):                1
On-line CPU(s) list:   0
Thread(s) per core:    1
Core(s) per socket:    1
Socket(s):             1
NUMA node(s):          1
Vendor ID:             GenuineIntel
CPU family:            6
Model:                 63
Model name:            Intel(R) Xeon(R) CPU E5-2676 v3 @ 2.40GHz
Stepping:              2
CPU MHz:               2400.082
BogoMIPS:              4800.16
Hypervisor vendor:     Xen
Virtualization type:   full
L1d cache:             32K
L1i cache:             32K
L2 cache:              256K
L3 cache:              30720K
```

#### 5. Use the ps command to get information about the process  
```
ps -e --format="pid ppid uname cmd group %cpu %mem stat" | head
  PID  PPID USER     CMD                         GROUP    %CPU %MEM STAT
    1     0 root     /sbin/init                  root      0.0  0.5 Ss
    2     0 root     [kthreadd]                  root      0.0  0.0 S
    3     2 root     [ksoftirqd/0]               root      0.0  0.0 S
    5     2 root     [kworker/0:0H]              root      0.0  0.0 S<
    6     2 root     [kworker/u30:0]             root      0.0  0.0 S
    7     2 root     [rcu_sched]                 root      0.0  0.0 S
    8     2 root     [rcu_bh]                    root      0.0  0.0 S
    9     2 root     [migration/0]               root      0.0  0.0 S
   10     2 root     [watchdog/0]                root      0.0  0.0 S
```

#### 6. How to define kernel processes and user processes?  
The kernel creates a process tree with two main branches: a process with PID(process identifier) = 2 (in ubuntu 18.04 and CenOS7 called "kthreadd") is assigned as the parent for all kernel processes; the process with PID = 1 (for example - init) is assigned as the parent for all user processes. We can see the names of kernel processes between square brackets when we call the "ps aux" command.  

#### 7. Print the list of processes to the terminal. Briefly describe the statuses of the processes.  
```
ubuntu@ip-172-31-33-124:~$ ps aux
USER       PID %CPU %MEM    VSZ   RSS TTY     STAT START   TIME COMMAND
root         1  0.0  0.5  37764  5188 ?        Ss   Jan22   0:05 /sbin/init
root         2  0.0  0.0      0     0 ?        S    Jan22   0:00 [kthreadd]
root         3  0.0  0.0      0     0 ?        S    Jan22   0:01 [ksoftirqd/0]
root         5  0.0  0.0      0     0 ?        S<   Jan22   0:00 [kworker/0:0H]
................................................................................
root        19  0.0  0.0      0     0 ?        SN   Jan22   0:00 [ksmd]
root        20  0.0  0.0      0     0 ?        SN   Jan22   0:00 [khugepaged]
................................................................................
systemd+   723  0.0  0.2 100320  2208 ?        Ssl  Jan22   0:00 /lib/systemd/systemd-timesyncd
root      1218  0.0  0.9 138840  9796 ?        Ssl  Jan22   1:27 /usr/bin/gitlab-runner run --working-directory /home/gitla
root      1219  0.0  0.0   5216   116 ?        Ss   Jan22   0:12 /sbin/iscsid
root      1220  0.0  0.3   5716  3520 ?        S<Ls Jan22   1:00 /sbin/iscsid
root      1441  0.0  0.1  14468  1712 ttyS0    Ss+  Jan22   0:00 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt220
root      1453  0.0  0.1  14652  1372 tty1     Ss+  Jan22   0:00 /sbin/agetty --noclear tty1 linux
mysql     1480  0.1 32.8 1296308 333008 ?      Ssl  Jan22  10:26 /usr/sbin/mysqld
root      1502  0.0  0.5 226704  5964 ?        Ssl  Jan22   5:06 docker-containerd -l unix:///var/run/docker/libcontainerd/
root      1551  0.0  0.0 207324   416 ?        Sl   Jan22   0:00 docker-containerd-shim cb594c448456313d1fa120a372933277317
................................................................................
ubuntu    8824  0.0  0.3  36080  3312 pts/0    R+   15:11   0:00 ps aux
root     12587  0.0  0.0      0     0 ?        S    Jan23   0:05 [kworker/0:1]
root     23680  0.0  0.0      0     0 ?        S    02:55   0:00 [kworker/u30:1]
root     26128  0.0  0.0      0     0 ?        S    Jan28   0:00 [kworker/u30:2]
root     30670  0.0  0.0      0     0 ?        S<   Jan28   0:00 [xfsalloc]
root     30671  0.0  0.0      0     0 ?        S<   Jan28   0:00 [xfs_mru_cache]
```
Statuses (STAT)  
- S - process is sleeping
- R - process that is running or in the queue
- s - process is the session leader
- < - process has high priority
- N - process has low priority
- L - some pages are locked in memory
- + - process group in the background
- l - multi-threading process  

#### 8. Display only the processes of a specific user  
List of "ubuntu"-user processes  
```
ubuntu@ip-172-31-33-124:~$ ps -fu ubuntu
UID        PID  PPID  C STIME TTY          TIME CMD
ubuntu    6518     1  0 13:28 ?        00:00:00 /lib/systemd/systemd --user
ubuntu    6521  6518  0 13:28 ?        00:00:00 (sd-pam)
ubuntu    6703  6516  0 13:28 ?        00:00:00 sshd: ubuntu@notty
ubuntu    6704  6514  0 13:28 ?        00:00:00 sshd: ubuntu@pts/0
ubuntu    6709  6703  0 13:28 ?        00:00:00 /usr/lib/openssh/sftp-server
ubuntu    6711  6704  0 13:28 pts/0    00:00:00 -bash
ubuntu   11295  6711  0 16:41 pts/0    00:00:00 ps -fu ubuntu
```

#### 9. What utilities can be used to analyze existing running tasks (by analyzing the help for the ps command)?  
- "pgrep" utility was created to removing the need to call grep with ps.  
```
ubuntu@ip-172-31-33-124:~$ pgrep docker -l
1227 dockerd
1502 docker-containe
1551 docker-containe
1572 docker-volume-s
```
- "pkill" - command pkill is similar to pgrep in that it can search by name and will send the specified signal (by default SIGTERM) to each process.  
```
ubuntu@ip-172-31-33-124:~$ sudo pkill docker
ubuntu@ip-172-31-33-124:~$ pgrep docker -l
ubuntu@ip-172-31-33-124:~$
```
- pidof. This command will check the PID of a specific binary even if another process with the same name is running  

#### 10. What information does top command display?  
The top command is using for real-time viewing details of running processes and quickly identifying issues with memory, CPU, etc.  

#### 11. Display the processes of the specific user using the top command  

![1.11](./scr/2021-01-![2021-01-31_213141.jpg)  




