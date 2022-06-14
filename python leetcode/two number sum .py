def twoNumberSum(array, targetSum):
    for i in range(len(array)-1):
		first=array[i]
		for j in range(i+1,len(array)):
			sec=array[j]
			if(first+sec==targetSum):
				return[first,sec]
	return[]	
