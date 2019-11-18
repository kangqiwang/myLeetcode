def power(x, y): 
  
    if(y == 0): return 1
    temp = power(x, int(y / 2))
    print("TEMP:    ",temp)
    if (y % 2 == 0): 
        print("*********        ",y)
        print("*********        ",temp)
        return temp * temp 
    else: 
        print("&&&&&&&&&&       ",y)
        print("&&&&&&&&&&       ",x)
        print("&&&&&&&&&&       ",temp)
        if(y > 0): return x * temp * temp 
        else: return (temp * temp) / x 
      
# Driver Code 
x, y = 2, -10
print('%.6f' %(power(x, y))) 
