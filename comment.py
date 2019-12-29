import facebook
import time

class Comment(object):
    page = ""
    id = ""
    graph = ""
    message = ""
    comments = []
    def __init__(self, page1, id1, graph1, message1):
        global page
        page = page1
        global id
        id = id1
        global graph
        graph = graph1
        global message
        message = message1
        #self.updateComments()

    def updateComments(self):
        tempId = self.id
        #print("temp id " + tempId)
        posts = graph.get_connections(id=tempId, connection_name="comments")
        posts = posts['data']
        #print(posts)
        for currentPost in posts: #get comment array for page
            currentMessage = currentPost['message']
            currentId = currentPost['id']
            #print(currentMessage)
            if not self.doesContainComment(currentId):
                newComment = Comment(self, currentId, graph, currentMessage)
                newComment.message = currentMessage
                newComment.id = currentId
                newComment.graph = graph
                newComment.parentId = self.id
                newComment.updateComments()
                self.comments.append(newComment)
                #print(newComment.message)

    def listener(self):
        beforeArray = self.comments
        beforeLen = len(beforeArray)
        while beforeLen == len(self.comments):
            self.updateComments()
            #print("updated...")
            time.sleep(30)

        for currentComment in self.comments:
            if currentComment not in beforeArray:
                return currentComment

    def getId(self):
        return id

    def getMessage(self):
        return message


    def doesContainComment(self, thisId):
        for currentComment in self.comments:
            if currentComment.getId() == thisId:
                return True

        return False

    def putComment(self, message):
        self.graph.put_comment(object_id=self.id, message=message)