def threeNumberSum(array, targetSum):
    for i in range(len(array)-1):
		first=array[i]
		for j in range(i+1,len(array)):
			second=array[j]
			for k in range(i+2,len(array)):
				third=array[k]
				if(third+second+first==targetSum):
					return[first,second,third]
	return[]			
