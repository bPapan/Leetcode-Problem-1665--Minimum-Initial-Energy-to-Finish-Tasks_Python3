class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        
        rem_energy = min_energy = sum(task[0] for task in tasks)   #At first, minimum total energy=total actual energy
        
        tasks = sorted(tasks, key =lambda x:x[0]-x[1])             #Reverse sort the tasks based on the difference between the minimum and actual
        
        for task in tasks:
            if task[1]>rem_energy:                                 #The minimum energy of the task is greater than the total remaining energy
                min_energy+=task[1]-rem_energy                     #So we need more energy
                rem_energy+=task[1]-rem_energy
            rem_energy-= task[0]                                   #Some energy is spent to do the task, so reduce  the amount of total remaining energy
                
        return min_energy
