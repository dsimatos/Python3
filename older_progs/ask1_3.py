secs = input("Give a number of seconds : ")
sec = secs%60
mins = ((secs - sec)//60)%60
hr = (secs - sec - mins*60)//3600
print '{:0}:{:02}:{:02}'.format(hr, mins, sec)
