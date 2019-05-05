

fp = open("./pyTest/nn",'r')
con = {'hash':'','l' : '' , 'r' : ''}
node = []

for i in range(50) :
	node.append({'hash':'','l':'','r':''})

def pushUp(i) :
    node[i]['hash'] = node[i << 1]['hash'] + node[i << 1 | 1]['hash']

 #   node[i]['hash'] = sha256(node[i << 1]['hash'], node[i << 1 | 1]['hash'] )

def build(i,l,r) :
	
    print(i,l,r)
    node[i]['l'] = l
    node[i]['r'] = r
   # sum[i]=0
    if(l == r) :
        node[i]['hash'] = fp.readline()
        node[i]['hash'].rstrip('\n')
        return

    m = int((l + r) / 2)
    build(i << 1, l, m)
    build(i << 1 | 1, m + 1, r)
    pushUp(i)


build(1,1,6)

fp.close()
print('finish!\n')
