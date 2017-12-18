# upass-automator

I wrote this script because I got tired of persuading the bus driver that I'm a university student every time I forgot to renew my U-PASS. Here's what you need:

## Make sure you have the dependencies
1. Download Selenium: `sudo pip install -U selenium`
2. Download Chromedriver and put it in your `PATH`. Click [here](https://sites.google.com/a/chromium.org/chromedriver/downloads) to download the latest version. To move Chromedriver to `PATH` on macOS, run `cp <path/to/chromedriver> /usr/local/bin`. 

## To run upass-automator
1. Run `python upass-request.py`
2. Enter your CWL credentials when prompted. <strong>Please note:</strong> I cannot be responsible for any security vulnerabilities that may occur when running this script, I initially wrote it for personal use. By your use of this script, you acknowledge the facts above.
3. Watch WebDriver execute the script!
4. Never get the stink-eye from the bus driver again.

## Future plans

This is a first pass at attempting to automate the UPASS renewal process. Of course, one still has to remember to run the script once a month. In the future, as a user I want to:

* Set the script up such that it runs automatically on the 16th of each month.

* Do some serious research on the security vulnerabilities that may be present with the current iteration. 