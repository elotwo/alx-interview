#!/usr/bin/python3
def canUnlockAll(boxes):
    n = len(boxes);
    opened_boxes = set([0])
    stack = [0]
    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key not in opened_boxes and key < n:
                opened_boxes.add(key)
                stack.append(key)
    return len(opened_boxes) == n
