

def price_finder(filename):
    f = open(filename, 'r')
    list_of_vals = []
    #Create a list of numbers from the file
    for line in f:
        list_of_vals.append(int(line))
    #Set the max profit to be the profit from 1 - 0
    maxprof = list_of_vals[1] - list_of_vals[0]
    #Set the min price to be the first price
    minval = list_of_vals[0]
    minval_idx = 0
    retmin_idx = 0
    val_idx = 0
    for i in range(0, len(list_of_vals)):
        val = list_of_vals[i]
    	prof = val - minval
        #Update maxprof and likewise the buy/sell indices
        if prof > maxprof:
            maxprof = prof
            currsell = val
            currbuy = minval
            retmin_idx = minval_idx
            val_idx = i
        #Update minval index
        if val < minval:
            minval = val
            minval_idx = i
    buy_str = "" + str(retmin_idx) + " BUY" 
    sell_str = "" + str(val_idx) + " SELL" 
    print buy_str
    print sell_str
    return maxprof


price_finder('numbers.txt')