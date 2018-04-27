Time = int(input())

Hours = int(Time/3600)

Time = Time - Hours*3600

Minutes = int(Time/60)

Time = Time - Minutes*60

Seconds = Time

print(str(Hours)+":"+str(Minutes)+":"+str(Seconds))