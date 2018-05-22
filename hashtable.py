class HashTable(object):
    def __init__(self, size):
        self.size = size
        self.slots = [None]*self.size  # where key is stored
        self.data = [None]*self.size  # where value is stored

    def put(self, key, data):
        # get the hash value
        hashvalue = self.hashfunction(key, len(self.slots))
        # new key
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data

        # existing key
        else:
            # if key is equal to the one in slots, simply update the new value
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data

            # collision
            else:
                # go to the next slot
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot, len(self.slots))
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:  # slots[nextslot] == key, simply update
                    self.data[nextslot] = data

    def hashfunction(self, key, size):
        return key % size

    def rehash(self, oldhash, size):
        # increment one to the hashvalue to avoid collision
        return (oldhash + 1) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))

                # if rehash go round one cycle, stop
                if position == startslot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


h = HashTable(5)
h[1] = 'one'
h[2] = 'two'
h[3] = 'three'
print('one' in h)
