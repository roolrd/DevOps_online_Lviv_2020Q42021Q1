### Task 2.  

#### 1. /etc/passwd and /etc/group  

```
[ruslan@cnt7 ~]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
..................................
ruslan:x:1000:1000:Ruslan Riznyk,Home:/home/ruslan:/bin/bash
```
Structure of lines /etc/passwd:  
- username
- password
- numeric identifier of the user account (UID)
- numeric identifier of the group to which the user belongs
- text description (comments) of the user
- the location of the user's HOME directory
- the default user's command interpreter  

```
[ruslan@cnt7 ~]$ cat /etc/group
root:x:0:
bin:x:1:
daemon:x:2:
............
ruslan:x:1000:
```

Structure of lines /etc/group:
- group name
- group password
- numeric group identifier (GID)
- a list of user accounts that belong to the group  

On Linux are real users (people), which can sign in to the system, and pseudo-users (daemons, services), which can't login to the system.  There are such pseudo-users - bin, daemon, shutdown, which usually have UID in range 1-999, don't have password and commant interpreter.  

#### 2. UID  
UID range, as usual - 0 to 65535. UID - "user identifier" on the Unix-like OS, a number that is used to identify the user on the system and to determine which system resources the user can access. We can define it using the 'id'-command and on the file /etc/passwd.  
q
#### 3. GID  
It's a numeric "group identifier" on the Unix-like OS. We can define GID of specific group using the file /etc/group (section #3 of each line).  

#### 4. How to determine belonging of user to the specific group  
We can use "id" and "groups". For example:
```
id -Gn <specific username>
groups <specific username>
```
We can also look on the file /etc/group  

#### 5. Adding a user to the system  
```
sudo useradd -m(add home-directory) <specific username>
sudo adduser <specific username>
```

#### 6. How do I change the name (account name) of an existing user?  
```
sudo usermod -l <new username> <username>
```

#### 7. What is skell_dir?  
It's a "template" of structure and content user-home-directory when new user is created. Fles and subdirectories from /etc/skel directory will be copied into /home/<new user> directory.
Structure of /etc/skel directory on ubuntu 16.04:  
```
drwxr-xr-x 103 root root 4096 Jan 14 16:21 ..
-rw-r--r--   1 root root  220 Aug 31  2015 .bash_logout
-rw-r--r--   1 root root 3771 Aug 31  2015 .bashrc
-rw-r--r--   1 root root  655 Jul 12  2019 .profile
```
almost the same structure in other Linux  

#### 8. How to remove a user from the system (including his mailbox)?  
```
userdel -r <username>
deluser --remove-all-files <username>
```

#### 9. What commands and keys should be used to lock and unlock a user account?  

LOCK
```
usermod -L(--lock) <username>
or
passwd -l <username>
or
usermod -s /sbin/nologin
```

UNLOCK  
```
usermod -U(--unlock) <username>
or
passwd -u <username>
or
usermod -s /sbin/bash (or another shell)
```

#### 10. How to remove a user's password?  
```
sudo passwd -d <username>
```

#### 11. Display the extended format of information about the directory
```
[ruslan@cnt7 .ssh]$ ls -la
total 8
drwx------ 2 ruslan ruslan   38 Jan 23 10:42 .
drwx------ 3 ruslan ruslan  124 Jan 19 16:47 ..
-rw------- 1 ruslan ruslan 1675 Jan 23 10:42 id_rsa
-rw-r--r-- 1 ruslan ruslan  397 Jan 23 10:42 id_rsa.pub
```
- "total 8" - total file size on the directory (kB)
- first symbol "d" or "-" - file type: "d" - directory, "-" - regular file
- "rwx------" - the permissions granted to the owner of the file(1st triade), users who are members of the owner's group (2nd triade), to everyone else(3rd triade)
- number of hard links to the file
- name of the file owner
- name the file owner's group
- file size (bytes)
- date and time of last file access
- file name. "." - current directory, ".." - parent directory  

