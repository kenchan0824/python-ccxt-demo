import os
import ccxt
from dotenv import load_dotenv

def init_exchange():
    # Load environment variables
    load_dotenv()
    
    # Initialize exchange (using Binance as an example)
    exchange = ccxt.binance()
    # {
    #     'apiKey': os.getenv('EXCHANGE_API_KEY'),
    #     'secret': os.getenv('EXCHANGE_SECRET'),
    #     'enableRateLimit': True
    # }
    
    return exchange

def main():
    try:
        exchange = init_exchange()
        
        # Examples of public methods you can use:
        markets = exchange.load_markets()
        print(f"Available markets: {len(markets)}")
        
        # Get ticker for a specific symbol
        ticker = exchange.fetch_ticker('BTC/USDT')
        print(f"BTC/USDT price: {ticker['last']}")
        
        # Get order book
        order_book = exchange.fetch_order_book('BTC/USDT')
        print(f"Top bid: {order_book['bids'][0][0]}")
        print(f"Top ask: {order_book['asks'][0][0]}")
        
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 