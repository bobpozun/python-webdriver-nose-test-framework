
# Test Automation

**Dependencies**
- Install Python
- Install pip: `easy_install pip` or upgrade `pip install --upgrade pip`
- Install dependencies: `pip install -r requirements.txt`

**Notes**
- chromedriver.exe in source is for win32.You must download the appropriate driver for your system here:https://sites.google.com/a/chromium.org/chromedriver/ and add it to your PATH.

**Run Example**

*All Selenium Tests:*

`nosetests -v --with-xunit --tc-file=cfg/google-com.cfg`

*To run a Specific Selenium Test File:*

`nosetests -v --with-xunit --tc-file=cfg/google-com.cfg test.py`

*To run a subset of tests based on a test @attr like smoke or regression:*

`--attr=smoke`
- Example
  - `nosetests -v --with-xunit --tc-file=cfg/google-com.cfg test.py --attr=smoke`

*To run a Class of Selenium Tests:*

`nosetests -v --with-xunit --tc-file=cfg/google-com.cfg test.py:Basic`

*To run a single Selenium Test:*

`nosetests -v --with-xunit --tc-file=cfg/google-com.cfg test.py:Basic.open_page`
