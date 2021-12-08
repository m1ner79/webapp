def test_correct_format(accept_json, client):
    """
    test to ensure that we have list of lists and the embedded list
    desired number of items
    """
    resp = client.get("/getdata")
    assert resp.status_code == 200
    assert resp.mimetype == "application/json"
    json = resp.json
    assert isinstance(json, list)  # is this an outer list?
    assert isinstance(json[0], list)  # is this list a list inside the outer list?
    assert len(json[0]) == 4  # does the embedded list contain 4 items?
