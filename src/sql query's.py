import getData as gD
import time

customerID = 1
startTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
endTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
device = 'x'
actualCalories = 10

getWeight = gD.getDataWhere('weight', 'customerInfo', customerID)

gD.insertData('customerPerformanceInfo (customerID, startSession, endSession, fitnessDevice, burntCalories)',
              '{}, \'{}\', \'{}\', \'{}\', {}'.format(customerID, startTime, endTime, device, actualCalories))

