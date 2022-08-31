This tool is used for send useful information via telegram. 

Installation

Install package installer for python

apt-get install python3-pip -y

Download python script and make the file executable

wget https://raw.githubusercontent.com/bobu4/notifications_bot/main/bot.py ; chmod +x bot.py

Download dependencies file and install 

wget https://raw.githubusercontent.com/bobu4/notifications_bot/main/requirements.txt ; pip3 install -r requirements.txt ; rm requirements.txt

That's all. Now you can use this tool for your tasks.

Usage

First you need to change name in bot.py

![image](https://user-images.githubusercontent.com/48527047/187607929-3658289c-ef54-450a-a603-623188a7b3ca.png)
Write your telegram username instead of Example_name

Then go to https://t.me/Mantcbot and click start

To send message you need to run command

python3 bot.py "YOUR MESSAGE HERE"

Example

Create a bash script that run loop and increment variable and send variable to telegram


#!/usr/bin/env bash
for i in {1..20}
do
    python3 bot.py "$i"
done

![image](https://user-images.githubusercontent.com/48527047/187609916-4445724d-af5f-4a40-8159-4fc11c6ce3ea.png)

We have got all variable values
