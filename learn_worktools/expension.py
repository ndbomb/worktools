from flask_profiler import Profiler

profiler = Profiler()

def register_expension(app):
    profiler.init_app(app)
