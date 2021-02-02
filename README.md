# README

## Installation

This uses VS Code's venv detection facility:

```
python -m venv venv
. venv/bin/activate
pip install chalice
```

## Running locally

```
chalice local
```

## Deploy

```
(venv) feldto a♥d♥u chalice deploy --profile FeldDotToChalice
Creating deployment package.
Reusing existing deployment package.
Creating IAM role: feldto-dev
Creating lambda function: feldto-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-west-2:070924157303:function:feldto-dev
  - Rest API URL: https://6bjvm1fdd6.execute-api.us-west-2.amazonaws.com/api/
```

## Accessing the AWS Console

In `1password` look up "AWS roygreenfelds account pydanny IAM user"