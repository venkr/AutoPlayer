Useful APIs & some potential ideas
=====
Twilio SMS API: https://www.twilio.com/docs/api/rest/message
* Create custom alerts by combining this with any other API
* Scrape data from websites and send alerts
* Implement games like Werewolf/Mafia in text

Youtube Search API: https://developers.google.com/youtube/v3/docs/search/list
* Combine with other APIs to get links to Youtube videos

Facebook Graph API: https://developers.facebook.com/docs/graph-api
* You can read posts on any group or page you're in
* You can also post to any group or page
  * Automatically post alerts to a Facebook group
  * Automatically upload pictures/videos at a specific time every day
  * Repost content from other groups onto your group
  
Sendgrid Email API: https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/index.html
* Similar to Twilio, but for emails instead, and hence free
* Create mailing lists or email notifications

<!--- 
Twilio SMS API
=====

Full API Documentation: https://www.twilio.com/docs/api/rest/message

Setup
-----

```Python
from twilio.rest import Client

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)
```

Get a list of all messages
-----

```Python
client.messages.list()
```

Message Functions
-----
You can access these on individual elements of the message list

```Python
message.date_sent
message.to
message.from_
message.body
```

--->
