class MyHashMap:
    DEFAULT_SIZE = 1000001
    def __init__(self):
        self.map=[0]*self.DEFAULT_SIZE
        self.present=[False]*self.DEFAULT_SIZE
    def put(self, key, value):
        self.map[key] = value
        self.present[key]=True
    def get(self, key):
        if self.present[key]:
            return self.map[key]
        else:
            return -1    
    def remove(self, key):
        self.present[key] = False
     


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
