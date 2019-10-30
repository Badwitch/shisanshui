import requests
import json
class node:
    flower=0
    num=0
    def __init__(self,f,n):
        self.flower=f
        self.num=n

poker_1,poker_2,poker_3=[],[],[]    # 扑克牌分堆
ans_1,ans_2,ans_3=[],[],[]  #暂时寄存排列答案
temp_1,temp_2,temp_3=[],[],[]   #存放完整排列答案
end_1,end_2,end_3=[],[],[]   #最终答案
s1,s2,s3=[],[],[]   #标记
tempp1,tempp2,tempp3=[],[],[]
pddun=[]
hua,number={},{}
submit_ans=[]

for i in range(0,20):
    poker_1.append(node(0,0))
    poker_2.append(node(0, 0))
    poker_3.append(node(0, 0))
    ans_1.append(node(0, 0))
    ans_2.append(node(0, 0))
    ans_3.append(node(0, 0))
    temp_1.append(node(0, 0))
    temp_2.append(node(0, 0))
    temp_3.append(node(0, 0))
    end_1.append(node(0,0))
    end_2.append(node(0, 0))
    end_3.append(node(0, 0))
    s1.append(0)
    s2.append(0)
    s3.append(0)

for i in range(0,2+1):
    tempp1.append(node(0,0))
for i in range(0,4+1):
    tempp2.append(node(0,0))
for i in range(0,4+1):
    tempp3.append(node(0,0))

cnt,r1,r2,r3,end_ans,score=0,0,0,0,0,0 # 计数器
cnt,r1,r2,r3=0,5,5,3
end_ans ,score= 0.0,0.0
e1, e2, e3=0,0,0
a1, a2, a3=0,0,0
token,user_id,use={},{},{}

hua,number={},{}
for i in range(0,15+1):
    hua[i]=0
    number[i]=0#桶排初始化

def init_cnt():
    for i in range(0, 15+1):
        hua[i] = 0
        number[i] = 0  # 桶排初始化

def takenum(x):
    return x.num

def shunzi3(start) :
    for i in range(start,start+2+1):
        if number[i] < 1:
            return 0
    return 1

def shunzi5(start):
    for i in range(start,start+4+1):
        if number[i] < 1:
            return 0
    return 1

def standof() :
    for i in range(1,3+1):# 前墩
        end_3[i] = ans_3[i]
    for i in range(1,5+1):#中墩
        end_2[i] = ans_2[i]
    for i in range(1,5+1): #后墩
        end_1[i] = ans_1[i]

def tempof() :
    for i in range(1,3+1):  #前墩
        ans_3[i] = temp_3[i]
    for i in range(1, 5 + 1):  # 中墩
        ans_2[i] = temp_2[i]
    for i in range(1, 5 + 1):  # 后墩
        ans_1[i] = temp_1[i]


def first():#前墩
    global score
    init_cnt()
    x = 1

    for i in range(0,2+1):
        tempp1[i]=ans_3[i+1]
    tempp1.sort(key=takenum) #  前墩牌组有序化

    for i in range(1,3+1):
        ans_3[i]=tempp1[i-1]


    for i in range(1,3+1):
        hua[ans_3[i].flower] +=1
        number[ans_3[i].num]+=1
    x = 1
    for i in range(1,4+1):
        if hua[i] == 3:
            if shunzi3(ans_3[1].num) == 1:
                k=(9.0+0.9 / 11.0 * (ans_3[1].num - 1))
                score += k
                return k # 3张同花顺
    x = 1
    for i in range(1,4+1):
        if hua[i] == 3:
            k=(6.0 +0.9/(1300+130+13)*((ans_3[3].num-1)*100+(ans_3[2].num-1)*10+(ans_3[1].num-1))*1.0 )
            score += k
            return k #3张同花
    x = 1
    if shunzi3(ans_3[1].num) == 1:
        k=(5.0  + 0.9/11.0*(ans_3[1].num-1)*1.0)
        score += k
        return k #3张顺子
    x = 1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 3:
            k=(4.0+0.9/13.0*(ans_3[1].num - 1)*1.0)
            score += k
            return k#三条
    x = 1
    for i in range(3,0,-1):
        if number[ans_3[i].num] == 1:
            x = ans_3[i].num
        if number[ans_3[i].num] == 2:
            k=(1.0 + 0.9/(130+13)*((ans_3[i].num - 1)*10+x-1)*1.0)
            score += k
            return k#单对
    x = 1
    k=0.9 / (1300.0 + 130.0 + 13.0)*((ans_3[3].num - 1) * 100 + (ans_3[2].num - 1) * 10 + (ans_3[1].num - 1))
    score += k
    return k #散牌

