#Youtube Downloader
import youtube_dl
import time

#Sound playback
import simpleaudio as sa

#Youtube Search API
from apiclient.discovery import build
from apiclient.errors import HttpError

#Twilio SMS API and Datetime lib for handling times
from twilio.rest import Client
from datetime import datetime
import pytz

import random

admins = []

#Twilio account setup
#Get your account_sid and auth_token from Twilio console at twilio.com/console
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

#Stores the time of latest parsed message, initialized to current time 
newestTime = pytz.utc.localize(datetime.utcnow())

# Begin setup for the downloading and playing

# Get the developer key from the google console: console.cloud.google.com
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

#Set options for downloaded videos
ydl_opts = {
  'format': 'bestaudio',
  'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'wav',
    'preferredquality': '64',
  }],
  'nocheckcertificate': True,
  'outtmpl': '%(id)s.%(ext)s'
}

ydl = youtube_dl.YoutubeDL(ydl_opts)

playlist = []
played = []
currentSong = None

#Searches a given query and adds a wave object to the playlist
def search_and_queue(query):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

  #Search using given query
  search_response = youtube.search().list(
    q=query + "lyrics",
    part="id,snippet",
    maxResults=10
  ).execute()

  videos = []

  #Store all the videos that could match
  for search_result in search_response.get("items", []):
    if search_result["id"]["kind"] == "youtube#video":
      videos.append((search_result["id"]["videoId"]))

  #Store the first matching video's url
  url = videos[0]
  ydl.download(['http://www.youtube.com/watch?v=' + url])
  
  #Store the filename to the playlist
  playlist.append(url + ".wav")


#Begin main loop
#Continuously loop over checking new SMSs and changing songs
while True:
  maxTime = pytz.utc.localize(datetime.min)
  #Iterate over all the messages we have
  for message in client.messages.list():
    #Get the time of the message
    currTime = message.date_sent  
    
    #Store the time of the newest message of this set of messages
    maxTime = max(maxTime, currTime)

    #datetime.strptime(message.date_sent, '%a, %d %b %Y %H:%M:%S %z')
    #If this is as old, or older than our newest message, we've gone too far
    if currTime <= newestTime:
      break
    #If this message is new enough, add it to the playlist
    else:
      print("Message: " + message.body + " is being read")
      if (message.body == "skip" and message.from_ in admins):
        currentSong.stop()
        print("This song has been skipped, moving onto the next song")
        played.pop()  
      else: 
        search_and_queue(message.body)
        print(message.body + " has been added to the playlist!")

  #Update newest message time
  newestTime = maxTime

  #Check if the song is still playing, and if not, lets queue the next song
  
  if currentSong is None or not currentSong.is_playing():
    #If the playlist is empty, check the played list
    if len(playlist) == 0:
      #Choose a random song played earlier
      if len(played) != 0:
        nextSong = random.choice(played)
      #We have no songs played earlier :(
      else:
        nextSong = None
    else:
      #Remove the first song from the playlist, and add it to played
      nextSong = playlist.pop(0)
      played.append(nextSong)

    if not nextSong is None:   
      wave_obj = sa.WaveObject.from_wave_file(nextSong)
      currentSong = wave_obj.play()
  time.sleep(5)
  print(".")
  
