import boto3

ecr_client = boto3.client('ecr', region_name='us-east-1')
repository_name = "my-cloud-repo"
response = ecr_client.create_repository(repositoryName = repository_name)
repositoyr_uri = response['repository']['repositoryUri']
print(repositoyr_uri)