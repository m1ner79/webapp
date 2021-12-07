import platform

where = platform.uname().release.find("aws")

if where == -1:
    # Local
    config = {
        "host": "127.0.0.1",
        "database": "visitorsDB",
        "user": "visitor",
        "password": "visitorpass",
    }
else:
    # Not on PA
    config = {
        "host": "C00265618.mysql.pythonanywhere-services.com",
        "database": "C00265618$default",
        "user": "C00265618",
        "password": "NewPasswd",
    }