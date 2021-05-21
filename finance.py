import matplotlib.pyplot as plt
import numpy as np
import quandl


def graph_data(stock):
    quandl.ApiConfig.api_key = "izafTQ-vdipJzAZ2uUnz"
    # fig = plt.figure()
    # ax1 = plt.subplot2grid((1, 1), (0, 0))

    tracked_stock = quandl.get(stock)

    tracked_stock.plot(y="Open", figsize=(12, 11))

    # x = [1, 2, 3, 4, 5, 6, 8]
    # y = [1, 55, 12, 12, 19, 0, 8]
    # ax1.plot(x, y)
    # for label in ax1.xaxis.get_ticklabels():
    #     label.set_rotation(45)

    plt.xlabel("Date", fontsize=16)
    plt.ylabel("Price", fontsize=18)
    plt.title(stock + " open prices")
    plt.show()


graph_data("WIKI/TSLA")
