## Password Locker

## By CALEB KIMUTAI
        
## Description
.Application that help us manage passwords,displaying credentials for the user in created account,find credentials,also create and login to your account and generate new ones.

## Setup/Installation Requirements
.git fork/clone repository <br>
. git clone https://github.com/Calebu6214/Password-locker.git <br>
.Open the folder with vscode.<br>
.Run locally with terminal command.
.Push to github

## BDD
|Behaviour|Input|Output|
|--------|-------|------|
|Run the application in the terminal of your code editor|$ ./run.py|Hello what is your name?|
|input your name|name|Welcome name to Password locker what do you want to do? -ca - create a new account , lg - login to your account xx-exit
| input ca|input username,password and comfirm password|congratualtions username new account created.Proceed to login|
|input lg|input created username and password| logged in successfully where would you like to navigate to? sc-store your credentials, cr-create new credentials dc-display your credentials, dl-delete existing credentials, cc-copy cred credentials to clipboard,ex-logout|
input sc|input application name,username and password|your application name have been successfully saved|
input cr|input application name and username|Choose the following options: 1 - create my own password , 2 - let password locker generate a password for me|
|input dc|dc|Here is a list of all your credentials|
|input dd|enter the name application name of the credential to be deleted|application credentials has been successfully deleted|
|input cu|enter the application name of the credential you want to copy|application credentials have been successfully copied to clip board|
|input ex| ex|you are logged out ...bye|

## Known Bugs
 .No bugs

## Technologies Used
1. Python

### Contact And Support
For any questions and contribution get me through;
Email; calebkimutai97@gmail.com
Tel; +254707160385

### License
Copyright (c) 2021 **CALEB KIPNGETICH**