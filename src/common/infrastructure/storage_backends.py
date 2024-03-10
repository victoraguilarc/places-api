from environ import environ
from storages.backends.s3boto3 import S3Boto3Storage

env = environ.Env()
STORAGE_BUCKET_NAE = env('AWS_STORAGE_BUCKET_NAME')


class MediaStorage(S3Boto3Storage):
    bucket_name = STORAGE_BUCKET_NAE
    location = 'media'


class StaticStorage(S3Boto3Storage):
    bucket_name = STORAGE_BUCKET_NAE
    location = 'static'
