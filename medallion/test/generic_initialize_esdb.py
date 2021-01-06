from elasticsearch import Elasticsearch


def connect_to_client(url="http://localhost:9200", user=None, password=None, verify_certs=False):
    """
    Fill:
        Connect to elasticsearch server accessible via the given url

    Args:
        url (str): url of the elasticsearch server
        user (str): user of the elasticsearch server
        password (str): password of the elasticsearch server
    Returns:
        elasticsearch client

    """
    return Elasticsearch([url], http_auth=(user, password), verify_certs=verify_certs)


def refresh_indices(client: Elasticsearch):
    client.indices.delete(index='stix2-discovery', ignore=[400, 404])
    client.indices.create(
        index="stix2-discovery",
        body={
            'mappings': {},
            'settings': {},
        },
        ignore=[400, 404]
    )
    client.indices.delete(index='stix2-api1', ignore=[400, 404])
    client.indices.create(
        index="stix2-api1",
        body={
            'mappings': {},
            'settings': {},
        },
        ignore=[400, 404]
    )
    client.indices.delete(index='stix2-api2', ignore=[400, 404])
    client.indices.create(
        index="stix2-api2",
        body={
            'mappings': {},
            'settings': {},
        },
        ignore=[400, 404]
    )
    client.indices.delete(index='stix2-trustgroup1', ignore=[400, 404])
    client.indices.create(
        index="stix2-trustgroup1",
        body={
            'mappings': {},
            'settings': {},
        },
        ignore=[400, 404]
    )
    client.indices.delete(index='collections', ignore=[400, 404])
    client.indices.create(
        index="stix2-collections",
        body={
            'mappings': {},
            'settings': {},
        },
        ignore=[400, 404]
    )
    client.indices.delete(index='objects', ignore=[400, 404])
    client.indices.create(
        index="stix2-objects",
        body={
            'mappings': {},
            'settings': {},
        },
        ignore=[400, 404]
    )


def store_doc(client: Elasticsearch, index: str, data: object):
    res = client.index(
        index=index,
        body=data,
        refresh='wait_for'
    )
    return res


def update_doc(client: Elasticsearch, index: str, doc_id: str, data: object):
    res = client.update(
        index=index,
        id=doc_id,
        body=data,
        refresh='wait_for'
    )
    return res
