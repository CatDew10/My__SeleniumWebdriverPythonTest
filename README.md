# Allure_Installation

1. To install AllureReports type in Command line or Terminal(Mac):
pip install allure-pytest
or
pip3 install allure-pytest

2. Do "import AllureReports" to your test file

3. add to your test file footer:
if __name__ == "__main__":
    unittest.main(AllureReports)

4. Then get and install latest version of "AllureCMD" tool from zip file:
https://github.com/allure-framework/allure2/releases/

5. Add AllureCMD to your System Variables PATH like that:
C:\Users\username\Downloads\allure-2.22.1\bin
or
C:\allure-2.22.1\bin

For Mac users:
- Install "Brew" from here: https://brew.sh
using this command:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
- Then install Allure using this command with "Homebrew":
brew install allure

6. this step is optional:
Install Allure Command Line using "Scoop" or "Brew" (for Mac users)

Using Homebrew:
$ brew install allure

For Windows, Allure is available from the Scoop commandline-installer.
https://scoop.sh
To install Allure, download and install Scoop and then execute in the Powershell:
scoop install allure

Add Allure to your System Variables PATH (For Scoop install):
C:\Users\username\scoop\apps\allure\allure-2.20.1\bin

7. Then download and install latest "JavaSE" build:
https://www.oracle.com/technetwork/java/javase/downloads/

8. Add "Java" to your System Variables PATH like that:
Create new record with System variables: JAVA_HOME
then add path to your Java folder like that:
C:\Program Files\Java\jdk-20
or
JAVA_HOME / C:\Program Files\Java\jdk-20
then in your System PATH add new record like that:
%JAVA_HOME%\bin
or
set it from PyCharm terminal like:
setx -m JAVA_HOME "C:\Program Files\Java\jdk-20"

9. Check your Java is installed:
go to CMD or Terminal and type: java -version
you should see something like that:
java version "20.0.1"
Java(TM) SE Runtime Environment (build 20.0.1+9-29)
Java HotSpot(TM) 64-Bit Server VM (build 20.0.1+9-29, mixed mode, sharing)

10. Check your Allure is installed:
go to CMD or Terminal and type: allure --version
you should see something like that:
2.19.0

11. Check your Pytest is installed
go to CMD or Terminal and type: pytest --version
you should see something like that:
"pytest 7.2.2"

12. Add "AllureReports" folder to your Project root

13. To run AllureReports use from Terminal:
py.test --alluredir=./AllureReports ./unittest_Allure_reports.py
or
py.test --alluredir=C:/AllureReports ./unittest_Allure_reports.py

Next 2 steps is optional:
14. To generate History Trend run only one time:
allure generate --clean ./AllureReports

15. Copy "history" folder from your "allure-report" folder to "AllureReports" folder

16. To generate Reports use:
allure serve ./AllureReports
or
allure serve C:/AllureReports

17. To share Allure reports you need to run this command:
"allure generate"
from your Project folder, or run this command:
"allure generate --clean"
if your folder "allure-report" is not empty

18. Then you need to create (or use) your account on https://www.netlify.com/
After you'll create new account, you need to confirm your registration email.
Then drag and drop there "allure-report" folder to deploy website.

19. After website deployment it's ready to share by URL with your current Allure report.
Also you could rename your website for more clear name.

20. Use Allure official website if you have any questions: https://github.com/allure-framework
