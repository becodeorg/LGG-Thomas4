from websocket import create_connection
import json
import socket

# Set Coinbase websocket URL
coinbase_url = "wss://ws-feed.exchange.coinbase.com"

# Set localhost socket parameters
localhost = "127.0.0.1"
local_port = 8776

# Create local socket
local_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_socket.bind((localhost, local_port))
local_socket.listen(1)

# Connect to Coinbase websocket
ws = create_connection(coinbase_url)

# Subscribe to desired channels and products
subscribe_message = {
    "type": "subscribe",
    "product_ids": [
        "ETH-USD",
        "ETH-EUR"
    ],
    "channels": [
        "level2",
        "heartbeat",
        {
            "name": "ticker",
            "product_ids": [
                "ETH-BTC",
                "ETH-USD"
            ]
        }
    ]
}
ws.send(json.dumps(subscribe_message))

# Wait for connection from local client
# !!! Will block until connection is made !!!
conn, addr = local_socket.accept()
print("Connected by", addr)

# Forward stream from Coinbase websocket to local socket
while True:
    data = ws.recv()
    conn.send(bytes(data + "\n", "ascii"))

ws.close()
local_socket.close()
