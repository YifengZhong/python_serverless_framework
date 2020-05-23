# python_serverless_framework

## Description
This is a project using Python, Serverless Framework and serverless offline plugin.

## Environment
Windows, Visual Stuido Code, Git bash,Python 3.7

## Steps
1. Install Python
2. Install virtualenv: pip3 install virtualenv
3. Open windows CLI.
4. Go into python_serverless_framework run virtualenv by type "virtualenv -p python3 venv" 
5. start virtual environment "venv\Scripts\activate.bat"
6. config your AWS security key and security id into credential file  \download\credential
7. npm install -g serverless
8. configure serverless with command 'serverless config credentials --provider aws --key <ACCESS KEY ID> --secret <SECRET KEY>'
9. if there is no project, use "serverless create --template aws-python3 --name hello-world" to create starter project.
10. serverless deploy --aws-profile serverless to deploy project, note serverless is the one label in /download/credential like
	<code>
		[serverless]
		aws_access_key_id = XXXXXXX
		aws_secret_access_key = XXXXXXXXXXXXX
	</code>

## Features
1. offline debug
2. Separate prod build and develp build	
	
## Use Serverless-offline
Refer to https://www.npmjs.com/package/serverless-offline-python

## Source Knowledge 
Refer to https://medium.com/faun/aws-lambda-serverless-framework-python-part-1-a-step-by-step-hello-world-4182202aba4a
