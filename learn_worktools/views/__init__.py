from .home import home, task

BLUEPRINT = (
    (home, '/'),
    (task, '/task')
)


def register_bp(app):
    for bp, url_perfix in BLUEPRINT:
        app.register_blueprint(bp, url_perfix=url_perfix)