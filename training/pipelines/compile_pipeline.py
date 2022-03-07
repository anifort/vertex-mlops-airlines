from google.cloud import storage
import os

from argparse import ArgumentParser
from training_pipeline import compile_pipeline



def upload(destination, pipeline_filename):
    uri = destination[5:]
    uri_parts = uri.split("/")
    bucket_name = uri_parts[0]
    source_blob_name = "/".join(uri_parts[1:])

    blob = storage.Client().bucket(bucket_name).blob("/".join(uri_parts[1:]))
    blob.upload_from_filename(pipeline_filename)
    

'''
example:
python3 compile-pipeline.py -d gs://feature-store-mars21/test/pipeline.json
'''
if __name__ == "__main__":
    
    parser = ArgumentParser()
    parser.add_argument("-d", "--dest",
                        dest="destination",
                        required=True,
                        help="gs:// path to export pipeline including the archived name and extension")
    
    #parser.add_argument("-pt", '--pipeline-type',
    #                choices=['training','deploy-model'],
    #                default='training',
    #                help='define pipeline type')

    args = parser.parse_args()
    
    
    pipeline_filename='pipeline.json' 

    compile_pipeline(pipeline_filename)
    upload(args.destination, pipeline_filename)