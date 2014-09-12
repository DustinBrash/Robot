#Iterative Deepening A* (IDA_STAR) algorithm for vision by Vincent Pugliese and Dustin Brashear
#This is a memory sensitive version of A* in which nodes which have reached a certain 
#cost are immediately terminated (much like alpha-beta pruning)
#The search space is the areas of the plane of vision in which high intensity light has been detected
#The heuristic will start at one of 2 parallel lines and spread out to find the other matching line
#this serves 2 purposes, bouding the local region of intensity for later analysis, and pairing 
#lines when more that 2 lines fo the same slope exist
import contrast
#imports here
done = []#nodes already evaluated
#THE FOLLOWING PART OF CODE IS FOR TESTING PURPOSES ONLY
k = []
q = contrast.main()
k = q

#function needs to have argument "k" for contrast graph (nodes for eval), and parr for bounds/start
def IDASTAR(k):
	navMap = k #this is the map of nodes in which we are navigating
	while element in navMap:
		current = 
		#evaluate "current" (node) to see if it has reached the goal or if it has reached the cost
		#do that with if, elif, else statement
		
