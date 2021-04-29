import os
import tushare as ts
import pandas as pd
import lib.config as cf
import lib.date_util as date_util

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
    ts_codes = data['ts_code'].values
    # symbols = data.values[1] 二维数组取股票代码应该是 data.values[i][1] i为有多少行
    # print(data.values[1])
    return ts_codes


def get_tushare_pro_api():
    ts.set_token(get_tushare_token())
    pro = ts.pro_api()
    return pro


def get_stock_daily(stock_codes_str, start_date, end_date) -> pd.DataFrame:
    pro = get_tushare_pro_api()
    df: pd.DataFrame = pro.daily(ts_code=stock_codes_str, start_date=start_date, end_date=end_date)
    return df


def show_ts_codes():
    symbols = get_stock_code()
    for i in symbols:
        print(i)


def show_daily():
    symbols = get_stock_code()
    start_date = date_util.get_date_before(2)
    end_date = date_util.get_current_date_str()
    df: pd.DataFrame = get_stock_daily('600276.SH', start_date, end_date)
    print(df['vol'])
    for symbol in symbols:
        pass


# show_symbols()
# print(get_stock_code())
if __name__ == '__main__':
    print(get_tushare_token())
    show_ts_codes()
    show_daily()
