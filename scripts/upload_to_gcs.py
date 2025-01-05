import os
from google.cloud import storage

def upload_to_gcs(bucket_name, source_folder):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)

    for root, _, files in os.walk(source_folder):
        for file in files:
            local_path = os.path.join(root, file)
            blob = bucket.blob(file)
            blob.upload_from_filename(local_path)
            print(f'Uploaded {file} to {bucket_name}')

if __name__ == "__main__":
    bucket_name = "otsuka-bucket"
    source_folder = "csv"
    upload_to_gcs(bucket_name, source_folder)
