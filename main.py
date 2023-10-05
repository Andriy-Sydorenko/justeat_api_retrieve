from restaurants_retrieval.justeat import Client

client = Client()
result = client.by_postal_code("NG1 1AA", filename="test_file", write_to_file=True)

for i in result:
    print(i)
