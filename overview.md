# Graph Theory Project Overview - Jack Haugh - G00359747

# Introduction
Hi there my name is Jack Haugh and i'm a current Third Year Software Development student at Galway-Mayo Institute of Technology. I will be giving you a overview of the module Graph Theory and the project we did for the module which was to execute regular expressions on strings using an algorithm known as Thompson’s construction while using the language python.</br>
We done the coding on Google cloud platform as it was used in conjunction with a linux machine and our work was uploaded to github to save our work and show progress. Python is a great language as it's an open source which means its free to use for personal and comercial purposes ease of use with the simplicity of their syntex and rules to faciliate code. </br>
What happened with the code was to take a NFA infix and convert it into a postfix expression using the shunting yard algorithm. An NFA infix means a Non-Deterministic Finite automaton that are used for regular expressions and the shunting yard algorithm is a parsing method for expressionsin infix notation. </br>
The file that we run when we clone the repository is myscript.py that runs the code from regex.py to see if code in that is correct and doesnt show errors.</br>

# Run
This project had many steps involved from the creation of the project to the finalizing the document for completion of project. For starters we used Google cloud platform to create a linux machine to do code. A suite of cloud computing services that runs on the same infrastructure that Google uses internally for its end-user products. I found google cloud platform great to use as your running a machine from the cloud where your pc specs good or bad won't have a huge effect on that machine compared to a local machine and great for others if group projects to use together. The steps follow as 
1. Create a google cloud platform account and you need to get credits to run the machines which come free with colleges. 
2. Go to VM Instances and create a new one. 
3. Then on create menu change region to europe west2, change boot disk to Debian GNU/Linux 10 and keep all other settings the same then and create it. 
4. Click on three dots on side of vm tab and click start and then click the SSH button under connect to launch the vm. 
5. You then come to the cmd of linux with lines of writing on the window and you can start typing. 
6. Type "sudo apt update" to update debian to the latest stuff for use, the upgrade it using "sudo apt upgrade". 
7. Next you need to install Git and gcc so first "sudo app install git", then "sudo apt install build-essential", "sudo apt install wget". 
8. Then if you want to for example use my code then we need to use git clone https://github.com/JackH97/Graph-Theory-Project which will clone my project to your vm to use. 
9. Then cd Graph-Theory-Project to go into that folder then cd thompson to go into that folder and then theres a command called vi which when you create a new file you use vi "".py which will let you create a new python file and if theres .py files in folder already just use same command and the file name. 
10. To run the file then use python3 "".py to run the fill and if works it outputs to the screen.
