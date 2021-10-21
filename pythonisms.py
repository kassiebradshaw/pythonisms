class Favorite:
    def __init__(self, collection=None):
        self.collection = []
    
    def __str__(self):
        return "Favorites"
    
    def __len__(self):
        return len(self.collection)
    
    def __iter__(self):
        def generator():
            for x in self.collection:
                yield x
        return generator()
    
    def add(self, favorite):
        self.collection.append(favorite)

