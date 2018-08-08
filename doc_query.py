import pydocumentdb.document_client as document_client
import pickle

connection = pickle.load(open('/home/alexw/Documents/db_credential.p', 'rb'))

client = document_client.DocumentClient(
    connection['ENDPOINT'],
    {'masterKey': connection['MASTERKEY']}
)

query = {'query': 'SELECT * FROM server'}

options = {}
options['enableCrossPartitionQuery'] = True
options['maxItemCount'] = 2

result_iterable = client.QueryDocuments('dbs/gLJHAA==/colls/gLJHANqCqvY=/', query, options)
results = list(result_iterable)

print(results[0:2])