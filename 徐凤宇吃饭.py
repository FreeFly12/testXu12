import requests
import threading
import xlwt
requests.packages.urllib3.disable_warnings()
book = xlwt.Workbook(encoding='utf-8',style_compression=0)
sheet = book.add_sheet('问存活情况',cell_overwrite_ok=True)
sheet.write(0,0,"域名")
sheet.write(0,1,"状态码")

urlList = open("崔魏毛.txt").readlines()
num = 0

for i in urlList:
    i = i.strip("\n")
    try:
        resp = requests.get(i,timeout = 10,verify = False)
        sheet.write(num, 0, i)
        sheet.write(num, 1, resp.status_code)
    except:
        sheet.write(num, 0, i)
        sheet.write(num, 1, "错误")
    num+=1
    print(num)


savepath = 'C:/Users/98017/Desktop/untitled/excel表格.xls'
book.save(savepath)


