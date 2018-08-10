import pydocumentdb.document_client as document_client
import pickle

connection = pickle.load(open('db_credential.p', 'rb'))

client = document_client.DocumentClient(
    connection['ENDPOINT'],
    {'masterKey': connection['MASTERKEY']}
)

# this query will return dates where coal was above 1%
query = {'query': '''
    SELECT t.id
    FROM things t
    WHERE 
        --t.id = '2018-08-09T12:30Z'
        t.data.data.generationmix[1].perc > 1
    '''
}

result_iterable = client.QueryDocuments('dbs/gLJHAA==/colls/gLJHANqCqvY=/', query)
results = list(result_iterable)

print(results)