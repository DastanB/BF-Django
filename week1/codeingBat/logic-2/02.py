def lone_sum(a, b, c):
  
  if(a == b):
    	if(a == c):
    	  return 0;
    	return c;
  	
  if(a == c):
    	return b; 
  
  if(b == c):
    	return a;
  
  return (a + b + c)
