from pymongo import ASCENDING, IndexModel

from medallion.common import datetime_to_float, string_to_datetime
from medallion.test.generic_initialize_esdb import (
    store_doc, update_doc, refresh_indices, connect_to_client
)


def reset_db(url="https://192.168.20.200:9200", user='elastic', password='LAB_P@ssw0rd', verify_certs=False):
    client = connect_to_client(url=url, user=user, password=password, verify_certs=verify_certs)
    refresh_indices(client)
    store_doc(
        client=client,
        index='stix2-discovery',
        data={
            "api_roots": [
                "http://localhost:5000/api1/",
                "http://localhost:5000/api2/",
                "http://localhost:5000/trustgroup1/"
            ],
            "contact": "string containing contact information",
            "default": "http://localhost:5000/trustgroup1/",
            "description": "This TAXII Server contains a listing of",
            "title": "Some TAXII Server"
        }
    )
    store_doc(
        client=client,
        index='stix2-api1',
        data={
            "url": "http://localhost:5000/api1/",
            "description": "A repo for general STIX data.",
            "max_content_length": 9765625,
            "title": "General STIX 2.1 Collections",
            "versions": [
                "application/taxii+json;version=2.1"
            ]
        }
    )
    store_doc(
        client=client,
        index='stix2-api2',
        data={
            "url": "http://localhost:5000/api2/",
            "description": "A repo for general STIX data.",
            "max_content_length": 9765625,
            "title": "STIX 2.1 Indicator Collections",
            "versions": [
                "application/taxii+json;version=2.1"
            ]
        }
    )
if __name__ == "__main__":
    reset_db()
