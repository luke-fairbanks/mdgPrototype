from distutils.log import debug
from digital_garage import create_app, db
from flask_migrate import Migrate

app = create_app()
migrate = Migrate(app,db)

if __name__ == "__main__":
    app.run()