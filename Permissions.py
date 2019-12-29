import facebook
import json
import requests

class Perm(object):
    contents = ""
    def __init__(self, jsonName, version):
        with open(jsonName, 'r') as f:
            global contents
            contents = json.load(f)
    

    def getAppId(self):
        id = contents['app']['id']
        return id
    
    def getAppSecret(self):
        secret = contents['app']['secret']
        return secret

    def getUserShortToken(self):
        token = contents['user']['short_token']
        return token
    
    def getUserLongToken(self):
        token = contents['user']['long_token']
        return token

    def getGraph(self):
        longToken = self.getUserLongToken()
        graph = facebook.GraphAPI(longToken)
        return graph

    def getPageId(self, pageName):
        graph = facebook.GraphAPI(access_token=self.getUserLongToken())
        pages = graph.request('me/accounts')
        myPages = pages['data']
        for currentPage in myPages:
            if (currentPage['name'] == pageName):
                return currentPage['id']

    def getPageToken(self, pageName):
        pageArray = contents['page']
        for currentPage in pageArray:

            if currentPage['name'] == pageName:
                return currentPage['token']

        return "Couldn't find Page Token"

    def printPages(self):
        graph = facebook.GraphAPI(access_token=self.getUserLongToken())
        pages = graph.request('me/accounts')
        myPages = pages['data']
        for currentPage in myPages:
            print(currentPage['name'])

    def getPageAccessToken(self, pageName):
        graph = facebook.GraphAPI(access_token=self.getUserLongToken())
        pages = graph.request('me/accounts')
        myPages = pages['data']
        for currentPage in myPages:
            if (currentPage['name'] == pageName):
                return currentPage['access_token']

        return "Page not found"
