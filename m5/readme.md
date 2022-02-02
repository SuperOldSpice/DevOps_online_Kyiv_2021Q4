# Report task 5.1

**Dmytro Kubai**

# Part  1 

# 1-2 Log in to the system as root. Use the passwd command to change the password. Examine the basic parameters of the command. What system file does it change *?

I logged into systeam as root user. And then changed my password with `passwd` command. This command changes the /etc/passwd file, which stores user account information.

![pic1](screenshots/1.png)

#3) Determine the users registered in the system, as well as what commands they execute. What additional information can be gleaned from the command execution?

I checked list of the users 

![pic2](screenshots/2.png)

Command displays too:
- The current system time.
- The length of time the system has been up.
- The number of logged-in users.
- The system load averages for the past 1, 5, and 15 minutes. (the number of jobs that are currently running or waiting for disk)
- USER – The name of the logged user.
- TTY – The name of the terminal used by the user.
- FROM – The host name or IP address from where the user is logged in.
- LOGIN@ – The time when the user logged in.
- IDLE – The time since the user last interacted with the terminal. Idle time.
- JCPU – The time used by all processes attached to the tty.
- PCPU – The time used by the user’s current process. The one displayed in the WHAT field.
- WHAT – The user’s current process and options/arguments.

# 4) Change personal information about yourself.

![pic3](screenshots/3.png)

# 5) Become familiar with the Linux help system and the man and info commands. Get help on the previously discussed commands, define and describe any two keys for these commands. Give examples.

![pic4](screenshots/4.png)
![pic5](screenshots/5.png)

# 6) Explore the more and less commands using the help system. View the contents of files .bash* using commands.

![pic6](screenshots/6.png)
![pic7](screenshots/7.png)

# 7) Describe in plans that you are working on laboratory work 1. Tip: You should read the documentation for the finger command.

![pic8](screenshots/8.png)

# 8) List the contents of the home directory using the ls command, define its files and directories. Hint: Use the help system to familiarize yourself with the ls command.

![pic9](screenshots/9.png)

# Part2

# 1) Examine the tree command. Master the technique of applying a template, for example, display all files that contain a character c, or files that contain a specific sequence of characters. List subdirectories of the root directory up to and including the second nesting level.

![pic10](screenshots/10.png)
![pic11](screenshots/11.png)

# 2) What command can be used to determine the type of file (for example, text or binary)? Give an example.

![pic12](screenshots/12.png)

# 3) Master the skills of navigating the file system using relative and absolute paths. How can you go back to your home directory from anywhere in the filesystem?

![pic13](screenshots/13.png)

# 4) Become familiar with the various options for the ls command. Give examples of listing directories using different keys. Explain the information displayed on the terminal using the -l and -a switches

`-l` displays detailed information about the files.
`-a` shows hidden files.

![pic14](screenshots/14.png)
![pic15](screenshots/15.png)

# 5) Perform the following sequence of operations: - create a subdirectory in the home directory; - in this subdirectory create a file containing information about directories located in the root directory (using I/O redirection operations);
- view the created file;
- copy the created file to your home directory using relative and absolute addressing.
- delete the previously created subdirectory with the file requesting removal;
- delete the file copied to the home directory.

![pic16](screenshots/16.png)
![pic17](screenshots/17.png)

# 6) Perform the following sequence of operations:
- create a subdirectory test in the home directory;
- copy the .bash_history file to this directory while changing its name to labwork2;
- create a hard and soft link to the labwork2 file in the test subdirectory;
- how to define soft and hard link, what do these
concepts;
- change the data by opening a symbolic link. What changes will happen and why
- rename the hard link file to hard_lnk_labwork2;
- rename the soft link file to symb_lnk_labwork2 file;
- then delete the labwork2. What changes have occurred and why?

![pic18](screenshots/18.png)

Hard link referencesto to the spot on a hard drive where the Inode stores the data. A soft link points to the name of the original file.

![pic19](screenshots/19.png)
![pic20](screenshots/20.png)

# 7) Using the locate utility, find all files that contain the squid and traceroute sequence.

![pic21](screenshots/21.png)

# 8) Determine which partitions are mounted in the system, as well as the types of these partitions.

![pic22](screenshots/22.png)

# 9) Count the number of lines containing a given sequence of characters in a given file.

![pic23](screenshots/23.png)

# 10) Using the find command, find all files in the /etc directory containing the host character sequence.

![pic24](screenshots/24.png)

# 11) List all objects in /etc that contain the ss character sequence. How can I duplicate a similar command using a bunch of grep?

![pic25](screenshots/25.png)

![pic26](screenshots/26.png)

# 12) Organize a screen-by-screen print of the contents of the /etc directory. Hint: You must use stream redirection operations.

![pic27](screenshots/27.png)

# 13) What are the types of devices and how to determine the type of device? Give examples.

Devices types: 
c - character
b - block
p - pipe
s - socket

![pic28](screenshots/28.png)

# 14) How to determine the type of file in the system, what types of files are there?

Regular files ('-')
Directory files ('d')
Special files (5 types)
Block file('b')
Character device file('c')
Named pipe file or just a pipe file('p')
Symbolic link file('l')
Socket file('s')

![pic29](screenshots/29.png)

# 15) List the first 5 directory files that were recently accessed in the /etc directory.

![pic30](screenshots/30.png)