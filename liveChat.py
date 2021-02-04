import os
import youtubeClient
import videoComments

last_read_date = '2021-01-25T00:10:57.999000Z'
live_chat_id = "Cg0KCzRaSGhua0I4SjAwKicKGFVDYzBuUS1QZkpCWVQ3S043MnEzMHIwQRILNFpIaG5rQjhKMDA"

def insert_comment(comment):
    return 0

def get_actual_live_chat_id(youtube_client):
    active_live_broadcasts = youtube_client.liveBroadcasts().list(part="snippet",broadcastStatus="active").execute()
    #active_live_broadcasts["items"][0]["snippet"]["liveChatId"]
    return 0

def convert_to_comment_obj(comment):
    return { "message" : comment["textMessageDetails"]["messageText"], "date" : comment["publishedAt"] }

def convert_message_list_to_list(comments_list):
    all_comment = []
    for comment in comments_list:
        try:
            comment = convert_to_comment_obj(comment["snippet"])
            all_comment.append(comment)
        except Exception:
            print("exploto")
    return all_comment

def get_all_message_of_chat(youtube_client):
    #Id del chat del directo actual
    live_chat_id = "Cg0KCzRaSGhua0I4SjAwKicKGFVDYzBuUS1QZkpCWVQ3S043MnEzMHIwQRILNFpIaG5rQjhKMDA"
    live_chat_messages = youtube_client.liveChatMessages()
    #Obtiene la lista de mensajes actuales
    message_list = live_chat_messages.list(liveChatId=live_chat_id, part="snippet").execute()
    all_comments = convert_message_list_to_list(message_list["items"])
    return all_comments

def filter_message_not_read(all_message):
    message_not_read = []
    for message in all_message:
        if(message['date'] > last_read_date):
            message_not_read.append(message)
    return message_not_read

def get_not_read_message(youtube_client):
    all_message = get_all_message_of_chat(youtube_client)
    not_read_message = filter_message_not_read(all_message)
    return not_read_message

def analyze_all_message(all_message):
    for message in all_message:
        if_command_so_execute(message)

##Despues emprolijamo esto, primero que ande
#Pal diccionario
def if_command_so_execute(message):
    global last_read_date
    last_read_date = message["date"]
    message = message["message"]
    print(message)
    if('!twitch' in message):
        print("imprimir twitch")
    if('!facebook' in message):
        print("Toma mi facebook")
    if('!twitter' in message):
        print("Toma mi twitter")
    if('!instagram' in message):
        print("Toma mi instagram")
    if('!discord' in message):
        print("Toma el discord")

def evaluate_new_message(youtube_client):
    pending_read_message = get_not_read_message(youtube_client)
    analyze_all_message(pending_read_message)

def write_message(message,youtube_client):
    live_chat_id = "Cg0KCzRaSGhua0I4SjAwKicKGFVDYzBuUS1QZkpCWVQ3S043MnEzMHIwQRILNFpIaG5rQjhKMDA"
    print("prueba")

def send_message(youtube_client):
    live_chat_id = "Cg0KCzRaSGhua0I4SjAwKicKGFVDYzBuUS1QZkpCWVQ3S043MnEzMHIwQRILNFpIaG5rQjhKMDA"
    request = youtube_client.liveChatMessages().insert(
        part="snippet",
        body={
            "snippet": {
            "liveChatId": live_chat_id,
            "type": "textMessageEvent",
            "textMessageDetails": {
                "messageText": "prueba"
            }
            }
        }
    )
    response = request.execute()