import time


calorie = [x for x in range(10**7)]
start_time = time.time_ns()
# Write program #1
calorie = sorted(calorie, reverse=True)
# End of program #1
end_time = time.time_ns()


start_time2 = time.time_ns()
# Write program #2
calorie.sort()
calorie.reverse()
# End of program #2
end_time2 = time.time_ns()


time_lapsed = end_time - start_time
print(time_lapsed)
time_lapsed = end_time2 - start_time2
print(time_lapsed)
