import http.server, ssl, socketserver

context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)

context.load_cert_chain("cert.pem")
port=3000
server_address = ("0.0.0.0", port) 

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(server_address, handler) as httpd:
    httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
    print("Server listening on https://localhost:3000")
    httpd.serve_forever()
