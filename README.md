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

bash
Copy
Edit
git clone https://github.com/tawarevaishu/binance-trading-bot.git
cd binance-trading-bot
Replace your Binance Testnet API credentials in bot.py:

python
Copy
Edit
api_key = 'YOUR_TESTNET_API_KEY'
api_secret = 'YOUR_TESTNET_API_SECRET'
Run the bot using CLI:

➤ Market Buy Order:
bash
Copy
Edit
python bot.py --symbol BTCUSDT --side buy --type market --quantity 0.001 --testnet
➤ Limit Sell Order:
bash
Copy
Edit
python bot.py --symbol BTCUSDT --side sell --type limit --quantity 0.001 --price 65000 --testnet
🔒 Use only Binance Testnet credentials. Never expose real credentials publicly.

📝 Log File
A trading_bot.log file will be generated automatically and contains all order logs and errors:

pgsql
Copy
Edit
2025-07-08 18:44:03 - INFO - Order placed: BTCUSDT BUY MARKET
📁 File Structure
pgsql
Copy
Edit
binance-trading-bot/
├── bot.py               # Main bot script
├── trading_bot.log      # Log output (generated after running)
├── README.md            # This file
🧪 Example Output
bash
Copy
Edit
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

