import pcapkit
#from cyclic import *
extraction=pcapkit.extract(fin='abhi.pcap',nofile=True,engine='dpkt')
k=1
ciphertext=''

for i in extraction.frame:
    try:
        
        if i['data']['p']==6:
            try:
                l=i['data']['data']['data']
                st= l.__str__()
                if st!="b''" and len(st.split('x'))==1:
                    
                    ciphertext=st[1:]
                    print(ciphertext[1:-1])
                    print(k)
            except:
                pass
    except:
        pass
    k=k+1
# call ur cyclic function
#cyclic(ciphertext)