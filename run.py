import service.yahoo_stock as ys
import numpy as np

for x in ys.save_data(ys.prey()):
    print(x)
