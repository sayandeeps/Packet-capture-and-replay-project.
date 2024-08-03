import socket

def send_http_request(host, port, request):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(request.encode())
    response = b""
    while True:
        part = client_socket.recv(4096)
        if not part:
            break
        response += part
    client_socket.close()

    return response.decode()

host = '3.7.179.253'
port = 80

http_request = f"GET /about-us/ HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

response = send_http_request(host, port, http_request)

with open('response_about_us.txt', 'w') as file:
    file.write(http_request)
    file.write("\n\n")
    file.write(response)

print("Response saved to response_about_us.txt")
