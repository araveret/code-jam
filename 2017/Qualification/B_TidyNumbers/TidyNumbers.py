
def solver(K, case):   
	if len(K)>1:
	    for x in range(1,len(K)):
	        if int(K[-x]) < int(K[-x-1]):
	        	K = list(K)
	        	K[-x:] = ['9']*len(K[-x:])
	        	K[-x-1] = str(int(K[-x-1])-1)
	        	K = ''.join(K)
	    print('CASE #{}: {}'.format(case, str(int(K))))
	else:
		print('CASE #{}: {}'.format(case, str(int(K))))

import fileinput
f = fileinput.input()    
T = int(f.readline())

for case in range(1,T+1):
    K = f.readline().split()[0]
    solver(K, case)