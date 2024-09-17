# Spark data stream

Read data from [Coinbase endpoint](https://docs.cloud.coinbase.com/exchange/docs/websocket-overview).

## Server side
Read data from Coinbase socket. Open a new socket locally and send data to it.

## Client side
Read data from local socket with pyspark and print it.

## Usage
### 0. Install dependencies
```bash
pip install -r requirements.txt
```

### 1. Server side
```bash
python server.py
```

### 2. Client side
```bash
python client.py
```