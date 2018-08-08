import pydocumentdb.document_client as document_client
import requests
import pickle

connection = pickle.load(open('/home/alexw/Documents/db_credential.p', 'rb'))

client = document_client.DocumentClient(
    connection['ENDPOINT'],
    {'masterKey': connection['MASTERKEY']}
)

grid_response = requests.get(
    'https://api.carbonintensity.org.uk/generation/2018-01-01T12:35Z/2018-03-01T12:35Z'
)
grid_data = grid_response.json()


new_document = client.CreateDocument(
    'dbs/gLJHAA==/colls/gLJHANqCqvY=/',
    {
        'id': '2018-01-01T12:35Z',
        'data': grid_data
    }

)