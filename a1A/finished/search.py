"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
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
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()

def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    "DFS uses a FILO data structure to implement it"
    frontier = util.Stack()
    exploredSet = []

    "each element in the frontier refers to a tuple: (path: list, actions: list)"
    frontier.push((problem.getStartState(), []))
    while False == frontier.isEmpty():
        state, acts = frontier.pop()
        # when reach the goal
        if problem.isGoalState(state):
            # print(acts)
            return acts
        # when not explored
        if state not in exploredSet:
            # now explored
            exploredSet.append(state)
            # get successors and push them into the frontier if not explored
            successors = problem.getSuccessors(state)
            for successor in successors:
                if successor[0] not in exploredSet:
                    frontier.push((successor[0], acts + [successor[1]]))


def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    "BFS uses a FIFO data structure to implement it"
    frontier = util.Queue()
    exploredSet = []

    "each element in the frontier refers to a tuple: (path: list, actions: list)"
    frontier.push((problem.getStartState(), []))
    while False == frontier.isEmpty():
        state, acts = frontier.pop()
        # when reach the goal
        if problem.isGoalState(state):
            return acts
        # when not explored
        if state not in exploredSet:
            # now explored
            exploredSet.append(state)
            # get successors and push them into the frontier if not explored
            successors = problem.getSuccessors(state)
            for successor in successors:
                if successor[0] not in exploredSet:
                    frontier.push((successor[0], acts + [successor[1]]))



def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    "UCS uses a priority queue structure to implement it"
    frontier = util.PriorityQueueWithFunction(lambda x: x[2])
    exploredSet = []

    "Each element in the frontier refers to a tuple: (path: list, actions: list, priority: int)"
    "use cost to represent priority"
    "use the 2nd element in the tuple as the function to indicate the priority"
    frontier.push((problem.getStartState(), [], 0))
    while False == frontier.isEmpty():
        state, acts, priority = frontier.pop()
        # when reach the goal
        if problem.isGoalState(state):
            # print(acts)
            return acts
            # when not explored
        if state not in exploredSet:
            # now explored
            exploredSet.append(state)
            successors = problem.getSuccessors(state)
            for successor in successors:
                if successor[0] not in exploredSet:
                    frontier.push((successor[0], acts + [successor[1]], priority + successor[2]))


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    "A* uses a priority queue structure to implement it"
    frontier = util.PriorityQueueWithFunction(lambda x: x[2])
    exploredSet = []

    "Each element in the frontier refers to a tuple: (path: list, actions: list, priority: int)"
    "use cost(forward + backward) to represent priority"
    "use the 2nd element in the tuple as the function to indicate the priority"
    startState = problem.getStartState()
    frontier.push((startState, [], 0 + heuristic(startState, problem)))
    while False == frontier.isEmpty():
        state, acts, priority = frontier.pop()
        # when reach the goal
        if problem.isGoalState(state):
            # print(acts)
            return acts
            # when not explored
        if state not in exploredSet:
            # now explored
            exploredSet.append(state)
            successors = problem.getSuccessors(state)
            for successor in successors:
                if successor[0] not in exploredSet:
                    frontier.push((successor[0], acts + [successor[1]], priority + successor[2] - heuristic(state, problem) + heuristic(successor[0], problem)))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
