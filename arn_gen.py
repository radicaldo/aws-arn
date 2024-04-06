import aws_arn
import csv
from datetime import datetime


# Generate ARN using service and resource name
#print(aws_arn.generate_arn('i-1234568901', 'ec2', 'instance', 'us-east-1', '012345789012', 'aws')) 
#arn:aws:ec2:us-east-1:012345789012:instance/i-1234568901
#export tag csv from AWS Tag Editor console and place in root directory or specify path in "csv_file" variable. 


account = input("Enter the account id: ")
region = input("Enter the region: ")

LOG_FILE = "log.txt"
ERROR_LOG = "error_log.txt"

def write_to_log(message, is_error=False):
    log_file = ERROR_LOG if is_error else LOG_FILE
    with open(log_file, 'a') as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

#account = "yourAWSaccountID"
partition = "aws"
csv_file = "./resources.csv"
arn_output = "./arns.csv"

def format_gen(file_path):
    arn_list = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            resource_id = row['Identifier'].replace('/', '', 1)
            service = row['Service'].lower()
            sub_service = row['Type'].lower()
            region = row['Region']

            # Attempt to generate the ARN
            try:
                arn = aws_arn.generate_arn(resource_id, service, sub_service, region, account, partition)
                arn_list.append({'ResourceARN': arn})
            except KeyError as e:
                write_to_log(f"Error generating ARN for row: {row}, Error: {e}")

    return arn_list

def writeToCsv(arn_list):
    with open(arn_output, 'w', newline='') as output_file:
        fieldnames = ['ResourceARN']  
        writer = csv.DictWriter(output_file, fieldnames=fieldnames)
        writer.writeheader()
        for resource in arn_list:
            writer.writerow(resource)

arn_list = format_gen(csv_file)
writeToCsv(arn_list)

