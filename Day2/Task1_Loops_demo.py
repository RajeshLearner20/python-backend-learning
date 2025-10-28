even_count = 0
odd_count = 0
for i in range(1,51):
   
    if i%2==0:
        print(i ,end=' ')
        even_count += 1
      
    
    else:
        print(i ,end=' ')
        odd_count += 1
print('\nTotal Even Numbers:',even_count)
print('Total Odd Numbers:',odd_count)