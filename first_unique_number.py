'''
Problem 28 - 28/07/2020
You have a queue of integers, you need to retrieve the first unique integer in the queue.
Implement the FirstUnique class:
    FirstUnique(int[] nums) Initializes the object with the numbers in the queue.
    int showFirstUnique() returns the value of the first unique integer of the queue, and returns -1 if there is no such integer.
    void add(int value) insert value to the queue.
'''
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = []
        self.dict ={}
        for i in nums:
            self.add(i)
        

    def showFirstUnique(self) -> int:
        while len(self.q)>0 and self.dict[self.q[0]]>1:
            self.q.pop(0)
        if len(self.q)==0:
            return -1
        else: 
            return self.q[0]
        

    def add(self, value: int) -> None:
        if value in self.dict:
            self.dict[value]+=1
        else:
            self.dict[value]=1
            self.q.append(value)
  

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value) 
