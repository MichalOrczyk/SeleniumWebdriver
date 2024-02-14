<h1>Summary</h1>
<p>The files posted here perform various operations using the Selenium Webdriver library and are written in Python.</p>
<p><b>GoogleSearch.py</b> searches for the term in the browser, goes to the Wikipedia page and retrieves basic information about the term. <b>GoogleSearch_test.py</b> does the same thing, but returns information about whether the test passed or failed.</p>
<p><b>GitHub_Login_Logout.py</b> logs you into GitHub and logs you out of it after a while. For the script to work properly, you must enter your GitHub login and password in the file. <b>GitHub_Login_Logout_test.py</b> does the same thing, but returns information about whether the test passed or failed.</p>

<h1>Installation</h1>
For scripts to work properly, the following are required:
<p></p>
<p>* Python installed: https://www.python.org/downloads/</p>
<p>* Chrome browser installed: https://www.google.com/chrome/</p>
<p>* Selenium library installed (same version as Chrome browser version): https://selenium-python.readthedocs.io/installation.html</p>
<p>* Webdriver-manager installed: https://pypi.org/project/webdriver-manager/</p>
<p>* Pytest installed: https://docs.pytest.org/en/7.1.x/getting-started.html/</p>

<h1>Starting up</h1>
Go to the directory where scripts are located.
<h2>Linux</h2>
Launch the console and type:
python3 [filename] to run the script or - to perform test with pytest - pytest [filename ending with _test]

<h2>Windows</h2>
Run cmd.exe and type:
python [filename] to run the script or - to perform test with pytest - pytest [filename ending with _test]
