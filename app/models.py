class Sources:
    '''
    Source class to define Source Objects
    '''

    def __init__(self,id,name,description,url,category,country):
        self.id =id
        self.name = name
        self.description = description
        self.url = "http://us.cnn.com"+ url
        self.category = category
        self.country = country


class Articles:
    """
     '''
    Article  class to define Article Objects
    '''
    """
    def __init__(self,id,name,description,author,url,title,urlToImage,content,publishedAt):
        self.id =id
        self.name = name
        self.description = description
        self.author = author
        self.url = url
        self.title = title
        self.urlToImage=urlToImage
        self.content= content
        self.publishedAt= publishedAt
       