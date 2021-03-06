# bs4_in_lambda
-----------------------
## Description

The purpose of this script is to show how to use the Beautiful Soup module in AWS Lambda with Python Runtimes. 
Keep in mind, AWS Lambda is not integrated with all the modules available for Python. And the only way to
import the modules to Lambda is to bundle the lambda function alongside the modules in an isolated environment.
The idea is similar to containers, we create an isolated environment, we import only the dependencies we need
to make our application working, we write our code, we bundle it and we export it to the Cloud.   


## Step1) Install Pipenv


Pipenv is the module that will enable us to create an isolated environment for our lambda function.

For Debian:
```
sudo apt update -y
sudo apt upgrade -y
sudo apt install python-pip
pip3 install pipenv 
```

For RPM:

```
sudo apt update -y
sudo apt upgrade -y
sudo yum install python-pip
```

## Step2) Create a Python 3.8 environment

At the time I am writing, the documentation for Beautiful Soup has been written for Python 3.8 https://www.crummy.com/software/BeautifulSoup/bs4/doc/ . As result, 
we need a Python 3.8 isolated environment. Let's create it:

```
pipenv --python 3.8
pipenv shell
```
## Step3 Install our bs4 dependency

```
pip install bs4
```
## Step4 Copy and Paste the lambda function to your virtual environment

```
cp lambda_function.py ~/.local/share/virtualenvs/<yourenvname>/lib/python3.8/site-packages
cd ~/.local/share/virtualenvs/<yourenvname>/lib/python3.8/site-packages
ls 
```

## Step5 Bundle up the lambda function and the dependencies

```
zip -r9 bs4_in_lambda.zip *
cp bs4_in_lambda.zip ~/Desktop
cd  ~/Desktop
ls *zip
```
## Step6 Upload the Zip File to your Lambda Function

Create a Lambda Function

Make sure you select Python3.8 Runtime

Go to Code and in the top right corner click on Upload from

And select the Zip file we have created

The Lambda function will show up and we can see on the left side all the pip packages stored in folders

Then go to Configuration and increase the runtime becaUse there are 5 pages to be scrapped

Let's set 5 minutes runtime to make sure it will scrape all the pages

Then Go back to Code > Press Test 

Leave the Configuration Test content by default and add any name on Event name and Save

Click Test

And sometimes we will get this error message

The trick is to swtich betwwen http and https in our function
Press Ctrl + F Scroll Down and replace all https with http, Deploy and Test the Function  
Et Voila!

Then Go to Monitor > Logs > Click in the LogStream of the first invocation, a new window will open
and you will get access to the full list


 
