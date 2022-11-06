from website import create_app

SERVER_HOST = '0.0.0.0'
SERVER_PORT = 3000

app = create_app()

if __name__ == '__main__':
  app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
