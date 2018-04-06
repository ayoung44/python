import datetime

''' user 이름'''
class User:
    def __init__(self):
        self.name = []
        self.postList = {}
        self.post = post_info()

    def getName(self):
        name = input('이름을 입력해주세요.')
        self.name.append(name)
    def addPost(self):
        self.post.postUi()
        self.post.postContent()
        self.postList[self.post.postName] = self.post.content

class post_info:
    def postUi(self):
        print('=' * 30)
        self.postName = input('게시글 이름: ')

    def postContent(self):
        self.content = input('내용을 입력하세요.')

a=User()
a.addPost()

print(a.postList)
