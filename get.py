import akshare as ak
import time
from IPython.display import clear_output as clear
i=0
while True:
    i=i+1
    futures_zh_spot_df = ak.futures_zh_spot(symbol='MA2309', market="CF", adjust='0').iloc[0]['current_price']
    print(futures_zh_spot_df)

    futures_zh_spot_df = ak.futures_zh_spot(symbol='FG2309', market="CF", adjust='0').iloc[0]['current_price']
    print(futures_zh_spot_df)
    print("-----------")
    time.sleep(10)
    if i%20==0:
        clear()
