from dotenv import load_dotenv
from os import environ
from atproto import Client

load_dotenv()

client = Client()

client.login(environ['HANDLE'], environ['PASSWORD'])

client.send_post('If you can see this, I tweeted this using the Python API!  Hmm, I wonder what power this gives me...  Maybe I\'ll make a bot next...')
