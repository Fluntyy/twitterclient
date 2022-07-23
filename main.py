from imaplib import _Authenticator
from tkinter import *
from tkinter import messagebox
import tkinter
import tweepy

ui = Tk()
key_list = open('keys').read().splitlines()
client = tweepy.Client(bearer_token=key_list[0], access_token=key_list[1], access_token_secret=key_list[2], consumer_key=key_list[3], consumer_secret=key_list[4])

#             Print Token and Keys              #
#-----------------------------------------------#
# print('Bearer Token: ', key_list[0])
# print('Access Token: ', key_list[1])
# print('Access Token Secret: ', key_list[2])
# print('Consumer/API Key: ', key_list[3])
# print('Consumer/API Key Secret: ', key_list[4])

ui.title("Tweet - Flunty's Twitter Client")
tweet_text = Label(ui, text="Tweet something: ", font=("Montserrat", 24))
tweet_text.grid(column=0, row=0)
tweet_txtbox = Text(ui, width=35, height=7, font=("Montserrat", 24))
tweet_txtbox.grid(column=0, row=1)
def send():
    
    tweet_value = tweet_txtbox.get("1.0","end-1c")
    client.create_tweet(text=tweet_value, user_auth=True)
    messagebox.showinfo("Flunty's Twitter Client", "Message sent! Check your profile.")
    ui.quit()

tweet_button = Button(ui, text="Tweet", width=35, font=("Montserrat", 24), command=send)
tweet_button.grid(column=0, row=3)
ui.mainloop()