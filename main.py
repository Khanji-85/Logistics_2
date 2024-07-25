from app import create_app
from routes import bp
from auth import auth

app = create_app()
# Blueprint registration:
app.register_blueprint(bp)
app.register_blueprint(auth, url_prefix='/auth')

if __name__ == '__main__':
    app.run(debug=False)