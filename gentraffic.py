import socket

def send_http_request(host, port, request):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))

    # Send the HTTP request
    client_socket.sendall(request.encode())

    # Receive the response
    response = b""
    while True:
        part = client_socket.recv(4096)
        if not part:
            break
        response += part

    # Close the socket
    client_socket.close()

    return response.decode()

# Host and port
host = '3.7.179.253'
port = 80

# HTTP GET request for the "About Us" page
http_request = f"GET /about-us/ HTTP/1.1\r\nHost: {host}\r\nConnection: close\r\n\r\n"

# Send the request and get the response
response = send_http_request(host, port, http_request)

# Dump the response into a file
with open('response_about_us.txt', 'w') as file:
    file.write(http_request)
    file.write("\n\n")
    file.write(response)

print("Response saved to response_about_us.txt")
