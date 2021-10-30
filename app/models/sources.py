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