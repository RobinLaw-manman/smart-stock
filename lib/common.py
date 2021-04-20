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
    pro = get_tushare_pro_api()
    data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
    print(type(data))
    symbols = data['symbol'].values
    # symbols = data.values[1] 二维数组取股票代码应该是 data.values[i][1] i为有多少行
    # print(data.values[1])
    return symbols


def get_tushare_pro_api():
    ts.set_token(get_tushare_token())
    pro = ts.pro_api()
    return pro


def get_stock_daily(stock_codes_str, start_date, end_date):
    pro = get_tushare_pro_api()
    df = pro.daily(ts_code=stock_codes_str, start_date=start_date, end_date=end_date)
    pd.DataFrame(df)


def show_symbols():
    symbols = get_stock_code()
    for i in symbols:
        print(i)


# show_symbols()
# print(get_stock_code())
if __name__ == '__main__':
    print(get_tushare_token())
    show_symbols()
