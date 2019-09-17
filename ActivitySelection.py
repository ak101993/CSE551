def maxTotalActivity(start_time,finish_time):
    n=len(start_time)
    # sorted_list=finish_time.sort()
    num=1
    print(start_time[0],finish_time[0])
    current_finish_time=finish_time[0]
    for i in range(n-1):
        if current_finish_time<start_time[i+1]:
            print(start_time[i+1],finish_time[i+1])
            current_finish_time=finish_time[i+1]
            num=num+1
    print(num)

start_time = [1 , 3 , 0 , 5 , 8 , 5] 
finish_time = [2 , 4 , 6 , 7 , 9 , 9] 
maxTotalActivity(start_time ,finish_time) 

