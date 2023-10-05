from http.server import HTTPServer, BaseHTTPRequestHandler
from message import Message
import os


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
        os.system("shutdown")


def main():
    
    HOST = "192.168.100.183"
    PORT = 6666
    
    server = HTTPServer((HOST, PORT), HomeServerHTTP)
    print("Server running...")
    server.serve_forever()


if __name__ == "__main__":
    main()
