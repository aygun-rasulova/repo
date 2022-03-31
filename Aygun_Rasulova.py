# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#Sual1
def emel_sayi(misal):
    say=0
    for i in misal[1:]:
        if i in ['+', '-', '*']:
            say+=1
    return say

misal1='-1+2*3+a'
misal2='+5-2+4-m/n*2:4'

print(emel_sayi(misal1))
print(emel_sayi(misal2))
################################################################

#Sual2
n=int(input('Ededi daxil edin:'))

while True:
    cem=0
    while n:
        cem+=(n%10)**2
        n//=10

    if cem==1:
        print('Bu ədəd xoşbəxt ədəddir.')
        break
    elif cem==4:
        print('Bu ədəd xoşbəxt ədəd deyil.')
        break
    else:
        n=cem  
    
##################################################################   
#Sual 3
kitablar=[ ('978', 'H. Cavid', 'İblis', 'qanun'),
          ('950', 'M. Ə. Sabir', 'Hophopnamə', 'kitab-yurdu'), 
          ('978', 'H. Cavid', 'Seyavüş', 'Şərq-Qərb')] 


def search(key=None, value=None):
    global kitablar
    keys=['kod', 'yazar', 'eser', 'neshriyyat'] 
    if not key and not value:
        print(kitablar)           
    
    else:
        for tpl in kitablar:
            if tpl[keys.index(key)]==value:
                print(tpl)
                

            
search(key='yazar', value='H. Cavid')

search('kod', '950')
                    
#################################################################
#Sual 4
def funk(l, eded):
    for i in range(len(l)):
        for j in range(len(l)):
            if i!=j:
                if l[i]+l[j]==eded:
                    return [i, j]
            else:
                continue
    else:
        return -1
        
        
l=[2, 8, 8, 12, 15]
eded=16

print(funk(l, eded))
#########################################################################

#Sual 5
siyahi=[1, 2, 3, -1, -2, 0, -1]

result=[]

for eded in siyahi:
    if eded!=0:
        say=siyahi.count(eded)+siyahi.count(eded*(-1))
    else:
        say=siyahi.count(0)
    cvb=(abs(eded), say)
    
    if cvb not in result:
       result.append(cvb)
    
    
print(result)



######### git ucun deyisiklik

    


    
    
    
    
    
