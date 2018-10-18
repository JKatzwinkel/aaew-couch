import pytest

def test_public_collections_retrieval():
    from aaew_couch import connect, all_public_collections
    server = connect('http://aaew64.bbaw.de:9589',
            auth_file='auth.json')
    collections = all_public_collections(server)
    assert collections is not None
    for category in ['wlist', 'ths', 'corpus', 'admin']:
        assert category in collections
        assert len(collections[category]) > 0


def test_public_documents_in_collection():
    from aaew_couch import connect, retrieve_public_documents
    server = connect('http://aaew64.bbaw.de:9589',
            auth_file='auth.json')
    doc_gen = retrieve_public_documents(server['aaew_corpus_bbawtestcorpus'])
    assert doc_gen is not None
    doc = next(doc_gen)
    assert doc is not None


    

     

