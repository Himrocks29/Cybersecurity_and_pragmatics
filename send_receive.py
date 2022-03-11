#!/usr/bin/python3
import requests
import socket, ssl, sys, pprint
hostname = sys.argv[1]
port = 443
#cadir = '/etc/ssl/certs'
cadir = './certs'
# Set up the TLS context
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations(capath=cadir)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = True
# Create TCP connection
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((hostname, port))
input("After making TCP connection. Press any key to continue ...")
# Add the TLS
ssock = context.wrap_socket(sock, server_hostname=hostname,
do_handshake_on_connect=False)
ssock.do_handshake() # Start the handshake
#Send HTTP Request to Server
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
hostname = 'https://'+hostname+'/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png'
print(hostname)
#request = b"GET / HTTPS/1.0\r\nHost: " + \
#hostname.encode('utf-8') + b"\r\n\r\n"

request = requests.get(hostname,headers=headers)
response = request.text
print("response Code: ",request)
#print("request_text: ",response)
#ssock.sendall(request)
# Read HTTP Response from Server
#response = ssock.recv(2048)
#while response:
#	pprint.pprint(response.split(b"\r\n"))
#	response = ssock.recv(2048)