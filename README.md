# Telegram Crypto Bot

Telegram Crypto Bot is a Telegram bot designed to track cryptocurrency prices and provide real-time updates directly in your Telegram chat.

## Features

- **Real-time Price Tracking**: Get the latest prices for various cryptocurrencies.
- **Price Alerts**: Set alerts for specific price points and receive notifications.
- **Market Data**: Access detailed market data and trends.

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [Telegram Bot API Token](https://core.telegram.org/bots#botfather)
- [Cryptocurrency API Key](e.g., [CoinGecko](https://www.coingecko.com/en/api))

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sargis-tovmasyan/Telegram_crypto_bot.git
    cd Telegram_crypto_bot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

3. Configure your environment variables:
    - `TELEGRAM_API_TOKEN`: Your Telegram bot API token.
    - `CRYPTO_API_KEY`: Your cryptocurrency API key.

### Usage

1. Start the bot:
    ```sh
    python bot.py
    ```

2. Add the bot to your Telegram chat and start receiving cryptocurrency updates.

### Configuration

The bot can be configured using environment variables or a configuration file. Ensure you set up the appropriate configurations for your API tokens.

#### Example `.env` file:
```env
TELEGRAM_API_TOKEN=your_telegram_api_token
CRYPTO_API_KEY=your_crypto_api_key
