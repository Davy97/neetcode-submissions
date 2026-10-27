"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        m = 0
        counter = 0
        times = []
        prev = -1
        
        for interval in intervals:
            times.append((interval.start,1))
            times.append((interval.end,-1))
        times.sort()
      
        for i in range(len(times)):
                
            counter += times[i][1]
            
            m = max(m,counter)
            
       



        return max(counter,m)
        

            


        