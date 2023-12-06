#Phython code to demonstrate difference
#in results of stdev() and variance()

#impoting Statistics module
import statistics

#creating a simple data-set
#sesuaikan data yang diinputkan dengan kasus 1 dan 2
sample = [70,80,87,90,69,90,60,70,78,88]

#Printing standard deviation
#xbar is set to default value of 1
print("Standard Deviation of the sample is % s " 
      % (statistics.stdev(sample)))

#variance is approximately the
#squared result of what stdev is
print("Variance of the sample is % s " 
      %(statistics.variance(sample)))