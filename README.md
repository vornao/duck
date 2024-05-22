# Duck Bot

Duck Bot is a simple Telegram bot written in Python that responds to the `/duck` command by sending a duck quacking sound to the user. This README provides an overview of the code and how to set up and run the bot.

### Prerequisites

Before you can run this code, make sure you have the following:

- Python 3.9 or higher installed.
- The `telegram` library, which you can install using `pip`:

```bash
pip install python-telegram-bot
```

- A Telegram bot token. You can obtain one by talking to the [BotFather on Telegram](https://core.telegram.org/bots#botfather).

### Setup

1. Clone or download this repository to your local machine.

2. Open the code in a text editor or integrated development environment (IDE) of your choice.

3. Replace the placeholder `TOKEN` in the code with your actual Telegram bot token obtained from the BotFather.

4. Ensure you have a valid audio file to send as a response. In this code, the audio file is expected to be located at `assets/duck.mp3`. Make sure you have this audio file in the specified path, or modify the code to point to the correct file path.



### Docker Setup

1. Clone or download this repository to your local machine.

2. Open the code in a text editor or integrated development environment (IDE) of your choice.

3. Replace the placeholder `TOKEN` in the code with your actual Telegram bot token obtained from the BotFather.

4. Ensure you have a valid audio file to send as a response. In this code, the audio file is expected to be located at `assets/duck.mp3`. Make sure you have this audio file in the specified path, or modify the code to point to the correct file path.

5. Build the docker image using the following command:

```bash
docker build -t duck-bot .
```

6. Run the docker container using the following command:

```bash
docker run -d --name duck-bot duck-bot
```

### Usage

To run the Duck Sound Bot, execute the Python script by running the following command in your terminal or command prompt:

```bash
python main.py
```

Once the bot is running, you can interact with it on Telegram by following these steps:

1. Find and start a chat with your bot on Telegram.

2. Send the `/duck` command to the bot.

3. The bot will respond by sending the duck quacking sound in the form of an audio message.

### Troubleshooting

- If the bot does not respond, double-check that you have entered the correct bot token and that the `assets/duck.mp3` file exists in the specified path.

- Ensure that your bot is authorized to send messages and audio files in the chat where you are testing it.


Enjoy your Duck Bot!