def second():
    global score
    init_cnt()

    for i in range(0, 4 + 1):
        tempp2[i] = ans_2[i + 1]

    tempp2.sort(key=takenum)  # 中墩牌组有序化
    for i in range(1, 5 + 1):
        ans_2[i] = tempp2[i - 1]

    x = 1
    for i in range(1,5+1):
        hua[ans_2[i].flower] +=1
        number[ans_2[i].num]+=1

    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            if shunzi5(ans_2[1].num) == 1:
                k= (9.0 + 0.9 / 9 * (ans_2[1].num - 1)) * 1.0
                score += k# 14 13 12 11 10
                return k # 同花顺

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 4:
            k=(8.0+ 0.9/(130+13)*((ans_2[i].num - 1)*10))*1.0
            score += k
            return k#炸弹

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 2:
                    k=(7.0 + 0.9 / (130 + 13)*((x - 1) * 10 + ans_2[j].num - 1))*1.0
                    score += k
                    return k#葫芦
    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            k=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((ans_2[5].num-1)*10000+(ans_2[4].num - 1)*1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + (ans_2[1].num - 1)))*1.0
            score +=k
            return k#同花

    x = 1
    if shunzi5(ans_2[1].num) == 1 :
        k=(5.0 + 0.9/9*(ans_2[1].num - 1)*1.0)
        score += k
        return k#5张顺子

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 3:
            x = ans_2[i].num
            for j in range(5,0,-1):
                if number[ans_2[j].num] == 1:
                    k=(4.0 + 0.9 / (1300+130+13) * ((x-1) * 100))
                    score += k
                    return k# 三条

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 and abs(ans_2[i].num - ans_2[j].num) == 1 :
                    k=(3.0+ 0.9 / 10 * (ans_2[j].num-1-1)) * 1.0
                    score += k
                    return k# 连对2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_2[i].num != ans_2[j].num) and number[ans_2[j].num] == 2 :
                    k=(2.0 +0.9 / (130+13) * ((ans_2[i].num - 1) * 10+ans_2[j].num-1)) * 1.0
                    score += k
                    return k # 普通2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_2[i].num] == 1:
            x = ans_2[i].num
        if number[ans_2[i].num] == 2:
            k=(1.0+0.9/(130+13)*((ans_2[i].num-1)*10+x-1))*1.0
            score += k
            return k #单对+3张散

    k= (0.9 / (130000 + 13000 + 1300 + 130 + 13)*((ans_2[5].num - 1) * 10000 + (ans_2[4].num - 1) * 1000 + (ans_2[3].num - 1) * 100 + (ans_2[2].num - 1) * 10 + ans_2[1].num - 1))*1.0
    score +=k
    return k

def third():
    global score
    init_cnt()

    for i in range(0, 4 + 1):
        tempp3[i] = ans_1[i + 1]

    tempp3.sort(key=takenum)  # 后墩牌组有序化
    for i in range(1, 5 + 1):
        ans_1[i] = tempp3[i - 1]

    x = 1
    for i in range(1,5+1):
        hua[ans_1[i].flower] +=1
        number[ans_1[i].num]+=1

    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            if shunzi5(ans_1[1].num) == 1:
                k=(9.0 + 0.9 / 9 * (ans_1[1].num - 1)) * 1.0 # 14 13 12 11 10
                score += k
                return k # 同花顺

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 4:
            k=(8.0+ 0.9/(130+13)*((ans_1[i].num - 1)*10))*1.0
            score += k
            return k#炸弹

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 2:
                    k=(7.0 + 0.9 / (130 + 13)*((x - 1) * 10 + ans_1[j].num - 1))*1.0
                    score += k
                    return k#葫芦
    x = 1
    for i in range(1,4+1):
        if hua[i] == 5:
            k=(6.0 + 0.9 / (130000 + 13000 + 1300+130+13)*((ans_1[5].num-1)*10000+(ans_1[4].num - 1)*1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + (ans_1[1].num - 1)))*1.0
            score +=k
            return k #同花

    x = 1
    if shunzi5(ans_1[1].num) == 1 :
        k=(5.0 + 0.9/9*(ans_1[1].num - 1)*1.0)
        score += k
        return k#5张顺子

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 3:
            x = ans_1[i].num
            for j in range(5,0,-1):
                if number[ans_1[j].num] == 1:
                    k=(4.0 + 0.9 / (1300+130+13) * ((x-1) * 100))
                    score += k
                    return k# 三条

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 and abs(ans_1[i].num - ans_1[j].num) == 1 :
                    k= (3.0+ 0.9 / 10 * (ans_1[j].num-1-1)) * 1.0
                    score +=k
                    return k # 连对2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 2:
            for j in range(5,0,-1):
                if (ans_1[i].num != ans_1[j].num) and number[ans_1[j].num] == 2 :
                    k=(2.0 +0.9 / (130+13) * ((ans_1[i].num - 1) * 10+ans_1[j].num-1)) * 1.0
                    score += k
                    return k # 普通2对

    x = 1
    for i in range(5,0,-1):
        if number[ans_1[i].num] == 1:
            x = ans_1[i].num
        if number[ans_1[i].num] == 2:
            k=(1.0+0.9/(130+13)*((ans_1[i].num-1)*10+x-1))*1.0
            score += k
            return k #单对+3张散

    k=(0.9 / (130000 + 13000 + 1300 + 130 + 13)*((ans_1[5].num - 1) * 10000 + (ans_1[4].num - 1) * 1000 + (ans_1[3].num - 1) * 100 + (ans_1[2].num - 1) * 10 + ans_1[1].num - 1))*1.0
    score += k
    return  k


