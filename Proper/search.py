import sys

class Node():
    def __init__(self, state , person , action):
        self.state = state
        self.person = person
        self.action = action

class StackFrontier():
    def __init__(self) -> None:
        self.frontier = []

    def add(self,node):
        self.frontier.append(node)

    def contain_state(self, state):
        return any(node.state == state for node in self.frontier)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def remove(self) :
        if self.empty():
            raise Exception("empty frontier")
        else :
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueFrontier(StackFrontier) :
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node 