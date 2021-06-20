# tg_answering_machine
Telegram answering machine made via Python.

## Setup
Python 3.9.0+ is recommended.

#### First step
Install all required libriaries.
```
pip install -r requirements.txt
```

#### Second step
Get your own Telegram api data. Go to https://my.telegram.org/apps and create an app.
You need api_id and api_hash.
![api_id and api_hash](https://user-images.githubusercontent.com/45712837/122667790-54671d00-d1bd-11eb-850b-99f435b71434.png)

#### Third step
Setup config.json file
```
{
    "message": "<Your message for reply>",
    "keys": ["The key by which the message to be answered is determined", "key2", "key3", "key_n"],
    "login": {
        "api_id": "<your_api_id>",
        "api_hash": "<your_api_hash>"
    }
}
```

## Runnig
```
python main.py
```
