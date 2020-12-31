### Create a network  

![1](./scr/2020-12-28_225943.jpg)

### Router configuration  

![2](./scr/2020-12-31_200237.jpg) 

![3](./scr/2020-12-31_200954.jpg)  

### Set a password  

```
Router>en
Router#conf t
Router(config)#enable secret 123456
Router(config)#exit
Router#copy running-config startup-config 
Destination filename [startup-config]? 
Building configuration...
[OK]
```

### RIP Config  

![5](./scr/2020-12-31_200954.jpg)  

### Check availability  

![6](./scr/2020-12-31_102659.jpg)

