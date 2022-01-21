from re import M
from flask import Flask, render_template
import os
import sys

import azure.cosmos.cosmos_client as cosmos_client
import azure.cosmos.exceptions as exceptions
from azure.cosmos.partition_key import PartitionKey


HOST = os.environ['ACCOUNT_URI']
MASTER_KEY = os.environ['ACCOUNT_KEY']
DATABASE_ID = os.environ['COSMOS_DATABASE']
CONTAINER_ID = os.environ['COSMOS_CONTAINER']

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
