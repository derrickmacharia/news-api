import unittest

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


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_sources = Sources("cnn","CNN",
        "View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN","http://us.cnn.com","general","us")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_sources,Sources))


if __name__ == '__main__':
    unittest.main()