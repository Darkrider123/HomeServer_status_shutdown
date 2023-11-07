from http.server import HTTPServer, BaseHTTPRequestHandler
from message import Message
import os
from sensible_config import HOST, PORT


class HomeServerHTTP(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(str(Message("Server is running!")), "utf-8"))

    def do_POST(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(str(Message("Server is shutting down!")), "utf-8"))
        os.system("shutdown now")

    def do_PUT(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(str(Message("Server is restarting!")), "utf-8"))
        os.system("shutdown -r now")
        


def main():
    server = HTTPServer((HOST, PORT), HomeServerHTTP)
    print("Server running...")
    server.serve_forever()


if __name__ == "__main__":
    main()
