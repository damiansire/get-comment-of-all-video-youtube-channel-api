def get_comment_data(comment):
    id_comment = comment["id"]
    video_id = comment["snippet"]["videoId"]
    text = comment["snippet"]["textDisplay"]
    date = comment["snippet"]["publishedAt"]
    like_count = comment["snippet"]["likeCount"]
    author_id = comment["snippet"]["authorChannelId"]["value"]
    return {"commentId" : id_comment, "video_id" : video_id, "text" : text, "datePublished" : date, "likeCount" : like_count, "authorId" : author_id}

def get_video_comment(video_id, youtube_client):
    request = youtube_client.commentThreads().list(
        part="snippet,replies",
        videoId=video_id
    )
    response = request.execute()
    return response


def get_author_data(comment):
    name = comment["snippet"]["authorDisplayName"]
    img_url = comment["snippet"]["authorProfileImageUrl"]
    author_id = comment["snippet"]["authorChannelId"]["value"]
    return { "id" : author_id, "name" : name, "imgUrl" : img_url}

def parse_response(response):    
    all_comment = []
    all_author = []
    for comment in response["items"]:
        top_level_comment = comment["snippet"]["topLevelComment"]
        # Estoy agregando mas de una vez el autor
        all_comment.append(get_comment_data(top_level_comment))
        all_author.append(get_author_data(top_level_comment))
        if("replies" in comment):
            replies = comment["replies"]["comments"]
            for comment in replies:
                all_comment.append(get_comment_data(comment))
                #Si el usuario ya existe, no lo agregues
                author = get_author_data(comment)
                if(not(author in all_author)):
                    all_author.append(author)
    return { "allComment" : all_comment, "allAuthor" : all_author}    
