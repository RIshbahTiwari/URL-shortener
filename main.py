# description before using the code

#before using this make sure you already have intall these two extensions :-
#1- pip install shortner
#2-pip install pyperclip
#for intalling these extensions use the followoing steps
#paste this line in terminal of your ide (ex-vscode,pycharm) :-
# 1st line ------>  pip install shortner  
# after this hit enter and then copy this and paste in terminal
#2nd line ---------> pip install pyperclip
# hit enter, and then use below code


# main code
#------->>>>

import pyshorteners

url = input("Enter the url \n: ")


def shortenurl(url):
    s = pyshorteners.Shortener()
    print(s.tinyurl.short(url))

shortenurl(url)
