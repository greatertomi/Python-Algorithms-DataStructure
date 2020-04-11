import hashlib
import datetime

class Block:
    def __init__(self, data, previous_hash):
        self.timestamp = self.get_timestamp()
        self.data = data
        self.next = None
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    @staticmethod
    def calc_hash():
        sha = hashlib.sha256()
        hash_string = "We are going to encode this string".encode('utf-8')
        sha.update(hash_string)
        return sha.hexdigest()

    @staticmethod
    def get_timestamp():
        now = datetime.datetime.now()
        return now.strftime("%H:%M %Y-%m-%d")

    def __repr__(self):
        return f"Block\nTimeStamp: {self.timestamp}\nData: {self.data}" \
               f"\nSHA256 Hash: {self.hash}\n"


class BlockChain:
    def __init__(self):
        self.head = None
        self.length = 0

    def push(self, value):
        if self.head is None:
            self.head = Block(value, None)
        else:
            block = Block(value, self.head)
            current_block = self.head
            while current_block.next:
                current_block = current_block.next
            current_block.next = block
        self.length += 1
        return

block_chain = BlockChain()
block_chain.push('Good Morning')
block_chain.push('Hello, I love biscuit')
block_chain.push('Love computers')
block_chain.push('Have Tea')

block_head = block_chain.head
while block_head:
    print(block_head)
    block_head = block_head.next
