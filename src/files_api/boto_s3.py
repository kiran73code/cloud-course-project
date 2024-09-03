import boto3

BUCKET_NAME = "cloud-course-bucket-kiran"

session = boto3.Session(profile_name="cloud-course")

s3_client = session.client("s3")

# write object to bucket
s3_client.put_object(Bucket=BUCKET_NAME, 
        Key="folder/hello_world.txt",
        Body="hello world..!",
        ContentType= "text/plain"
        )
