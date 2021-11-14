# Report task 2.2

**Dmytro Kubai**

I registered an AWS Free Tier account. Then I started an Amazon Linux VM with Amazon Lightsail and connected to it.
![screenshot](screenshots/1.png)
Then I launched another VM without Amazon Lightsail with t2.micro instance. 
![](screenshots/2.png)
I saved ssh key, converted it by PuTTY key generator and connected to my VM with PuTTY.
![](screenshots/3.png)
I created a new snapshot.
![](screenshots/4.png)
Created and attached Disk_D
![](screenshots/5.png)
Created file system on new volume. Then i created data folder and mounted Disk_D on it.
```
sudo mount /dev/xvdf /data
```
Created few files 
![](screenshots/6.png)
I created image from snapshot and launched a new instance, using it.
![](screenshots/7.png)

I detached disk D from old instance and attached it to the new VM.

![](screenshots/8.png)
I mounted disk D to the directory data.
![](screenshots/9.png)
In folder data we can see files, which I have created on previous steps.
![](screenshots/10.png)
Launched WordPress instance with Amazon Lightsail
![](screenshots/11.png)
Created bucket and uploded a file to it.
![](screenshots/12.png)
I created a user AWS IAM, configured CLI AWS and uploaded file to my bucket.
![](screenshots/13.png)