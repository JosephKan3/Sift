# -*- coding: utf-8 -*-

# Sample Python code for youtube.channels.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/guides/code_samples#python

import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

api_service_name = "youtube"
api_version = "v3"
client_secrets_file = "client_secret.json"
DEVELOPER_KEY = "AIzaSyC6SnrDyBVwM6EBLuP55jwEIcvRZeUcfes"

# Get credentials and create an API client
flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
    client_secrets_file, scopes)
credentials = flow.run_console()
youtube = googleapiclient.discovery.build(
    api_service_name, api_version, credentials=credentials)

def getUploadID():
    print("Input channel name:")
    channelNameInput = input()
    uploadID = getCommentsByAuthorName(channelNameInput)["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]
    videoIDs = getVideoIDs(uploadID)
    commentSet = []
    for videoId in videoIDs:
        comments = getComments(videoId)
        commentSet.append(comments)
    print(commentSet)

def getCommentsFromVideoID():
    print("Input video ID:")
    videoIdInput = input()
    comments = getComments(videoIdInput)
    print(comments)


def getComments(videoId):
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey = DEVELOPER_KEY)

    request = youtube.commentThreads().list(
        part="snippet",
        videoId=videoId
    )
    comments = []
    response = request.execute()
    for comment in response["items"]:
        try:
            comments.append(comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"])
        except Exception:
            print("Invalid comment ignored")
    return comments


    return response
def getCommentsByAuthorName(channelName):
    # print(str(channelName))
    request = youtube.channels().list(
        part="contentDetails",
        maxResults=4,
        forUsername=str(channelName)
    )

    response = request.execute()

    return response

def getVideoIDs(uploadID):
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=3,
        playlistId=uploadID
    )
    response = request.execute()
    videoIDs = []
    for video in response["items"]:
        try:
            videoIDs.append(video["snippet"]["resourceId"]["videoId"])
        except KeyError:
            print("Error, skipped invalid video")
    return videoIDs


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "client_secret.json"

    while True:
        print("Enter 1, if enterring video ID, Enter 2, if enterring Youtube Channel, or Enter anything else to quit.")
        functionInput = input()
        if functionInput == str(1):
            getCommentsFromVideoID()
        elif functionInput == str(2):
            getUploadID()
        else:
            break



if __name__ == "__main__":
    main()