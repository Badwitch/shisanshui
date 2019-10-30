import time
import json
import dd as shisanshui
import sys

shisanshui.login()#登录

try:

    timestart = time.perf_counter
    shisanshui.init_start()
    shisanshui.read_opengame()
    shisanshui.dfs_1(1, 1)
    shisanshui.submit_ans = shisanshui.printf_ans()
    shisanshui.submitgame(shisanshui.submit_ans)  #提交牌局
    shisanshui.ranking()#显示排行榜
    timeend = time.perf_counter
    #print(str(timeend - timestart))
    shisanshui.init_end()
except IndexError:
   time().sleep(5)
