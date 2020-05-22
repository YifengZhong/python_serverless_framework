# python_serverless_framework

## Description
This is a project using Python, Serverless Framework and serverless offline plugin.

## Environment
Windows, Visual Stuido Code, Git bash,Python 3.7

## Steps
1. Install Python
2. Install virtualenv: pip3 install virtualenv
3. Open gitbash.
4. Go into python_serverless_framework run virtualenv by type "source ./venv/Scripts/activate"
5. config your AWS security key and security id into credential file  /download/credential
6. npm install -g serverless
7. configure serverless with command 'serverless config credentials --provider aws --key <ACCESS KEY ID> --secret <SECRET KEY>'
8. if there is no project, use "serverless create --template aws-python3 --name hello-world" to create starter project.
9. serverless deploy --aws-profile serverless to deploy project, note serverless is the one label in /download/credential like
	<code>
		[serverless]
		aws_access_key_id = XXXXXXX
		aws_secret_access_key = XXXXXXXXXXXXX
	</code>
