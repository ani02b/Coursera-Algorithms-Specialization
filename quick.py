def partition_1(a,l,r):

    #Pivot: Always the 1st element of the array
    p = a[l]
    
    i = l+1
    j = l+1
    while j <= r:
        if a[j] <= p:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            i+=1
            j+=1
        else:
            j+=1
    temp = a[l]
    a[l] = a[i-1]
    a[i-1] = temp
    
    return i-1
    
def partition_2(a,l,r):
    
    #Pivot: Use the last element of the array. Swap with the first element.
    temp = a[l]
    a[l] = a[r]
    a[r] = temp
    
    p = a[l]
    i = l+1
    j = l+1
    while j <= r:
        if a[j] <= p:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            i+=1
            j+=1
        else:
            j+=1
    temp = a[l]
    a[l] = a[i-1]
    a[i-1] = temp
    
    return i-1
 
def partition_3(a,l,r):
    
    #Pivot: Use median of three. The median of first, last and middle element. Swap with the first element
    mid = l+(r-l)//2
    if a[l] > a[mid]:
        if a[l]< a[r]:
            median = a[l]
        elif a[mid] > a[r]:
            median = a[mid]
        else:
            median = a[r]
    else:
        if a[l] > a[r]:
            median = a[l]
        elif a[mid] < a[r]:
            median = a[mid]
        else:
            median = a[r]

    if median == a[r]:
        temp = a[r]
        a[r] = a[l]
        a[l] = temp
    elif median == a[mid]:
        temp = a[mid]
        a[mid] = a[l]
        a[l] = temp
    
    p = a[l]
    
    i = l+1
    j = l+1
    while j <= r:
        if a[j] <= p:
            temp = a[j]
            a[j] = a[i]
            a[i] = temp
            i+=1
            j+=1
        else:
            j+=1
    temp = a[l]
    a[l] = a[i-1]
    a[i-1] = temp
    
    return i-1

def QS_count(a,l,r, pivot = ['first', 'last', 'median']):
    count = 0

    if r-l+1 <=1:
        return 0
    
    if pivot =='first':
        p = partition_1(a,l,r)
    elif pivot =='last':
        p = partition_2(a,l,r)
    else:
        p = partition_3(a,l,r)
        
    num= r-l
    
    left = QS_count(a,l,p-1,pivot)
    right = QS_count(a,p+1,r,pivot)
    count= left+right+num
    
    return count
 
if __name__ == '__main__':
    with open('quick_text.txt') as f:
        a = [int(x) for x in f]
    # 1. 'first' to use the 1st element as pivot.
    # 2. 'last' to use the last element as pivot
    # 3. 'median' to use the median of three as pivot(first, last and middle elements).
    c=QS_count(a,0,9999,'first')
    print(c)
