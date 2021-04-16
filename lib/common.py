import os
import tushare as ts
import pandas as pd

"""
conda info --envs or conda env list
conda activate your_env_name
conda deactivate
conda create --name new_env_name --clone old_env_name
conda remove --name your_env_name --all
"""


def get_tushare_token():
    # tushare_token = os.environ.get('TUSHARE_TOKEN')
    tushare_token = '27160235153db4e7a6cf445eb4cc43db0e91df057db5c056f5f57e11'
    if tushare_token is not None:
        return tushare_token
    else:
        return ""


print(get_tushare_token())


# print(os.environ["PYTHONPATH"])
# print(os.environ["PYTHONHOME"])

def get_stock_code():
    ts.set_token(get_tushare_token())
    pro = ts.pro_api()
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(type(data))
    symbols = data['symbol'].values
    return symbols


def show_symbols():
    symbols = get_stock_code()
    for i in symbols:
        print(i)


show_symbols()
# print(get_stock_code())
