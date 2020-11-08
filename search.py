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
    return [s, s, w, s, w, w, s, w]


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

    "1. Initialize the frontier using the initial state of problem"
    frontier = util.Stack()          # use a stack to implement the frontier of nodes to be explored
    start = problem.getStartState()  # start
    frontier.push((start, []))       # add the start node - state and action(path) - to the frontier
    nodes_available = True           # boolean variable to ensure that there are nodes available to explore
    nodes_explored = []              # list of nodes explored

    # if the start node is the goal state, return solution path to the start node, which is an empty list
    if problem.isGoalState(start):
        return []

    "2. loop do"
    # loop to iterate over the nodes on the frontier. Runs as long as the goal state is not reached
    while nodes_available:

        "3. if the frontier is empty, return failure"
        # if the frontier is empty, print an error message and return an empty list
        if frontier.isEmpty():
            nodes_available = False
            print('The frontier is empty. Failure to return node!')
            return []

        "4. else choose a node and remove it from the frontier"
        current_state, path = frontier.pop()   # remove the top node from the frontier and set the state & path (action)
        nodes_explored.append(current_state)   # add the current node (state) to the list of nodes explored

        "5. if the node contains a goal state, return solution"
        # if the current node is the goal state, return the directions aka the path to the current node
        if problem.isGoalState(current_state):
            return path

        "6. else expand the chosen node"
        # get the successor to the current node, to continue to graph search for the goal node
        # getSuccessors() returns a list of triples, successor, action and stepCost
        successor_nodes = problem.getSuccessors(current_state)

        "7. add all the neighboring nodes of the expanded node to the frontier"
        # iterate through the list of successor_nodes
        for successor, action, stepCost in successor_nodes:
            # check if the next succeeding node has already been explored or not
            # if the node is not in the nodes_explored list, update the path to the node push it to the frontier
            if successor not in nodes_explored:
                successor_node_path = path + [action]
                frontier.push((successor, successor_node_path))

    util.raiseNotDefined()


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    "1. Initialize the frontier using the initial state of problem"
    frontier = util.Queue()          # use a queue to implement the frontier of nodes to be explored
    start = problem.getStartState()  # start
    frontier.push((start, []))       # add the start node - state and action/path - to the frontier
    nodes_available = True           # boolean variable to ensure that there are nodes available to explore
    nodes_explored = []              # list of nodes explored

    # if the start node is the goal state, return solution path to the start node, which is an empty list
    if problem.isGoalState(start):
        return []

    "2. loop do"
    # loop to iterate over the nodes on the frontier. Runs as long as the goal state is not reached
    while nodes_available:

        "3. if the frontier is empty, return failure"
        # if the frontier is empty, print an error message and return an empty list
        if frontier.isEmpty():
            nodes_available = False
            print('The frontier is empty. Failure to return node!')
            return []

        "4. else choose a node and remove it from the frontier"
        current_state, path = frontier.pop()   # remove the top node from the frontier and set the state & path (action)

        "5. if the node contains a goal state, return solution"
        # if the current node is the goal state, return the directions aka the path to the current node
        if problem.isGoalState(current_state):
            return path

        # check to ensure we don't explore the same node twice i.e check that current node hasn't already been visited
        if current_state not in nodes_explored:
            nodes_explored.append(current_state)   # add the current node (state) to the list of nodes explored
            "6. else expand the chosen node"
            # get the successor to the current node, to continue to graph search for the goal node
            # getSuccessors() returns a list of triples, successor, action and stepCost
            successor_nodes = problem.getSuccessors(current_state)

            "7. add all the neighboring nodes of the expanded node to the frontier"
            # iterate through the list of successor_nodes
            for successor, action, stepCost in successor_nodes:
                # check if the next succeeding node has already been explored or not
                # if the node is not in the nodes_explored list, update the path to the node push it to the frontier
                if successor not in nodes_explored:
                    successor_node_path = path + [action]
                    frontier.push((successor, successor_node_path))

    util.raiseNotDefined()


