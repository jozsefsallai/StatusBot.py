import discord, requests

badStatus = []
down = []

def checkSite(site):
  try:
    req = requests.get(site)
    if req.status_code >= 400:
      badStatus.append(site)
  except:
    down.append(site)

def runChecks(config):
  for site in config['domains']:
    checkSite(site)

  if not badStatus and not down:
    if config['app']['quiet']:
      return None
    else:
      return ':tada: Woohoo! At the moment, all your websites are completely functional.'
  else:
    message = ':warning: **<@&{0}>, some of your websites are not functional!**\n'.format(config['app']['roleToMention'])
    if down:
      message += '\nThe following websites are inaccessible:\n'
      for site in down:
        message += ' - {0}\n'.format(site)
    
    if badStatus:
      message += '\nThe following websites return a bad status code (>= 400):\n'
      for site in badStatus:
        message += ' - {0}\n  '.format(site)
    
    return message
