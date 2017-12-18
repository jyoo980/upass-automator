# upass-automator

I wrote this script because I got tired of persuading the bus driver that I am a university student every time I forgot to renew my UPASS. Here's what you need:

## Make sure you have the dependencies
1. Download Selenium: `sudo pip install -U selenium`
2. Download the latest chromedriver and put it in your `PATH`. For macOS, `usr/local/bin` is where you want to put it

## To run upass-automator
1. Run `python upass-request.py`
2. Enter your CWL ID and Password when prompted. <strong>Note:</strong> I cannot be responsible for any security vulnerability this script exposes that information to, I initially wrote this as a personal side project. 
3. Never get the stink-eye from the bus driver again!

## Future plans

This is a first pass at attempting to automate the UPASS renewal process. Of course, one still has to remember to run the script once a month. In the future, as a user I want to:

* Set the script up such that it runs automatically on the 16th of each month.

* Do some serious research on the security vulnerabilities that may be present with the current iteration. 
