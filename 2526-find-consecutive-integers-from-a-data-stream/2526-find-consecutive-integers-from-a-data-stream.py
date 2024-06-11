class DataStream:

    def __init__(self, value: int, k: int):
        self.key_ = value
        self.target_counter_ = k
        self.counter_ = 0
        

    def consec(self, num: int) -> bool:
        if num == self.key_:
            self.counter_ += 1
            if self.counter_ == self.target_counter_:
                self.counter_ -= 1
                return True
        else:
            self.counter_ = 0
            return False

# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)