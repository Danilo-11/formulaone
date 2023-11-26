import json
import boto3

from helpers import get_raw_data_path

with open("config.json", "r") as f:
  config = json.load(f)

session = boto3.Session(
    aws_access_key_id = config["aws_access_key_id"],
    aws_secret_access_key = config["aws_secret_access_key"]
)

dynamo_resource = session.resource(
    'dynamodb',
    region_name='eu-west-1'
)

movies = dynamo_resource.Table('doc-example-table-movies')

raw_data_path = get_raw_data_path()
raw_data_path.mkdir(parents=True, exist_ok=True)

movies.get_item(0)

"""
with open(raw_data_path / 'current.json', 'w') as f:
    json.dump(movies, f)
"""