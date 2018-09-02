def string_splosion(str):
    string = ""
   
    for i in range(len(str)):
        string += str[:i+1]
    
    return string