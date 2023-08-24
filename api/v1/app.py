from flask import Flask
from models import storage
from api.v1.views import app_views

app = Flask(__name__)

# Register the app_views blueprint
app.register_blueprint(app_views)

# Method to be called when the app context tears down
def close_storage(exception=None):
    storage.close()

# Register the teardown function
app.teardown_appcontext(close_storage)

# Additional configuration and routes can be defined here

if __name__ == '__main__':
    app.run(debug=True)