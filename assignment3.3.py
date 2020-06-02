score =input("enter a score:")
s = float(score)
if 0.0 <= s <= 1.0:
    if s >= 0.9:
        result = 'A'
        print(result)
    elif 0.8 <= s < 0.9:
        result = 'B'
        print(result)
    elif 0.7 <= s < 0.8:
        result = 'C'
        print(result)
    elif 0.6 <= s < 0.7:
        result ='D'
        print(result)
    else:
        result = 'F'
        print(result)
else:
    print ('Error: score out of range')
