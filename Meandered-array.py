  
def meanderingArray(unsorted):
      #sort array in ascending order
      ascendingArray = sorted(unsorted)
      #create empty list to sort items in meandering order
      meanderedArray = []
  
      #Giving that the array is not empty or with only one element, 
      while len(ascendingArray) > 1:
      #take the biggest and smallest from the ascendingArray list and add the to the    meandering list
       meanderedArray += [ascendingArray[-1], ascendingArray[0]]
      #remove the biggest and smallest from the ascendingArray list to allow for new biggest and new smallest
       ascendingArray = ascendingArray[1:-1]
  
      #add whatever is left of ascendingArray list to the meanderedArray (i.e. empty or 1 item)
      meanderedArray += ascendingArray
  
      return meanderedArray
