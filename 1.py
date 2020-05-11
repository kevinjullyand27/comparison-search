import time
def binarySearch (arr, l, r, x):
    if r >= l:
        mid = l + (r - l)
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x) 
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1

def search(arr, n, x): 

	for i in range (0, n): 
		if (arr[i] == x): 
			return i; 
	return -1; 

print('data array')
print('[ 2, 3, 4, 10, 40 ]')
arr = [ 2, 3, 4, 10, 40 ] 
x = input('data yang dicari:')
start= time.time()
result = binarySearch(arr, 0, len(arr)-1, int(x)) 
end= time.time()

if result != -1: 
	print(x+" ada di array ke "+str(result)) 
else: 
	print('data yang dicari tidak ditemukan') 
print('data ditemukan dalam '+str(float(end-start))+' detik')
start= time.time()
result = search(arr, len(arr), int(x))
end= time.time()
if result != -1: 
	print(x+" ada di array ke "+str(result)) 
else: 
	print('data yang dicari tidak ditemukan') 
print('data ditemukan dalam '+str(end-start)+' detik')
