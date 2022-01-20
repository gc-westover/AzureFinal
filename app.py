from flask import Flask, render_template
import os

import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey


# settings = {
#     'host': os.environ.get('ACCOUNT_URI'),
#     'master_key': os.environ.get('ACCOUNT_KEY'),
#     'database_id': os.environ.get('COSMOS_DATABASE'),
#     'container_id': os.environ.get('COSMOS_CONTAINER'),
# }
settings = {
    'host': 'https://gw-cc-az-cosmos.documents.azure.com:443/',
    'master_key': '8fTvQj8ENlK016AwkIlDdRYpsYgV6736wrvAgW3G6ZkUeXyVM4s7mWxR5NCT689G3V0BHuh3C6Cfep8RIt3PjA==',
    'database_id': 'ButtonTimes',
    'container_id': 'Times'
}

HOST = settings['host']
MASTER_KEY = settings['master_key']
DATABASE_ID = settings['database_id']
CONTAINER_ID = settings['container_id']

client = cosmos_client.CosmosClient(HOST, {'masterKey': MASTER_KEY} )

app = Flask(__name__)

@app.route('/')
def home():
    
    try:
        db = client.get_database_client(DATABASE_ID)
        container = db.get_container_client(CONTAINER_ID)
        data = container.query_items(query='SELECT * FROM container ORDER BY container.second DESC', enable_cross_partition_query=True,)
    except exceptions.CosmosHttpResponseError as e:
        print('\nrun_sample has caught an error. {0}'.format(e.message))
    finally:
        print("\nrun_sample done")

    return render_template('testweb.html', data=data)

if __name__ == '__main__':
    app.run()