def tempof1() :
    for i in range(1,4): #前墩
        ans_3[i] = temp_3[i]
    for i in range(1,6): #中墩
        ans_2[i] = temp_2[i]
    for i in range(1,6): #后墩
        ans_1[i] = temp_1[i]

def contrast_ans() :


    global score,end_ans,cnt
    global e1, e2, e3
    global a1, a2, a3
    tempof()
    score = 0.0
    k1 = first()
    e1 = score
    k2 = second()
    e2 = score - e1
    k3 = third()
    e3 = score - (e1 + e2)
    if k1 > k2 or k2 > k3 or k1 > k3 :
        score = 0
    if score>end_ans :
        end_ans = score
        a1 = e1; a2 = e2; a3 = e3
        standof()
    cnt+=1


def init_2():
    index = 0
    for i in range(1,8+1):
        if s2[i] == 0 :
            index+=1
            temp_3[index] = poker_2[i]

def dfs_2(d,index_2) :#/*枚举组合*/
    for i in range(d,9):
        temp_2[index_2] = poker_2[i]
        s2[i] = 1
        if index_2 == r2 :
            init_2()
            contrast_ans()
        else :
            dfs_2(i + 1, index_2 + 1)
        s2[i] = 0

def init_1() :
    index = 0
    for i in range(1,14):
        if s1[i] == 0:
            index+=1
            poker_2[index] = poker_1[i]

def dfs_1(d, index_1): #/ * 枚举组合 * /
    for i in range(d,13+1):
        s1[i] = 1
        temp_1[index_1] = poker_1[i]
        if index_1 == r1 :
            init_1()
            dfs_2(1, 1)
        else:
            dfs_1(i + 1, index_1 + 1)
        s1[i] = 0


def number_to_hua(x):
    if x == 1:
        return "&"
    if x == 2:
        return "$"
    if x == 3:
        return "#"
    if x == 4:
        return "*"

def hua_to_number(x):
    if x == "&":
        return 1
    if x == "$":
        return 2
    if x == "#":
        return 3
    if x == "*":
        return 4

def change(x):
    if x==10:
        return "10"
    if x==11:
        return "J"
    if x==12:
        return "Q"
    if x==13:
        return "K"
    if x==14:
        return "A"
    return str(x)



def login():
    """
    包括登入，注册，验证
    """
    global token, user_id
    url = "http://api.revth.com/auth/login"
    print("请输入用户名与密码：")
    username = input()
    password = input()
    headers = {"Content-Type": "application/json"}
    formdata = {"username": username, "password": password}
    response = requests.post(url, data=json.dumps(formdata), headers=headers, verify=False)
    print(response.text)
    res = response.json()#转为json格式便于引用
    print(res)
    if res['status'] != 0:
        print("用户不存在，请注册后登入：")
        print("请输入要注册的用户名与密码")
        username = input()
        password = input()
        print("请绑定学号+密码：")
        student_number = input()
        student_password = input()
        url = "http://api.revth.com/auth/register2"
        headers = {"content-type": "application/json"}
        formdata = {
            "username": username,
            "password": password,
            "student_number": student_number,
            "student_password": student_password
        }
        response = requests.post(url, data=json.dumps(formdata), headers=headers, verify=False)
        print("注册情况:" + response.text)
        url = "http://api.revth.com/auth/login"
        headers = {"content-type": "application/json"}
        formdata = {"username": username, "password": password}
        response = requests.post(url, data=json.dumps(formdata), headers=headers, verify=False)
        print(type(response))
        res = response.json()
        print(type(res))
        print(res)
    token = res["data"]["token"]
    user_id = res["data"]["user_id"]
    print("登入状态:" + response.text)
    url = "http://api.revth.com/auth/validate"
    headers = {"X-Auth-Token": token}
    response = requests.get(url, headers=headers)
    print("检测状态:" + response.text)

