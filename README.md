# Python AWS Rekognition

A simple project written in Python that uses AWS Rekognition to detect objects.

## Example

To see an example of the result, you can check the `example` folder.

## Requirements

- Python 3
- An AWS account and user with permissions to use AWS Rekognition programatically
- AWS CLI
- An `example.jpg` file inside the `dev` folder

## How to use

```sh
# Install the required packages
> pip install -r requirements.txt

# Configure your AWS credentials
> aws configure

# Run the project
> python main.py
```

## How to use without the AWS CLI

If you don't have the AWS CLI installed, you can create the `credentials` file using `touch ~/.aws/credentials`.

Then you can add the lines below inside that file.

```
[default]
aws_access_key_id = <access-key>
aws_secret_access_key = <secret-key>
```
