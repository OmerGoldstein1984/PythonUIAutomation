Welcome to my python automation ui framework with the following:
Selenium,pytest,allure reports and parallel executing and run on "different" environments and get values from configuration file from CLI 
before running tests execute pip install requirments.txt

user defined arguments:
--browsername: ch|ff ch=chrome ff=firefox
--env: get values from test or production

the -n=4 is run few tests in parallel mode
For example to run on chrome with "test" enviroment run from cli the following:
pytest --alluredir=report  -n=4 --browsername=ch --env=test 

after execution is finish you can see a report by executing 
allure serve report 

the automation can run on CI servers 
