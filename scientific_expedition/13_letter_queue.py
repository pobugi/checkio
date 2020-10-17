"""
In computer science, a queue is a particular kind of data type in which the entities in the collection are kept
in order and the principal operations on the collection are the addition of entities to the rear terminal position
(enqueue or push), and removal of entities from the front terminal position (dequeue or pop).
This makes the queue a First-In-First-Out (FIFO) data structure. In a FIFO data structure, the first element added to
the queue will be the first one to be removed. This is equivalent to the requirement that once a new element is added,
all elements that were added before have to be removed before the new element can be removed.

We will emulate the queue process with Python. You are given a sequence of commands:
- "PUSH X" -- enqueue X, where X is a letter in uppercase.
- "POP" -- dequeue the front position. if the queue is empty, then do nothing.
The queue can only contain letters.

You should process all commands and assemble letters which remain in the queue in one word from the front to the rear
of the queue.
"""


from typing import List


def letter_queue(commands: List[str]) -> str:
    res = ''
    for element in commands:
        command = element.split()[0]
        if command == 'PUSH':
            value = element.split()[1]
            res += value
        elif command == 'POP':
            if res:
                res = res[1:]
    return res


if __name__ == '__main__':
    print("Example:")
    print(letter_queue(['PUSH A',
                        'POP',
                        'POP',
                        'PUSH Z',
                        'PUSH D',
                        'PUSH O',
                        'POP',
                        'PUSH T']))

    assert letter_queue(['PUSH A',
                            'POP',
                            'POP',
                            'PUSH Z',
                            'PUSH D',
                            'PUSH O',
                            'POP',
                            'PUSH T']) == 'DOT'
    assert letter_queue(['POP', 'POP']) == ''
    assert letter_queue(['PUSH H', 'PUSH I']) == 'HI'
    assert letter_queue([]) == ''
    print("Coding complete? Click 'Check' to earn cool rewards!")