def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    frontier = util.PriorityQueue()  # use a priority queue to implement the frontier of nodes to be explored
    start = problem.getStartState()  # start
    frontier.push((start, []), 0)    # add the start node - state and action(path), and the priority to the frontier
    nodes_available = True           # boolean variable to ensure that there are nodes available to explore
    nodes_explored = []  # list of nodes explored

    # if the start node is the goal state, return solution path to the start node, which is an empty list
    if problem.isGoalState(start):
        return []

    # loop to iterate over the nodes on the frontier. Runs as long as the goal state is not reached
    while nodes_available:

        # if the frontier is empty, print an error message and return an empty list
        if frontier.isEmpty():
            nodes_available = False
            print('The frontier is empty. Failure to return node!')
            return []

        current_state, path = frontier.pop()  # remove the top node from the frontier and set the state & path (action)

        # if the current node is the goal state, return the directions aka the path to the current node
        if problem.isGoalState(current_state):
            return path

        # check to ensure we don't explore the same node twice i.e check that current node hasn't already been visited
        if current_state not in nodes_explored:
            nodes_explored.append(current_state)  # add the current node (state) to the list of nodes explored

            # get the successor to the current node, to continue to search for the goal node
            # getSuccessors() returns a list of triples, successor, action and stepCost
            successor_nodes = problem.getSuccessors(current_state)

            # iterate through the list of successor_nodes
            for successor, action, stepCost in successor_nodes:
                # check if the next succeeding node has already been explored or not. if not, then
                # update the path to the node, calculate the cost of the action,
                # and then push the node and its cost, which is the priority attached to it, to the frontier
                if successor not in nodes_explored:
                    successor_node_path = path + [action]                                # update path
                    successor_action_cost = problem.getCostOfActions(successor_node_path)  # get cost of updated path
                    frontier.push((successor, successor_node_path), successor_action_cost)

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

    frontier = util.PriorityQueue()  # use a priority queue to implement the frontier of nodes to be explored
    start = problem.getStartState()  # start
    # add the start node - state and action(path), and the null heuristic to the frontier
    frontier.push((start, []), nullHeuristic(start, problem))
    nodes_available = True           # boolean variable to ensure that there are nodes available to explore
    nodes_explored = []  # list of nodes explored

    # if the start node is the goal state, return solution path to the start node, which is an empty list
    if problem.isGoalState(start):
        return []

    # loop to iterate over the nodes on the frontier. Runs as long as the goal state is not reached
    while nodes_available:

        # if the frontier is empty, print an error message and return an empty list
        if frontier.isEmpty():
            nodes_available = False
            print('The frontier is empty. Failure to return node!')
            return []

        current_state, path = frontier.pop()  # remove the top node from the frontier and set the state & path (action)

        # if the current node is the goal state, return the directions aka the path to the current node
        if problem.isGoalState(current_state):
            return path

        # check to ensure we don't explore the same node twice i.e check that current node hasn't already been visited
        if current_state not in nodes_explored:
            nodes_explored.append(current_state)  # add the current node (state) to the list of nodes explored

            # get the successor to the current node, to continue to search for the goal node
            # getSuccessors() returns a list of triples, successor, action and stepCost
            successor_nodes = problem.getSuccessors(current_state)

            # iterate through the list of successor_nodes
            for successor, action, stepCost in successor_nodes:
                # check if the next succeeding node has already been explored or not. if not, then
                # update the path to the node, calculate the cost, which is the cumulative backward cost + heuristics,
                # and then push the node and its cost, which is the priority attached to it, to the frontier
                if successor not in nodes_explored:
                    successor_node_path = path + [action]                                # update path
                    # f(n) =  g(n) (aka backward cost) + h(n) (aka forward cost / heuristic)
                    action_total_cost = problem.getCostOfActions(successor_node_path) + heuristic(successor, problem)
                    frontier.push((successor, successor_node_path), action_total_cost)

    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch