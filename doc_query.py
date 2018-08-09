import pydocumentdb.document_client as document_client
import pickle

connection = pickle.load(open('db_credential.p', 'rb'))

client = document_client.DocumentClient(
    connection['ENDPOINT'],
    {'masterKey': connection['MASTERKEY']}
)

query = {'query': '''
    SELECT * 
    FROM server s 
    WHERE s.id = '2018-08-09T12:30Z'
    '''
}

result_iterable = client.QueryDocuments('dbs/gLJHAA==/colls/gLJHANqCqvY=/', query)
results = list(result_iterable)

print(results)