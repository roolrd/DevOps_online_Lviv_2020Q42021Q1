## Task 6.1  

#### 2. VM2 has one interface (internal), VM1 has 2 interfaces (NAT and internal).  
Configure  all network interfaces in order to make VM2 has an access to the Internet (iptables, forward, masquerade)  

```
sudo nano /etc/network/interfaces
.....................
#internal
auto enp0s8
iface enp0s8 inet static
address 10.10.10.1
netmask 255.255.255.0
broadcast 10.10.0.255
```

![6.1](./scr/2021-02-10_164617.jpg)  

![6.2](./scr/2021-02-10_164257.jpg)  

![6.3](./scr/2021-02-10_164349.jpg)  

#save changes and restart network service  
sudo systemctl networking restart  

![6.4](./scr/2021-02-10_165949.jpg) 

```
# for VM2
sudo nano /etc/network/interfaces
.....................
#internal
auto enp0s3
iface enp0s3 inet static
address 10.10.10.2
netmask 255.255.255.0
broadcast 10.10.0.255
gateway 10.10.10.1
dns-nameservers 8.8.8.8
```

![6.5](./scr/2021-02-10_171040.jpg)  

![6.6](./scr/2021-02-10_171155.jpg)  

![6.7](./scr/2021-02-11_125357.jpg)  

For CentOS7 internal machine  

![6.5](./scr/2021-02-11_143158.jpg)  

![6.6](./scr/2021-02-11_143121.jpg)  

Iptables configurig:

```
sudo iptables -t nat -A POSTROUTING -o enp0s3 -j MASQUERADE
sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -m state --state RELATED,ESTABLISHED -j ACCEPT

#it can be works without
sudo iptables -A FORWARD -i enp0s8 -o enp0s3 -j ACCEPT
```

![6.8](./scr/2021-02-11_132842.jpg)  

```
#if we want the iptables rules work after reload host:
apt-get install iptables-persistent
#and agree with saving existing iptables rules
# notice - we need to restart system on VM1
```

#### 3. Check the route from VM2 to Host.  

Host-machine has IP - 192.168.0.163  

![6.9](./scr/2021-02-11_180145.jpg)  

Using "mtr"

![6.10](./scr/2021-02-11_180052.jpg)  

![6.9](./scr/2021-02-11_132842_1.jpg)  

![6.10](./scr/2021-02-11_132842_2.jpg)  

#### 4. Check the access to the Internet, (just ping, for example, 8.8.8.8).  

![6.11](./scr/2021-02-11_132843.jpg)  

![6.12](./scr/2021-02-11_132844.jpg)  

![6.13](./scr/2021-02-11_143056.jpg)  

#### 5. Determine, which  resource has an IP address 8.8.8.8.  

![6.14](./scr/2021-02-11_151444.jpg)  

#### 6. Determine, which  IP address belongs to resource epam.com.  

![6.15](./scr/2021-02-11_151613.jpg)  

#### 7. Determine the default gateway for your HOST and display routing table.  

![6.16](./scr/2021-02-11_162319.jpg)  

![6.17](./scr/2021-02-11_163344.jpg)  

![6.18](./scr/2021-02-11_162049.jpg)  

![6.19](./scr/2021-02-11_162154.jpg)  

#### 8. Trace the route to google.com  

Using "mtr" - utility

![6.20](./scr/2021-02-11_164411.jpg)  

using "traceroute"

![6.21](./scr/2021-02-11_164619.jpg)  

![6.21](./scr/2021-02-11_164902.jpg)  

