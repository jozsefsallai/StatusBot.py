import asyncio, discord, json, GetStatus

with open('config.json', 'r') as configfile:
  config = json.load(configfile)

client = discord.Client()

async def runtimeCheck():
  await client.wait_until_ready()
  channel = client.get_channel(config['app']['channel'])
  while not client.is_closed:
    message = GetStatus.runChecks(config)
    if message:
      await client.send_message(channel, message)
    await asyncio.sleep(60 * 60 * config['app']['refreshInterval'])

@client.event
async def on_message(message):
  if '<@{0}>'.format(client.user.id) in message.content:
    # Bot invoked by user
    status = GetStatus.runChecks(config)
    if not status:
      status = ':tada: Woohoo! At the moment, all your websites are completely functional.'
    await client.send_message(message.channel, status)

@client.event
async def on_ready():
  print('StatusBot.py has started...')
  if config['app']['activity']:
    await client.change_presence(game = discord.Game(name = config['app']['activity']))

client.loop.create_task(runtimeCheck())
client.run(config['app']['token'])
