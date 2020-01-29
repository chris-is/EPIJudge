from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    # TODO - you fill in here.
    '''
    The main thing to remember here is that you can't short your stock - your buy always needs to happen before a sell.
    So then you realize...the maximum profit that can be made by selling on a specific day is determined by the minimum
    of the stock prices over the previous days. Therefore, keep track of your max profit encountered so far,
    but ALWAYS update your lowestBuy point to the lower price to maximize your profit when iterating through
    the following days' stock prices.
    '''
    lowestBuy = 0
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < prices[lowestBuy]:
            lowestBuy = i
        if prices[i] - prices[lowestBuy] > maxProfit:
            maxProfit = prices[i] - prices[lowestBuy]
        # else:
        #     continue
    return maxProfit

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("buy_and_sell_stock.py",
                                       "buy_and_sell_stock.tsv",
                                       buy_and_sell_stock_once))
