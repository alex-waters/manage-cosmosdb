import pydocumentdb.document_client as document_client
import requests
import pickle

connection = pickle.load(open('db_credential.p', 'rb'))

client = document_client.DocumentClient(
    connection['ENDPOINT'],
    {'masterKey': connection['MASTERKEY']}
)

grid_response = requests.get(
    'https://api.carbonintensity.org.uk/generation/'
)
grid_data = grid_response.json()


new_document = client.CreateDocument(
    'dbs/gLJHAA==/colls/gLJHANqCqvY=/',
    {
        'id': grid_data['data']['from'],
        'data': grid_data
    }

)