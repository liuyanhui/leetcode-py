class LRUCache:
    def __init__(self, capacity: int):
        self.queue = []
        self.hashtable = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.hashtable:
            self.queue.remove(key)
            self.queue.append(key)
            return self.hashtable[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # 已经存在
        if key in self.hashtable:
            self.queue.remove(key)
            self.queue.append(key)
            self.hashtable[key] = value
        # 不存在
        else:
            # 队列已满
            if len(self.queue) >= self.capacity:
                # print(str(self.hashtable))
                # 删除队列头部元素
                tmp_key = self.queue.pop(0)
                self.hashtable.pop(tmp_key)
                # 新元素入队
                self.queue.append(key)
                self.hashtable[key] = value
            # 队列未满
            else:
                self.queue.append(key)
                self.hashtable[key] = value




                # Your LRUCache object will be instantiated and called as such:
                # obj = LRUCache(capacity)
                # param_1 = obj.get(key)
                # obj.put(key,value)
