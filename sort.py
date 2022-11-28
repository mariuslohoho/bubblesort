def sort(lists) :
    
    length = len(lists) - 1
    sort2 = False

    if isinstance(lists, list) :
        while not sort2:
            
            
            
            sort2 = True

            for i in range(0, length):
                if lists[i] > lists[i + 1]:
                    sort2 = False 
                    lists[i],lists[i + 1] = lists[i + 1],lists[i]
                    
                               

        
        if sort2 == True:
            return(lists)
