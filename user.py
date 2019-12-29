import facebook
import json
from login import Login
from page import Page
from comment import Comment
from post import Post
import requests
class User(object):
    graph = "" #add to init and do self. for all global var
    pages = []
    comments = []
    def __init__(self):
        userLogin = Login()
        userLogin.userLogin()
        apiKey = userLogin.getToken()
        self.graph = facebook.GraphAPI(apiKey)
        self.initPages()
        self.initComments()
        #print(apiKey)
    
    def getGraph(self):
        return graph

    def initPages(self):
        pagesRaw = self.graph.request('me/accounts')
        myPages = pagesRaw['data']
        tempPages = []
        for currentPage in myPages:
            newPage = Page(currentPage['name'], self.graph)
            tempPages.append(newPage)
        
        global pages
        pages = tempPages

    def getPage(self, index):
        return pages[index]

    def initComments(self):
        posts = self.graph.get_connections(id="me", connection_name="posts")
        #print(posts)
        #posts = graph.request('me/posts')
        posts = posts['data']
        
        for currentPost in posts:
            if "message" not in currentPost:
                continue

            currentMessage = currentPost['message']
            currentId = currentPost['id']
            if not self.doesContainComment(currentId):
                newComment = Post(self, currentId, self.graph, currentMessage)
                newComment.message = currentMessage
                newComment.id = currentId
                newComment.graph = self.graph
                newComment.updateComments()
                #print(newComment.message)
                self.comments.append(newComment)


    def doesContainComment(self, thisId):
        for currentComment in self.comments:
            if currentComment.id == thisId:
                return True

        return False

    def getComment(self):
        return self.comments[len(self.comments) - 1]

    def putPost(self):
        self.graph.put_object(parent_object="me", connection_name="feed", message="hello")

