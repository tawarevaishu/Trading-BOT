import argparse
import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

# ------------------ Setup Logging ------------------
logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s: %(message)s'
)

# ------------------ Trading Bot Class ------------------
import time

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            self.client.API_URL = 'https://testnet.binancefuture.com'

        # ✅ Manual timestamp offset calculation
        try:
            server_time = self.client.futures_time()['serverTime']
            local_time = int(time.time() * 1000)  # current local timestamp in ms
            self.client.timestamp_offset = server_time - local_time
        except Exception as e:
            print("⚠️ Failed to sync timestamp:", e)

        # ✅ Test connection
        try:
            self.client.futures_account()
            logging.info("Connected to Binance Futures Testnet.")
        except BinanceAPIException as e:
            logging.error(f"Connection failed: {e}")
            raise


    def place_order(self, symbol, side, order_type, quantity, price=None):
        try:
            params = {
                'symbol': symbol.upper(),
                'side': SIDE_BUY if side.lower() == 'buy' else SIDE_SELL,
                'type': ORDER_TYPE_MARKET if order_type == 'market' else ORDER_TYPE_LIMIT,
                'quantity': quantity
            }

            if order_type == 'limit':
                if price is None:
                    raise ValueError("Price required for limit orders.")
                params['price'] = price
                params['timeInForce'] = TIME_IN_FORCE_GTC

            response = self.client.futures_create_order(**params)
            logging.info(f"Order placed successfully: {response}")
            return response

        except BinanceAPIException as e:
            logging.error(f"Order failed: {e}")
            print("Order Error:", e.message)
            return None

# ------------------ Argument Parser ------------------
def parse_arguments():
    parser = argparse.ArgumentParser(description="Simplified Binance Futures Trading Bot")
    parser.add_argument('--symbol', type=str, required=True, help='Trading pair (e.g. BTCUSDT)')
    parser.add_argument('--side', type=str, choices=['buy', 'sell'], required=True, help='Order side')
    parser.add_argument('--type', type=str, choices=['market', 'limit'], required=True, help='Order type')
    parser.add_argument('--quantity', type=float, required=True, help='Order quantity')
    parser.add_argument('--price', type=float, help='Order price (required for limit orders)')
    parser.add_argument('--testnet', action='store_true', help='Use Binance Futures Testnet')
    return parser.parse_args()

# ------------------ Main Execution ------------------
def main():
    # 🔑 Replace with your actual API keys from Binance Testnet
    api_key = 'fbca9a06314521f3e8e7b0e4713e00b8b141a3064d1451ab50361b124a713b06'
    api_secret = 'e1c790be612c86242d2d3f6bae69d11d3ff219bde3cab0d0a80c658d6befddf5'

    args = parse_arguments()
    bot = BasicBot(api_key, api_secret, testnet=args.testnet)

    result = bot.place_order(
        symbol=args.symbol,
        side=args.side,
        order_type=args.type,
        quantity=args.quantity,
        price=args.price
    )

    if result:
        print("✅ Order Placed Successfully!")
        print(result)
    else:
        print("❌ Order Failed. Check logs for more details.")

if __name__ == '__main__':
    main()
