from selenium import webdriver
from selenium.common import TimeoutException, UnexpectedAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import wait_until
from bs4 import BeautifulSoup


def get_all_videos():
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    videos = soup.find_all(class_='bili-video-card')
    for video in videos:
        try:
            link = video.find('a').get('href')
            title = (video.find(class_='bili-video-card__info--tit').get('title'))
            pic = video.find(class_='bili-video-card__cover').find('img').get('src')
            print(f'标题 {title} 链接 https:{link} 图片 https:{pic}')
        except:
            continue


driver = webdriver.Chrome()
try:
    driver.get("https://www.bilibili.com/")
    driver.implicitly_wait(2)

    WAIT = WebDriverWait(driver, 10)
    input_btn = WAIT.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#nav-searchform > div.nav-search-content > input"))
    )
    submit = WAIT.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#nav-searchform > div.nav-search-btn')))
    input_btn.send_keys('蔡徐坤 篮球')
    submit.click()

    # 跳转到新的窗口
    print('跳转到新窗口')
    all_h = driver.window_handles
    driver.switch_to.window(all_h[1])

    total = WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, "vui_pagenation--btns")))
    lastPage = driver.find_elements(By.CLASS_NAME, 'vui_pagenation--btn')[-1]
    page_index = 1
    get_all_videos()
    while lastPage is not None and lastPage.accessible_name == '下一页':
        try:
            lastPage.click()
            total = WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, "vui_pagenation--btns")))
            lastPage = driver.find_elements(By.CLASS_NAME, 'vui_pagenation--btn')[-1]
            get_all_videos()
            page_index += 1
        except:
            driver.refresh()
            total = WAIT.until(EC.presence_of_element_located((By.CLASS_NAME, "vui_pagenation--btns")))
            lastPage = driver.find_elements(By.CLASS_NAME, 'vui_pagenation--btn')[-1]
            get_all_videos()
finally:
    driver.close()
