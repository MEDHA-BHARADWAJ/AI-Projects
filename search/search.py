# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    
def checkElementNotInCLosed(item,closed):
    if(item not in closed):
        return True
    else:
        return False
    
def getFringe(searchType):
    from util import PriorityQueue,Stack,Queue
    if(searchType == "dfs"):
        return Stack()
    elif(searchType == "bfs"):
        return Queue()
    elif(searchType == "ucs"):
        return PriorityQueue()
    else:
        print("unknown search type")
    
def genericSearch(problem,searchType):
    """Generic Search"""
    from util import Stack
    currentNode = dict({'state':(problem.getStartState(),'Undefined',0),'parent':'none'})
    
    closedNodes = []
    openNodes = getFringe(searchType)
    path = Stack()
    while not (problem.isGoalState(currentNode['state'][0])):
        closedNodes.append(currentNode['state'][0])
        successors = problem.getSuccessors(currentNode['state'][0])
        for s in successors:
            if not (s[0] in closedNodes):
                newNode = dict({'state': s,'parent': currentNode})
                openNodes.push(newNode)
        while not(openNodes.isEmpty()):
            x = openNodes.pop()
            if(checkElementNotInCLosed(x['state'][0],closedNodes)):
                currentNode = x
                break
                
    while not (currentNode['parent'] == 'none'):
        path.push(currentNode['state'][1])
        currentNode = currentNode['parent']
    result = []
    while not(path.isEmpty()):
        n = path.pop()
        result.append(n)
        
    return result

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    path = genericSearch(problem, "dfs")
    return path
    util.raiseNotDefined()
    
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    path = genericSearch(problem, "bfs")
    return path
    util.raiseNotDefined()
    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    from util import Stack
    currentNode = dict({'state':(problem.getStartState(),'Undefined',0),'parent':'none'})
    
    closedNodes = []
    openNodes = util.PriorityQueue()
    path = Stack()
    while not (problem.isGoalState(currentNode['state'][0])):
        closedNodes.append(currentNode['state'][0])
        successors = problem.getSuccessors(currentNode['state'][0])
        for s in successors:
            if not (s[0] in closedNodes):
                priority = s[2] + currentNode['state'][2]
                newNode = dict({'state': (s[0],s[1],priority),'parent': currentNode})
                openNodes.push(newNode, priority)
        while not(openNodes.isEmpty()):
            x = openNodes.pop()
            if(checkElementNotInCLosed(x['state'][0],closedNodes)):
                currentNode = x
                break
                
    while not (currentNode['parent'] == 'none'):
        path.push(currentNode['state'][1])
        currentNode = currentNode['parent']
    result = []
    while not(path.isEmpty()):
        n = path.pop()
        result.append(n)
        
    return result
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    
    from util import Stack
    currentNode = dict({'state':(problem.getStartState(),'Undefined',0),'parent':'none'})
    
    closedNodes = []
    openNodes = util.PriorityQueue()
    path = Stack()
    while not (problem.isGoalState(currentNode['state'][0])):
        closedNodes.append(currentNode['state'][0])
        successors = problem.getSuccessors(currentNode['state'][0])
        for s in successors:
            if not (s[0] in closedNodes):
                priority = s[2] + currentNode['state'][2]
                newNode = dict({'state': (s[0],s[1],priority),'parent': currentNode})
                openNodes.push(newNode, priority+heuristic(newNode['state'][0],problem))
        while not(openNodes.isEmpty()):
            x = openNodes.pop()
            if(checkElementNotInCLosed(x['state'][0],closedNodes)):
                currentNode = x
                break
                
    while not (currentNode['parent'] == 'none'):
        path.push(currentNode['state'][1])
        currentNode = currentNode['parent']
    result = []
    while not(path.isEmpty()):
        n = path.pop()
        result.append(n)
        
    return result
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
