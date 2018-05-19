# matrix list
M = [['cr7', 'benzema', 'bale'],
     ['isco','modric','jamesr'],
     ['marcelo','ramos','varane']]

print('sequence 1',M[0][0])
# col2 = [row[0] for row in M]
col2 = [M[i][i] for i in [0,1,2]]
print(col2)

# tuple things
rmad =('arjun', 'james', 'bale')
lfc = ('milner', 'mosalah', 'mane')
tmatch = ('hnder', lfc)

# rmad.append('dog') wont work tuple!

print('lfc all', len(tmatch))
print('lfc payer 3', tmatch[1][1])

# dictionary
ab = {'11': 'mosalah', '8' :'Stevie G',
       '7': 'milner', '9': 'Firmino'}

print('dictionary 8',ab['8'])

ab['4'] = 'vandjirk'

print('number 4 {} and total length {} '.format(ab['4'], (len(ab))))


Madlist = ['modric', 'CR7', 'marcelo']
print('number of madlist', len(Madlist))
Madlist.append('benzema')
Madlist.remove('marcelo')
print('new squad', Madlist)
