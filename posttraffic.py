import socket
import ssl

def send_post_request(ip, port, request):

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


    if port == 443:
        context = ssl.create_default_context()
        client_socket = context.wrap_socket(client_socket, server_hostname=ip)

    try:

        client_socket.connect((ip, port))
        print("Connected to server")

  
        client_socket.sendall(request.encode())
        print("Request sent")


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
    
        client_socket.close()
        print("Connection closed")

    return response.decode()

ip = '76.76.21.22'
port = 443


http_request = (
    "POST /api/send HTTP/1.1\r\n"
    f"Host: {ip}\r\n"
    "Content-Type: application/json\r\n"
    "Content-Length: 89\r\n"  # Length of the payload in bytes
    "Connection: close\r\n"
    "\r\n"
    '{"email": "sayandeep11@gmail.com", "subject": "efwfe", "message": "ewfqwefw ef wef ew few fwe fef"}'
)

response = send_post_request(ip, port, http_request)

with open('response_send_api.txt', 'w') as file:
    file.write(response)

print("Response saved to response_send_api.txt")
