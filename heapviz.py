# Module to draw a heap using graphviz in a nice "textbook" layout
# Created by Zachary Friggstad, 2018
# Only works with the BinaryHeap class we developed in 275

from graphviz import Digraph
from binary_heap import BinaryHeap
import random
import copy

def convert_pos_string(pos, padding):
    return str(pos[0]*padding)+','+str(pos[1])+'!'

def heapviz(heap, just_keys = False, padding = 0.6):
    """
    Draw a list representing a binary heap using graphviz.

    heap: An instance of BinaryHeap

    padding: reflects the amount of space between nodes (horizontally)
    Increase it beyond the default 0.6 if the circles are mashed together.

    just_keys: True if only the keys should be displayed. False
    if the (item, key) pairs should be displayed.
    """

    dot = Digraph()

    nodes = heap.nodes

    dot.attr("node", fontname="helvetica-bold", fontsize="20")

    if len(heap) == 0:
        dot.node("empty heap", style="dashed")
        return dot

    # if len(heap) == 1:
    #     dot.node(str(heap[0]))
    #     return dot

    max_level = 0
    while 2**(max_level+1)-1 < len(heap):
        max_level += 1

    pos = {0:[0,0]}

    def draw_label(i):
        if just_keys:
            output = str(nodes[i][1])
        else:
            output = str(nodes[i][0]) + "," + str(nodes[i][1])
        dot.node(str(i), output, pos=convert_pos_string(pos[i], padding))

    #dot.node(str(heap[0]), pos=convert_pos_string(pos[0], padding))
    draw_label(0)

    level = 0
    for i in range(1, len(heap)):
        if i >= 2**(level+1)-1:
            level += 1
        parent = (i-1)//2
        pos[i] = copy.copy(pos[parent])
        if i%2 == 0:
            pos[i][0] += 2**(max_level-level)
        else:
            pos[i][0] -= 2**(max_level-level)
        pos[i][1] -= 1

        #dot.node(str(heap[i]), pos=convert_pos_string(pos[i], padding))
        draw_label(i)
        dot.edge(str(parent), str(i))

    dot.engine="neato"
    return dot

if __name__ == "__main__":
    heap = BinaryHeap()

    for c in ["dog", "cat", "bear", "deer", "cat", "monkey", "hippo",
              "hawk", "frog", "dog", "dog", "moose", "fish", "cougar"]:
        heap.insert(c, random.randrange(10))

    # dot = heapviz(heap, padding = 1.2)

    # try the one below, only the keys are displayed
    dot = heapviz(heap, just_keys = True, padding = 0.8)

    dot.render(view=True)
