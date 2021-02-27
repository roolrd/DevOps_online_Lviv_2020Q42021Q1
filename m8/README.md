## Task 8  

There is github repository with java aplication:  

![8.1](./scr/2021-02-27_132347.jpg)  

Create freestile Jenkins-job "Cheking_base_of_product". Install such plugins - "Deploy to container", "Generic Webhook Trigger Plugin". Then configure job:
- add into option "Git" url of github repository

![8.2](./scr/2021-02-27_132520.jpg)  

- add build stages

![8.3](./scr/2021-02-27_132546.jpg)  

- configure post-build action for Tomcat-server

![8.4](./scr/2021-02-27_132604.jpg)  

![8.5](./scr/2021-02-27_135328.jpg)  

- configure connection GitHub<->Jenkins

![8.6](./scr/2021-02-27_141226.jpg)  

- configure github project and webhook pipeline

![8.7](./scr/2021-02-27_144953.jpg)  

![8.8](./scr/2021-02-27_145847.jpg)  

![8.9](./scr/2021-02-27_150356.jpg)  

- try to make some shange in the java app

![8.10](./scr/2021-02-27_150617.jpg)  

![8.11](./scr/2021-02-27_150717.jpg)  

![8.12](./scr/2021-02-27_150902.jpg)  

![8.13](./scr/2021-02-27_151022.jpg)  

![8.14](./scr/2021-02-27_151406.jpg)  

![8.15](./scr/2021-02-27_152605.jpg)  

![8.16](./scr/2021-02-27_152624.jpg)  

![8.17](./scr/2021-02-27_152647.jpg)  




===========================================
Jenkins 
SSH Build Agents. This plugin is formerly known as "SSH Slaves Plugin". It was renamed in 1.32.0, but the plugin ID was retained as ssh-slaves to retain compatibility for the plugin users.
Перевірити чи може запускатись білд на мастері якщо не вказати лейбли