from bs4 import BeautifulSoup
import requests
import xlwt

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}

workbook = xlwt.Workbook(encoding='utf-8', style_compression=0)
sheet = workbook.add_sheet('豆瓣Top250', cell_overwrite_ok=True)
sheet.write(0, 0, '名称')
sheet.write(0, 1, '图片')
sheet.write(0, 2, '排名')
sheet.write(0, 3, '评分')
sheet.write(0, 4, '作者')
sheet.write(0, 5, '简介')
cnt = 1
for index in range(0, 11):
    res = requests.get(f'https://movie.douban.com/top250?start={25 * index}&filter=', headers=headers)
    if res.status_code == 200:
        soup = BeautifulSoup(res.text, features='lxml')
        sel = soup.find(class_='grid_view')
        items = sel.find_all('li')
        for item in items:
            item_index = item.find(class_='').string
            img = item.find("a").find("img").get("src")
            name = item.find(class_='title').string
            author = item.find("p").get_text(strip=True)
            rate = item.find(class_='rating_num').string
            introduce = item.find(class_='inq').string if item.find(class_='inq') is not None else ''
            sheet.write(cnt, 0, name)
            sheet.write(cnt, 1, img)
            sheet.write(cnt, 2, item_index)
            sheet.write(cnt, 3, rate)
            sheet.write(cnt, 4, author)
            sheet.write(cnt, 5, introduce)
            cnt += 1
workbook.save(u'豆瓣.xls')
