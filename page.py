import facebook
import requests
from comment import Comment
from post import Post
class Page(object):
    commentArray = []
    token = ""
    name = ""
    id = ""
    graph = ""
    def __init__(self, name1, graph1):
        self.graph = graph1

        self.name = name1

        self.getPageId()
        #graph = graph1
        self.getPageAccessToken()
        self.graph = facebook.GraphAPI(access_token=self.token)
        #print(name)
        self.initializeComments()

    def getPageId(self):
        pages = self.graph.request('me/accounts')
        myPages = pages['data']
        for currentPage in myPages:
            if (currentPage['name'] == self.name):
                #global id
                self.id = currentPage['id']

    def getPageAccessToken(self):
        pages = self.graph.request('me/accounts')
        myPages = pages['data']
        for currentPage in myPages:
            if (currentPage['name'] == self.name):
                self.token = currentPage['access_token']

    def postOnPage(self, message):
        self.graph.put_object(parent_object=self.id, connection_name="feed", message=message)
        self.initializeComments()

    def getGraph(self):
        return self.graph

    def initializeComments(self):   #_ means private
        posts = self.graph.get_connections(id=self.id, connection_name="posts")
        posts = posts['data']
        
        for currentPost in posts:
            currentMessage = currentPost['message']
            currentId = currentPost['id']
            if not self.doesContainComment(currentId):
                newComment = Post(self, currentId, self.graph, currentMessage)
                newComment.message = currentMessage
                newComment.id = currentId
                newComment.graph = self.graph
                newComment.updateComments()
                self.commentArray.append(newComment)
        

            

    def getPost(self, idx):
        if idx >= len(self.commentArray):
            return self.commentArray[len(self.commentArray) - 1]
        
        if idx < 0:
            return self.commentArray[0]

        return self.commentArray[idx]

    def doesContainComment(self, thisId):
        for currentComment in self.commentArray:
            if currentComment.id == thisId:
                return True

        return False


    def postReply(self, message, thisId):
        self.graph.put_comment(object_id=thisId, message=message)



    
        