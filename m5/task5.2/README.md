### Task 2.  

#### 1. /etc/passwd and /etc/group  

```
[ruslan@cnt7 ~]$ cat /etc/passwd
root:x:0:0:root:/root:/bin/bash
bin:x:1:1:bin:/bin:/sbin/nologin
daemon:x:2:2:daemon:/sbin:/sbin/nologin
......................................
sync:x:5:0:sync:/sbin:/bin/sync
```
Structure of /etc/passwd:  
- username
- password
- numeric identifier of the user account (UID)
- numeric identifier of the group to which the user belongs
- text description (comments) of the user
- the location of the user's HOME directory
- the default user's command interpreter  




