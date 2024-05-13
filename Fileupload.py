import boto3

def upload_files_to_s3(file_names, bucket_name):
    try:
        # Initialize the S3 client with explicit credentials
        s3_client = boto3.client(
            's3',
            aws_access_key_id='your_access_key',
            aws_secret_access_key='your_secret_key'
        )

        for file_name in file_names:
            object_name = file_name

 
            s3_client.upload_file(file_name, bucket_name, object_name)
            print(f"File {file_name} uploaded successfully to bucket {bucket_name}")

        return True
    except Exception as e:
        print(f"Error uploading files to bucket {bucket_name}: {e}")
        return False

if __name__ == "__main__":
    file_names = ["Ball_By_Ball.csv", "Match.csv", "Player_match.csv", "Player.csv", "Team.csv"]  
    bucket_name = "your_bucket_name"  


    upload_files_to_s3(file_names, bucket_name)

