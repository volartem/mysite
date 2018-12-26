from mysite.wsgi import application
import bjoern


if __name__ == "__main__":
    bjoern.run(application, '0.0.0.0', 8000)
