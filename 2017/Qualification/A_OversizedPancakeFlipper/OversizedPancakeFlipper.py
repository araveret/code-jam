
def solver(S, K, case):   
    
    def flipper(S,y):
        if S[y] == '-':
            S = list(S)
            S[y] = '+'
            S = ''.join(S)
        else:
            S = list(S)
            S[y] = '-'
            S = ''.join(S)
        return S
    
    flips = 0
    
    if '-' in S:
        for n in range(len(S)-K+1):
            if S[n]=='-':
                flips+=1
                for x in range(K):
                    S = flipper(S,n+x)
    
    if '-' in S[-K:]:
        for x in range(1,K+1):
            S = flipper(S,-x)
    
    if '-' in S:
        print('CASE #{}: IMPOSSIBLE'.format(case))
    else:
        print('CASE #{}: {}'.format(case, flips))
        
import fileinput
f = fileinput.input()    
T = int(f.readline())

for case in range(1,T+1):
    S, K = f.readline().split()
    solver(S, int(K), case)