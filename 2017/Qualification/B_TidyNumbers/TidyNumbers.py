
def solver(K, case):   
    for num in range(len(K)):
        
    if '-' in S:
        print('CASE #{}: IMPOSSIBLE'.format(case))
    else:
        print('CASE #{}: {}'.format(case, flips))
        
import fileinput
f = fileinput.input()    
T = int(f.readline())

for case in range(1,T+1):
    K = f.readline()
    solver(int(K), case)