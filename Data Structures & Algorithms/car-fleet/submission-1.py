class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        total_carfleet = 0
        for i in range(len(position)):
            cars.append((position[i],speed[i]))
        cars.sort()
        max_time = 0
        for i in range(len(cars)-1,-1,-1):
            timetaken = (target - cars[i][0])/cars[i][1]
            if max_time < timetaken:
                max_time = timetaken
                total_carfleet +=1
        return total_carfleet
        