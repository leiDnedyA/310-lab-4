def max_profit(prices):
    curr_max = 0
    i, j = 0, 1
    while j < len(prices):
        if prices[i] < prices[j]:
            curr_price = prices[j] - prices[i]
            curr_max = max(curr_price, curr_max)
        else:
            i += 1
        j += 1
    return curr_max

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print("Maximum Profit:", max_profit(prices))
