count = 0
hour = 2
mini =0
while count < 25:
	print("{:02}.{:02}-{:02}.{:02}".format(hour+ mini//60, mini%60, hour+ (mini+20)//60, (mini+20)%60))
	count +=1
	mini += 20
