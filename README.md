# AWS-Bash-Projects

## S3 Backup Script

## Description:
Creating a Bash script that automates the backup of local files or directories to an AWS S3 bucket. I used the AWS CLI to interact with S3, upload files, and manage the backup process.

## Steps:

- I made sure to set up AWS CLI with my access and secret keys,alongside the default region.
- Furthermore, I created the Bash script.
- Made sure that the script was executable using  `chmod u+x backup_script.`
- I ran the script: `./bin/S3/backup_script.`


## Services Used:
- AWS CLI
- AWS S3


## Precautions
One of the safety measures I had to take was ensuring my AWS Credentials was secure by creating a `.env`file. Also, ensuring that the bucket policies and IAM permissions were correctly configured. 


## Challenges 
I had to ensure proper handling of files and permissions.This was the main challenge for me, and handling errors when creating the script for the backup process 
