def make_chocolate(small, big, goal):
    maxBig = goal/5;
    if maxBig <= big:
    	goal -= maxBig*5;
    else:
    	goal -= big*5;
    if goal <= small:
    	return goal;
    return -1;