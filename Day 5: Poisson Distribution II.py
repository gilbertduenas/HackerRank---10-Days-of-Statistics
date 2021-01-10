# https://www.hackerrank.com/challenges/s10-poisson-distribution-2/problem

# This is a discrete probability distribution that expresses the probability of a given number of events occurring 
# in a fixed interval of time or space if these events occur with a known constant mean rate and independently of the time since the last event.
# The Poisson distribution can also be used for the number of events in other specified intervals such as distance, area or volume.

# For instance, a call center receives an average of 180 calls per hour, 24 hours a day. 
# The calls are independent; receiving one does not change the probability of when the next one will arrive. 
# The number of calls received during any minute has a Poisson probability distribution: the most likely number is 3, 
# but 2 and 4 are also likely and there is a small probability of it being as low as zero and a very small probability it could be 10. 
# Another example is the number of decay events that occur from a radioactive source in a given observation period.

averageX, averageY = [float(num) for num in input().split(" ")]

CostX = 160 + 40*(averageX + averageX**2)
CostY = 128 + 40*(averageY + averageY**2)

print(round(CostX, 3))
print(round(CostY, 3))
