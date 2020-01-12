from collections import deque

graf = {}
graf['a1'] = ['b2', 'c2']
graf['c2'] = ['d3', 'e3', 'f3']

q = deque()
q.extend(graf['a1'])

searched = []

while q:
    print q
    el = q.popleft()
    if not el in searched:
        if el == 'e3':
            print 'Yes'
            break
        searched.append(el)
        next_p = graf.get(el)
        if next_p:
            q.extend(next_p)
