
#import openpyxl
import pandas as pd


df = pd.read_excel('exel/a1.xlsx')

wa = df[df["店舗名"] == '和食 清風']
wb = df[df["店舗名"] == 'Bar Seifu']
wc = df[df["店舗名"] == 'オステリアSeifu']

with pd.ExcelWriter('exel/aaa.xlsx') as writer:
    wa.to_excel(writer, sheet_name='和食 清風')
    wb.to_excel(writer, sheet_name='Bar Seifu')
    wc.to_excel(writer, sheet_name='オステリアSeifu')