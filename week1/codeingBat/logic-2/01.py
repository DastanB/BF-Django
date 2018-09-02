def make_bricks(small, big, goal):
	maxBig = goal/5;
	if(maxBig <= big):
		goal -= maxBig*5;
	else:
		goal -= big*5;
	if(goal <= small):
		return True
	return False