import facebook
import requests
from Permissions import Perm
from user import User
from page import Page
from comment import  Comment
#import os
import json
graph = ""
user1 = ""
accessToken = ""
driver = ""
log = []
def main():
  log.append("Program started")
  currentUser = User()
  log.append("User Logged in")
  #currentUser.putPost()
  currentPage = currentUser.getPage(0)
  log.append("Page Name: " + currentPage.name + " Page ID: " + currentPage.id + " Loaded")
  #userInput = input("What would you like to comment?")
  #currentPage.postOnPage(userInput)
  currentComment = currentPage.getPost(0)
  log.append("Post Message: " + currentComment.message + " Post ID: " + currentComment.id + " Loaded")
  #print(currentComment.message)
  while True:
    log.append("Listening for new response for comment ID: " + currentComment.id + " comment Message: " + currentComment.message)
    toComment = currentComment.listener()
    log.append("Listener response ID: " + toComment.id + " Listener response message: " + toComment.message)
    print("Message Found: " + toComment.message)
    reply = input("what would you like to respond with?")

    #currentComment.putComment(reply)
    currentPage.postReply(reply, toComment.id)
    log.append("Listener response: " + reply)
    if (reply == "goodbye"):
      break
  log.append("User Logging Out")


def writeToLog():
    logTxt = open("log.txt", "w+")
    for current in log:
      logTxt.write(current + "\n")

    logTxt.close() 





  
if __name__ == "__main__":
  main()
  writeToLog()

