import sys
import requests
import os
import re
from hashlib import md5
from past.builtins import raw_input

#读取账号密码
def dq(path):
    wj=os.path.exists(path)
    if wj==True:
        with open(path,mode="rt",encoding="utf-8") as f1:
            txt01=f1.readline()
            txt02=f1.readline()
            txt03=jm_mm(txt02.strip())
            txt04=f1.readline()
            if len(txt04)==0|txt04.isspace()==True:
                txt04=3
            return txt01.strip(),txt03,int(txt04)
    else:
        print("文件不存在，请在本程序下创建data.txt文件，并写好账号密码")
        raw_input("输入回车以结束程序运行")
        sys.exit()

def jm_mm(mm):   #加密密码
    new_md5=md5()
    new_md5.update(mm.encode(encoding='utf-8'))
    mm01=new_md5.hexdigest()
    mm02=mm01[0:5]
    mm03=mm01[5:9]
    mm04=mm01[9:-2]
    mmmax=(mm02+"a"+mm03+"b"+mm04)
    return mmmax

session01=requests.session()

def dl(uname,pd_mm):       #登录获取cookie  账号，密码
    url="http://xggl.hnqczy.com/website/login"
    headers={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"}
    data={
    "uname":uname,
    "pd_mm":pd_mm
    }
    rp=session01.post(url=url, headers=headers, data=data)
    rp01=rp.text
    ts=re.search("\d{13}",rp01)
    return ts.group()

def dk(ts,zs):        #自动打卡  时间,针数
    ym=["未接种","已接种未完成","已接种已完成","已接种加强针","未接种加强针"]
    url="http://xggl.hnqczy.com/content/student/temp/zzdk?_t_s_={}".format(ts)
    headers ={"User-Agent":"Mozilla/5.0 (Linux; Android 6.0.1; Moto G (4)) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Mobile Safari/537.36"
              }
    data={"dkdz":"湖南省株洲市天元区天台路60",
        "dkdzZb":"113.134,27.8275",
        "dkly":"baidu",
        "dkd":"湖南省株洲市",
        "jzdValue":"430000,430200,430202",
        "jzdSheng.dm":"430000",
        "jzdShi.dm":"430200",
        "jzdXian.dm":"430202",
        "jzdDz":"湖南汽车工程职业学院三栋南623号",
        "jzdDz2":"三栋南623号",
        "lxdh":"19973982412",
        "sfzx":"1",
        "sfzx1":"在校",
        "twM.dm":"01",
        "tw1":"[35.0~37.2]正常",
        "tw1M.dm":"",
        "tw11":"",
        "tw2M.dm":"",
        "tw12":"",
        "tw3M.dm":"",
        "tw13":"",
        "yczk.dm":"01",
        "yczk1":"无症状",
        "fbrq":"",
        "jzInd":"0",
        "jzYy":"",
        "zdjg":"",
        "fxrq":"",
        "brStzk.dm":"01",
        "brStzk1":"身体健康、无异常",
        "brJccry.dm":"01",
        "brJccry1":"未接触传染源",
        "jrStzk.dm":"01",
        "jrStzk1":"身体健康、无异常",
        "jrJccry.dm":"01",
        "jrJccry1":"未接触传染源",
        "jkm":"1",
        "jkm1":"绿色",
        "xcm":"1",
        "xcm1":"绿色",
        "xgym":str(zs-1),
        "xgym1":ym[zs-1],
        "hsjc":"1",
        "hsjc1":"是",
        "bz":"",
        "operationType":"Create",
        "dm":""
        }

    response = session01.post(url=url, headers=headers, data=data).text
    print(response)


try:
    x1, x2, x3 = dq("data.txt")  # 读取账号密码 针数
    ts01=dl(x1,x2)         #登录账号
except Exception:
    print("账号或密码错误")
    raw_input("输入回车以结束程序运行")  # 结束程序运行
    sys.exit()
else:
    try:
        dk(ts01,x3)     #打卡 时间，针数
    except Exception:
        print("打卡失败")
        raw_input("输入回车以结束程序运行")  # 结束程序运行
        sys.exit()
    else:
        print("运行成功")
        raw_input("输入回车以结束程序运行")   #结束程序运行
        sys.exit()
