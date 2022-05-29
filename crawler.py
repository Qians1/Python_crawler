
from selenium import webdriver  # 导入Chrome浏览器的驱动
import time
import datetime
 
webdriver = webdriver.Chrome(executable_path='C:\Program Files\Google\Chrome\Application\chrome')     # 打开一个谷歌浏览器
webdriver.maximize_window()
 
def buy_on_time(buytime):
    while True:
        now = datetime.datetime.now()
        if now.strftime('%Y-%m-%d %H:%M:%S') == buytime:
            for i in range(1, 21):   # 每隔0.05秒抢购一次，尝试抢购20次
                webdriver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/input").click()
                webdriver.find_element_by_link_text("去结算").click()
                print(now.strftime('%Y-%m-%d %H:%M:%S'))
                print("第%d次抢购" % i)
                time.sleep(0.05)
            time.sleep(3)
            print('purchase success')
        time.sleep(0.5)
 
def scan():
    webdriver.get("https://item.jd.com/100012043978.html")    # 此为购物车网站 https://cart.jd.com/cart?rd=0.6242487242726857
    time.sleep(3)
    webdriver.find_element_by_xpath('//*[@id="content"]/div[2]/div[1]/div/div[2]/a').click()   # 一般需要登录，此处点击的是去登录按钮
    time.sleep(50)    # 为了避免输入校验码绕过了输入登录账户密码的步骤，此处打开的是二维码页面，请在50秒内用手机app扫描登录。
 
if __name__ == "__main__":
    #  times = input("请输入抢购时间：")
    # 时间格式："2018-09-06 11:20:00.000000"
    scan()
    buy_on_time("2022-01-06 18:00:00.000000")     # 这里设置你需要抢购商品的时