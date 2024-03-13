## Pyrostring
<div align="center">
🪡
</div>

`Pyrostring` generates session strings for `Telegram` accounts using `Pyrogram` and all session string generated is usable on `Pyrogram forks`.

#### Note
Before running the script, ensure that you have created all accounts in Telegram X or the official Telegram app.

#### Installation
1. Clone the repository
- `git clone https://github.com/zawsq/Pyrostring.git`
2. Install the required dependencies
- `pip install -r requirements.txt`

#### Configuration
After cloning the repository, you need to edit the `config.py` file to include your API credentials:
- Update `API_ID` and `API_HASH` with your own values.

Put your numbers in `numbers.csv`
Format should be:
- +your_number
- +your_number


Refer to the [configuration guide](https://github.com/zawsq/Pyrostring/blob/main/Pyrostring/config.py).

#### Running the Script
Navigate to the Pyrostring directory and run `main.py`

#### Usage Guide
When prompted, provide the following information:

- `NEED SESSION:` Enter the 4-digit code provided by Telegram.
- `AUTH PASSWORD:` Enter your Telegram authentication password.

Once completed, all your session strings will be saved in the `session_string.csv` file.

---
Please note that this script is intended for educational purposes only. Misuse of this tool may lead to account suspension or banning by Telegram. Use at your own risk.

