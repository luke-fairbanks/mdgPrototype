from distutils.log import debug
from digital_garage import create_app

app = create_app()

if __name__ == "__main__":
    app.run()