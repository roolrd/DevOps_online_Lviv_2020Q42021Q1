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
UID range, as usual - 0 to 65535. UID - unique "user identifier" on the Unix-like OS, a number that is used to identify the user to the system and to determine which system resources the user can access. We can define it using the 'id'-command and on the file /etc/passwd.  

#### 3. GID  
It's a numeric "group identifier" on the Unix-like OS. We can define GID of specific group using the file /etc/group (section #3 of each line).  

#### 4. How to determine belonging of user to the specific group  
We can use "id" and "groups". For example:
```
id -Gn <specific username>
groups <specific username>
```

#### 5. Adding a user to the system  


