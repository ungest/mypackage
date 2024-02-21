from mypackage import myModule

def test():
    assert myModule.top_n([76, 235, 794, 7293, 13, 52, 5241], 4) == [7293, 5241, 794, 235], 'Incorrect output'
    assert myModule.top_n([8, 9, 4, 0, 2], 2) == [9, 8], 'Incorrect output'
    assert myModule.top_n([6, 80, 50, 14, 65], 3) == [80, 50, 65], 'Incorrect output'