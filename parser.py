import argparse
import random
import re

'''
this code is dedicated to my beloved, 
the best and the most beautiful in the world, to Ilvina <3

Roses are red,
The rain is blue,
You always beautiful,
Isn't that true?
'''

class Message:
    sender = None
    date = None
    text = None

    def __init__(self, sender, date, text):
        self.sender = sender
        self.text = text
        self.date = date

    def __str__(self):
        return '[{}] ({}) {}'.format(self.date, self.sender, self.text)

def parse(text):
    lines = text.split('\n')
    senders = {}
    messages = []


    for line in lines:
        parts = line.split(' - ')
        if len(parts) == 0:
            continue
        elif re.match(r'\d\d\.\d\d\.\d\d, \d\d:\d\d', parts[0]) is None:
            messages[-1].text += [line[:-1]]
        else:
            if ':' not in parts[1]:
                continue
            sender = parts[1].split(':')[0]
            line = []
            if ': ' in parts[1]:
                line = [parts[1].split(': ')[1]]
            if len(parts) >= 2:
                line += parts[2:]
            line = ' - '.join(line)
            message = Message(sender, parts[0], [line])
            messages.append(message)
            if message.sender not in senders.keys():
                senders[message.sender] = {'messages_count': 0, 'color': '#' + ''.join(random.choices("0123456789abcdef", k=6))}
            senders[message.sender]['messages_count'] += 1
    return messages
