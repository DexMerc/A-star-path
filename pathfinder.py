import numpy as np
import random

open_list = []
closed_list = []


class Node(object):
    def __init__(self, parent, position):
        self.position = position
        self.parent = parent
        self.g = self.f = self.h = 0

    def __eq__(self, other):
        return self.position == other.position


def a_star(maze, start, end):
    global open_list
    global closed_list
    global n
    start_node = Node(None, start)
    end_node = Node(None, end)
    start_node.g = start_node.h = start_node.f = 0
    end_node.g = end_node.h = end_node.f = 0

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        ind = 0
        for index, item in enumerate(open_list):
            if current_node.f > item.f:
                current_node = item
                ind = index

        open_list.pop(ind)
        closed_list.append(current_node)

        if current_node == end_node:
            path = []
            curr = current_node
            while curr.parent is not None:
                path.append(curr.position)
                curr = curr.parent
            return path[::-1]

        children = []

        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if i == 0 and j == 0:
                    continue
                temp_pos = [current_node.position[0] + i, current_node.position[1] + j]
                if temp_pos[0] < 0 or temp_pos[0] >= len(maze) or temp_pos[1] < 0 or temp_pos[1] >= len(maze[0]):
                    continue
                if maze[temp_pos[0]][temp_pos[1]] == 0:
                    continue
                temp_node = Node(current_node, temp_pos)
                children.append(temp_node)

        for child in children:
            for closed_child in closed_list:
                if child == closed_child:
                    continue

            child.g = current_node.g + maze[current_node.position[0]][current_node.position[1]]
            child.h = ((child.position[0] - end_node.position[0]) ** 2) + (
                        (child.position[1] - end_node.position[1]) ** 2)
            child.f = child.g + child.h

            # Child is already in the open list
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            # Add the child to the open list
            open_list.append(child)


# def ret_path(current_node):
#     path = []
#     curr = current_node
#     while curr.parent is not None:
#         path.append(curr.position)
#         curr = curr.parent
#     return path[::-1]
