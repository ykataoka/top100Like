class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        queue = []
        hashmap = {}
        
        # create the hash map
        for height, peopleahead in people:
            if height not in hashmap:
                hashmap[height] = [peopleahead]
            else:
                hashmap[height].append(peopleahead)
                
        heightFromTop = sorted(hashmap.keys(), reverse=True)

        # O(N) even though this is double loop.
        for height in heightFromTop:
            # retrieve the index list at the same height
            index_list = sorted(hashmap[height])
            for index in index_list:
                print(index)
                queue.insert(index, [height, index])
        return queue