#### 12 & 13 What access rights exist and for whom (i. e., describe the main roles)? What is the sequence of defining the relationship between the file and the user?   
"rwx | rw- | r--"  
- r - read: the contents of the file may be read
- w - write: the contents of the file may be changed
- x - execute: The file may be executed (a program or a script)  
First triade - the permissions granted to the owner of the file (it's, usually, user who created the file).   Second - the permissions granted to users who are members of the owner's group. 
Third - the permissions granted to everyone else.  

There are also 3 additional permissions bits - the set-user-ID (s), set-group-ID (s), and sticky (t) bits
- s - set-user-id (SUID) - when a user executes a file, the program is run based on the permissions of the file owner. Set-group-ID (SGID) - the execution of the program is based on the group permissions of the file. For a directory, the directory group is used as the default group for new files created in the directory.
- t - sticky bit makes it possible to create a directory that is shared by many users, who can each create and delete their own files in the directory but can’t delete files owned by other users  

#### 14. What commands are used to change the owner of a file (directory), as well as the mode of access to the file?  

- changing of the file owner (and file owner's group) - command "chown"
```
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw-r--. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt

[ruslan@cnt7 test]$ sudo chown user2 file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw-r--. 1 user2 ruslan 5 Jan 23 13:32 file1.txt

#change both owner and group
[ruslan@cnt7 test]$ sudo chown user1.user2 file1.txt
#or
sudo chown user1:user2 file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw-r--. 1 user2 user1 5 Jan 23 13:32 file1.txt

#change group only
[ruslan@cnt7 test]$ sudo chown :ruslan file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw-r--. 1 user2 ruslan 5 Jan 23 13:32 file1.txt
```

- changing of the file owner's group - command "chgrp"
```
ruslan@cnt7 test]$ ls -l file2.txt
-rw-rw-r--. 1 ruslan ruslan 6 Jan 23 13:32 file2.txt

[ruslan@cnt7 test]$ chgrp wheel file2.txt
[ruslan@cnt7 test]$ ls -l file2.txt
-rw-rw-r--. 1 ruslan wheel 6 Jan 23 13:32 file2.txt

[ruslan@cnt7 test]$ sudo chgrp user1 file2.txt
[ruslan@cnt7 test]$ ls -l file2.txt
-rw-rw-r--. 1 ruslan user1 6 Jan 23 13:32 file2.txt
```

- changing mode access to the file - command "chmod"
```
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw-r--. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt

#rwx for all 
[ruslan@cnt7 test]$ chmod a+rwx file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rwxrwxrwx. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt

[ruslan@cnt7 test]$ chmod ug-x,o-rwx  file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw----. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt

[ruslan@cnt7 test]$ chmod ug-rw  file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
----------. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt

[ruslan@cnt7 test]$ chmod ug+rw  file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-rw----. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt
[ruslan@cnt7 test]$ chmod g=o  file1.txt
[ruslan@cnt7 test]$ ls -l file1.txt
-rw-------. 1 ruslan ruslan 5 Jan 23 13:32 file1.txt
```

#### 15. What is an example of octal representation of access rights? Umask.  

4 = r =  read
2 = w =  write
1 = x = execute
rw-rw-r-- - 0664
rwxrwxrwx - 0777
--------- - 0000
rwxr-x--x - 0751

The "umask"-command sets an octal attribute that specifies which permission bits should always be turned off when new files or directories are created by the process.  Shows the current value, if it's used without options and values.  

#### 16. Give definitions of sticky bits and mechanism of identifier substitution  

Setting "sticky bit" on a directory means that an unprivileged
users can remove or rename files (directories) in the directory only if it has write permission on the directory and owns either the file or the directory. The executable file for which the "sticky bit" is set remains (fixed) in memory after the end of the process.
```
drwxrwxrwt. 7 root root 93 Jan 23 14:26 /tmp/
```

Set User ID (SUID). When a user executes a file, the program runs based on the permissions of the file owner.
```
-rwsr-xr-x. 1 root root 27856 Apr  1  2020 /usr/bin/passwd
```

 Set Group ID (SGID). When applied to a file, the execution of the program is based on the group permissions of the file.
For a directory, the directory group is used as the default group for new files created in the directory.
```
-r-xr-sr-x. 1 root tty 15344 Jun 10  2014 /usr/bin/wall
drwxr-sr-x. 3 root systemd-journal 60 Jan 23 14:25 /run/log/journal
[ruslan@cnt7 test]$ ls -l /run/log/journal/68b9dc601af449909715222228ac0f9b/
total 6344
-rwxr-x---+ 1 root systemd-journal 6496256 Jan 23 16:34 system.journal
```

#### 17. What file attributes should be present in the command script?  
A file that contain command script must have at least the permissions of 0500 (-r-x------) and begin with the #! characters. 




