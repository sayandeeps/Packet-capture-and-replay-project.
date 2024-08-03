import socket
import ssl

def send_post_request(ip, port, request):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Wrap the socket with SSL to handle HTTPS
    if port == 443:
        context = ssl.create_default_context()
        client_socket = context.wrap_socket(client_socket, server_hostname=ip)

    try:
        # Connect to the server
        client_socket.connect((ip, port))
        print("Connected to server")

        # Send the HTTP POST request
        client_socket.sendall(request.encode())
        print("Request sent")

        # Receive the response
        response = b""
        while True:
            part = client_socket.recv(4096)
            if not part:
                break
            response += part
        print("Response received")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket
        client_socket.close()
        print("Connection closed")

    return response.decode()

# Define the IP, port, and POST request
ip = '76.76.21.22'
port = 443

# Construct the HTTP POST request
http_request = (
    "POST /api/send HTTP/1.1\r\n"
    f"Host: {ip}\r\n"
    "Content-Type: application/json\r\n"
    "Content-Length: 89\r\n"  # Length of the payload in bytes
    "Connection: close\r\n"
    "\r\n"
    '{"email": "sayandeep11@gmail.com", "subject": "efwfe", "message": "ewfqwefw ef wef ew few fwe fef"}'
)

# Send the request and get the response
response = send_post_request(ip, port, http_request)

# Dump the response into a file
with open('response_send_api.txt', 'w') as file:
    file.write(response)

print("Response saved to response_send_api.txt")
