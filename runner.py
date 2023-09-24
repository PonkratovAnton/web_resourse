from http.server import HTTPServer
from server import RequestHandler


if __name__ == '__main__':
    port = 8080
    server_address = ('', port)
    httpd = HTTPServer(server_address, RequestHandler)
    print(f"Сервер запущен на порту {port}")
    httpd.serve_forever()
