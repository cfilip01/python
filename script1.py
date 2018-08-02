import datetime
import boto3

client = boto3.client('athena')

response = client.batch_get_query_execution(
	QueryExecutionIds=[
		'SHOW SCHEMAS',
	]
)

#start_date = datetime.date( year = 2018, month = 9, day = 1, hour = 8 )
#end_date = datetime.date( year = 2020, month = 9, day = 1, hour = 8)

#s3 = boto3.resource('s3')
#for bucket in s3.buckets.all():
#	print(bucket.name)

