#!/usr/bin/env python3
import sys
import parser
import random

ce = 6 # Количество слогов
length = 8 # Длина в строках
tr = 0 # Тип рифмы

allowed_chars = 'абвгдёежзийклмнопрстуфхцчшщыъьэюя,-'
vowels = 'ёеыаоэяию'
seps = '.!?'

def clean_line(line):
    res = []
    sent = ''
    for i in line.lower():
        if i in allowed_chars:
            sent += i
        elif i in seps:
            if sent.split() != []:
                q=sent.split()
                res.append(' '.join(q))
            sent = ''
        else:
            sent += ' '
    if sent.split() != []:
        res.append(' '.join(sent.split()))
    return res

def count_syls(line):
    x = 0
    ss = False
    for i in line:
        if i in vowels and not ss:
            ss = True
        if i not in vowels and ss:
            ss = False
            x += 1
    if ss:
        x += 1
    return x
    

if len(sys.argv) < 2:
    print(sys.argv[0], ' <whatsapp chat>')
    exit(-1)

file = open(sys.argv[1])
messages = parser.parse(file.read())
file.close()

sentences = []

for msg in messages:
    for line in msg.text:
        sents = clean_line(line)
        sentences += sents

sentences = list(set(sentences))

syls = {}

for sent in sentences:
    s = count_syls(sent)
    if syls.get(s) is None:
        syls[s] = []
    syls[s].append(sent)

'''
for i in sorted(syls.keys()):
    print('Предложений из', i, 'слогов:', len(syls[i]))
'''

pl = 2 # Длина конца

if tr == 0:
    res = []
    res.append(random.choice(syls[ce]))

    for i in range(length - 1):
        ending = res[-1][-pl:]
        ok = []
        for j in syls[ce]:
            if j.endswith(ending):
                ok.append(j)
        res.append(random.choice(ok))

    print('\n'.join(res))
elif tr == 1:
    res = []
    res.append(random.choice(syls[ce]))
    res.append(random.choice(syls[ce]))

    for i in range(length - 2):
        ending = res[-2][-pl:]
        ok = []
        for j in syls[ce]:
            if j.endswith(ending):
                ok.append(j)
        res.append(random.choice(ok))
    print('\n'.join(res))
