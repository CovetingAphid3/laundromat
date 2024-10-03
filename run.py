from laundromat import create_app
from werkzeug.serving import WSGIRequestHandler

app = create_app()
# Set the server header to an empty string
WSGIRequestHandler.server_version = ''
WSGIRequestHandler.sys_version = ''

if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='0.0.0.0')