# Trading-BOT
# 📈 Binance Futures Trading Bot

A simplified crypto trading bot built in Python using the [Binance Futures Testnet](https://testnet.binancefuture.com). This bot allows users to place **market** and **limit** orders via the command-line interface and is designed with clean structure, logging, and basic error handling.

---

## 🧠 Features

- ✅ Place **Market** and **Limit** orders  
- ✅ Support for **Buy** and **Sell** sides  
- ✅ Connects to **Binance Futures USDT-M Testnet**  
- ✅ CLI input using `argparse`  
- ✅ Structured logging of API requests and errors  
- ✅ Pythonic and modular design  

---

## 📦 Requirements

- Python 3.8+
- `python-binance`

Install dependencies:
```bash
pip install python-binance

⚙️ Setup Instructions
Clone the repository:


git clone https://github.com/tawarevaishu/binance-trading-bot.git
cd binance-trading-bot


api_key = 'fbca9a06314521f3e8e7b0e4713e00b8b141a3064d1451ab50361b124a713b06'
api_secret = 'e1c790be612c86242d2d3f6bae69d11d3ff219bde3cab0d0a80c658d6befddf5'
Run the bot using CLI:

➤ Market Buy Order:


python bot.py --symbol BTCUSDT --side buy --type market --quantity 0.001 --testnet
➤ Limit Sell Order:

python bot.py --symbol BTCUSDT --side sell --type limit --quantity 0.001 --price 65000 --testnet
🔒 Use only Binance Testnet credentials. Never expose real credentials publicly.

📝 Log File
A trading_bot.log file will be generated automatically and contains all order logs and errors:

2025-07-08 18:44:03 - INFO - Order placed: BTCUSDT BUY MARKET
📁 File Structure

binance-trading-bot/
├── bot.py               # Main bot script
├── trading_bot.log      # Log output (generated after running)
├── README.md            # This file
🧪 Example Output

✅ Order Placed Successfully!
{'orderId': 12345678, 'status': 'FILLED', 'price': '0', ...}
📧 Assignment Submission
This project was completed as part of an application for:

Junior Python Developer – Crypto Trading Bot
saami@bajarangs.com, nagasai@bajarangs.com
CC: sonika@primetrade.ai

🙋‍♀️ Author
Vaishnavi Taware
GitHub Profile

