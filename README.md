# StatusBot.py

Python implementation of the [StatusBot JavaScript app](https://github.com/jozsefsallai/StatusBot) - A Discord bot that tells you if there's any problems with your websites. The app will send a new message to a specific channel from a specific Discord server at a given refresh interval.

## How It Works

The bot will automatically fetch all the websites you've provided to it and see if they are accessible. Then it will send a message to the channel you've specified, at a given refresh interval. The bot will separate the sites that are unavailable and the ones that throw an HTTP status code that is greater than or equal to 400, and will show them separately in the Discord message. Unless quiet mode is enabled, the bot will send a message even if all your websites are functional.

---

## Prerequisites
 * Python 3.4.2-3.6.x
 * A Discord server with a channel dedicated to the bot
 * A registered Discord application
 * The ID of the channel where the bot will send notifications
 * The ID of the role to mention when something's wrong

## Getting Started

1. Clone this repository:
```
git clone git@github.com:jozsefsallai/StatusBot.py StatusBot
cd StatusBot
```

2. Install the dependencies:
```
pip install -r requirements.txt
```

3. Create the config file:
```
cp config.example.json config.json
```

## Configuration

All the configuration is done in the `config.json` file. To get the guild and channel IDs, make sure to enable **Developer Mode** in your Discord settings. 

You need to enter each domain you want to check into the `domains` array (separated by comma). The domains **must** include the protocol (http or https). If the protocol is missing or is not http or https, the bot will mark it as unreachable.

The `app.refreshInterval` setting (hours) tells the bot how often it should check the websites. The default value is 1 hour.

The `app.roleToMention` setting is the ID of the role that will get mentioned whenever something is wrong. Make sure to enable the "Allow anyone to @mention this role" option in the role's settings. To get the role ID, just mention the role and put a backslash in front of the name (e.g.: `\@MyRole`) and send the message. The ID is the number part of the returned string.

The `app.quiet` setting (boolean) will tell the bot whether it should only send a message to the channel if there is something wrong with at least one of the websites (`true`) or at every check, even if everything's okay (`false`).

## Starting

After you've finished configuring your bot, you can start it with the following command:

```
python StatusBot.py
```