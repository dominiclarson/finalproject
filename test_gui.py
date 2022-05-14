import pytest
from gui import *

class Test:
    def setup_method(self):
        self.window = Tk()
        self.tester = GUI(self.window)
            
    def teardown_method(self):
        del self.window
        
    def test_init(self):
        assert self.window.__str__() == '.'
        
    def test_clicked(self):
        assert self.tester.clicked() == None
        
    def test_search(self):
        assert self.tester.find() == None

if __name__ == '__main__':
    pytest.main()