def ranking():
    """
    排行榜
    """
    url = "http://api.revth.com/rank"
    response = requests.get(url)
    print(response.text)

def historicalRecords(limit, page):
    """
    历史战局列表
    """
    global user_id, token
    url = 'http://api.revth.com/history'
    headers = {'X-Auth-Token': token}
    params = {'player_id':user_id, 'limit': limit, 'page': page}
    response = requests.get(url, params=params, headers=headers)
    print(response.text)

def historicalRecordsDetail(id):
    """
    历史战局详情
    """
    global  token
    url = 'http://api.revth.com/history/'+str(id)
    headers = {'X-Auth-Token': token}
    params = {'id': id}
    response = requests.get(url, params=params, headers=headers)
    print(response.text)

def opengame():
    global token
    global userid
    url = "http://api.revth.com/game/open"
    headers = {"X-Auth-Token": token}
    response = requests.post(url, headers=headers)
    ret=response.json()
    id=ret["data"]["id"]
    card=ret["data"]["card"]
    print(response.text)
    return card

def submitgame(lastPoker):
    """
    提交牌
    """
    global id, token
    url = "http://api.revth.com/game/submit"
    headers = {"X-Auth-Token": token, "content-type": "application/json"}
    formdata = {"id": id, "card": lastPoker}
    response = requests.post(url, data=json.dumps(formdata), headers=headers, verify=False)
    print(response.text)
    return id


def read_opengame():#读入

    str0 = opengame()#开始牌局
    # print(str0)
    str1 = str0.replace("10", "T")
    dex = 0
    for i in range(0, 39, 3):
        if str1[i + 1] == "T":
            x = node(hua_to_number(str1[i]), 10)
        elif str1[i + 1] == "J":
            x = node(hua_to_number(str1[i]), 11)
        elif str1[i + 1] == "Q":
            x = node(hua_to_number(str1[i]), 12)
        elif str1[i + 1] == "K":
            x = node(hua_to_number(str1[i]), 13)
        elif str1[i + 1] == "A":
            x = node(hua_to_number(str1[i]), 14)
        else:
            x = node(hua_to_number(str1[i]), int(str1[i + 1]))
        dex += 1
        poker_1[dex] = x


def printf_ans():#输出
    submit_ans=[]
    s=""
    for i in range(1, 3 + 1):  # 前墩
        if i!=3:
            s+=number_to_hua(end_3[i].flower)+change(end_3[i].num)+" "
        else:
            s+=number_to_hua(end_3[i].flower)+change(end_3[i].num)

    submit_ans.append(s)
    print(s)
    s=""
    for i in range(1, 5 + 1):  # 中墩
        if i != 5:
            s += number_to_hua(end_2[i].flower) + change(end_2[i].num) + " "
        else:
            s += number_to_hua(end_2[i].flower) + change(end_2[i].num)
    submit_ans.append(s)
    print(s)
    s = ""
    for i in range(1, 5 + 1):
        if i != 5:
            s += number_to_hua(end_1[i].flower) + change(end_1[i].num) + " "
        else:
            s += number_to_hua(end_1[i].flower) + change(end_1[i].num)
    submit_ans.append(s)
    print(s)
    return submit_ans
def init_end():
    print("end!")
def init_start():
    print("start!")
    global end_ans,score
    end_ans,score=0.0,0.0
    poker_1.clear()
    poker_2.clear()
    poker_3.clear()
    ans_1.clear()
    ans_2.clear()
    ans_3.clear()
    temp_1.clear()
    temp_2.clear()
    temp_3.clear()
    end_1.clear()
    end_2.clear()
    end_3.clear()
    s1.clear()
    s2.clear()
    s3.clear()
    tempp1.clear()
    tempp2.clear()
    tempp3.clear()
    submit_ans.clear()
    pddun.clear()
    for i in range(0, 20):
        poker_1.append(node(0, 0))
        poker_2.append(node(0, 0))
        poker_3.append(node(0, 0))
        ans_1.append(node(0, 0))
        ans_2.append(node(0, 0))
        ans_3.append(node(0, 0))
        temp_1.append(node(0, 0))
        temp_2.append(node(0, 0))
        temp_3.append(node(0, 0))
        end_1.append(node(0, 0))
        end_2.append(node(0, 0))
        end_3.append(node(0, 0))
        s1.append(0)
        s2.append(0)
        s3.append(0)
        submit_ans.append("")
        pddun.append(node(0,0))

    for i in range(0, 2 + 1):
        tempp1.append(node(0, 0))
        submit_ans.append("")
    for i in range(0, 4 + 1):
        tempp2.append(node(0, 0))
    for i in range(0, 4 + 1):
        tempp3.append(node(0, 0))

    for i in range(0, 15 + 1):
        hua[i] = 0
        number[i] = 0  # 桶排初始化
