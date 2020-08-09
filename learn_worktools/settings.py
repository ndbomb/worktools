
def default_setting(app):

    app.config["flask_profiler"] = {
        "enabled": app.config["DEBUG"],
        "storage": {
            "engine": "sqlite"
        },
        "basicAuth":{
            "enabled": True,
            "username": "admin",
            "password": "admin"
        },
        "ignore": [
            "^/static/.*"
        ]
    }