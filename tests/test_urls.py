from flask import request


def test_up(client):
    """Test to see if the server is up."""
    assert client.get("/").status_code == 200


def test_missing(client):
    """Test to see an appropriate response for a missing URL"""
    assert client.get("/missing").status_code == 404


#######################################################################


def test_correct_mainPage(client):
    """Grab the home page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_cvPage(client):
    """Grab the cv page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/cv")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_interestPage(client):
    """Grab the interest page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/interest")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_technologiesPage(client):
    """Grab the technologies page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/technologies")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_machinelearningPage(client):
    """Grab the technologies/machinelearning page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/technologies/machinelearning")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_cloudcomputingPage(client):
    """Grab the technologies/cloudcomputing page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/technologies/cloudcomputing")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_printingPage(client):
    """Grab the technologies/3dprinting page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/technologies/3dprinting")
    assert response.status_code == 200
    # response.data is a binary text version of the HTML page
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_visitorsPage(client):
    """Grab the visitors page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """

    response = client.get("/visitors")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)


def test_correct_messagePage(client):
    """Grab the visitors page, check for 200 code(all ok), then check to
        see if the response is a HTML page.
    """
    response = client.get("/message")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)

def test_correct_form(client):
    """Grab the home page, check for 200 code(all ok), then check to
        see if we have received the correct form and that response is 
        a HTML page.
    """
    response = client.get("/form")
    assert response.status_code == 200
    #assert '<form action="/processform" method="post">' in response.get_data(True)
    assert "<!DOCTYPE html>" in response.get_data(True)


#######################################################################


def test_form_operation(client, clean_up_db):
    """Create some test/sample data, then POST the data to the server.
        Ensure the request is using POST, then look for a 200(all ok) status code.
        Get the response,check for valid HTML page, then check that the submitted
        form data was received then send back to the browser in the response.
    """
    form_data = {
        "fname": "tester",
        "email": "test@gmail.com",
        "message": "This is a test message.",
    }
    response = client.post("/processform", data=form_data)
    assert request.method == "POST"
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.get_data(True)
    # assert "<form_data['login'], encoding='utf-8'>"in response.get_data(True)
    # assert bytes(form_data["visitors"], encoding="utf-8") in response.get_data(True)
