import facebook
import time
from comment import Comment

class Post(object):
    page = ""
    id = ""
    graph = ""
    message = ""
    comments = []
    token = ""
    def __init__(self, page1, id1, graph1, message1):
        self.page = page1
        self.id = id1
        self.graph = graph1
        self.message = message1
        #self.token = page1.token
        #print(self.token)

    def putComment(self, insertMessage):
        self.graph.put_comment(object_id=self.id, message=insertMessage)
        self.updateComments()

    def updateComments(self):

        posts = self.graph.get_connections(id=self.id, connection_name="comments")
        posts = posts['data']
        #print(posts)
        for currentPost in posts: #get comment array for page
            currentMessage = currentPost['message']
            currentId = currentPost['id']
            #print(currentMessage)
            if not self.doesContainComment(currentId):
                newComment = Comment(self, currentId, self.graph, currentMessage)
                newComment.message = currentMessage
                newComment.id = currentId
                newComment.graph = self.graph
                self.comments.append(newComment)
                #print(newComment.message)

    def listener(self):
        beforeArray = self.comments
        beforeLen = len(beforeArray)
        while beforeLen == len(self.comments):
            #print(beforeLen)
            self.updateComments()
            #print("updated...")
            time.sleep(10)
            #print(len(self.comments))

        return self.comments[len(self.comments) - 1]

    def doesContainComment(self, thisId):
        for currentComment in self.comments:
            if currentComment.id == thisId:
                return True

        return False