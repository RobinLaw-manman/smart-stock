import os
import tushare as ts
import pandas as pd
import lib.config as cf

"""
conda info --envs or conda env list
conda activate your_env_name
conda deactivate
conda create --name new_env_name --clone old_env_name
conda remove --name your_env_name --all

git branch -m master main
git fetch origin
git branch -u origin/main main
git remote set-head origin -a

"""


def get_tushare_token():
    # tushare_token = os.environ.get('TUSHARE_TOKEN')
    tushare_token = cf.get_tushare_token()
    if tushare_token is not None:
        return tushare_token
    else:
        return ""


print(os.environ["PYTHON_CONFIG_PATH"])
# print(os.environ["PYTHONHOME"])

def get_stock_code():
    ts.set_token(get_tushare_token())
    pro = ts.pro_api()
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(type(data))
    symbols = data['symbol'].values
    # symbols = data.values[1]
    # print(data.values[1])
    return symbols


def show_symbols():
    symbols = get_stock_code()
    for i in symbols:
        print(i)


# show_symbols()
# print(get_stock_code())
if __name__ == '__main__':
    print(get_tushare_token())
    show_symbols()