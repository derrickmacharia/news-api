import unittest
from models import sources
Sources = sources.Sources

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