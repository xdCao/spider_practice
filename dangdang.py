import requests
import re

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
"""
<li>
    <div class="list_num ">19.</div>   
    <div class="pic"><a href="http://product.dangdang.com/29585917.html" target="_blank"><img src="http://img3m7.ddimg.cn/64/14/29585917-1_l_1688356874.jpg" alt="千万不要打开这本数学书（套装2册）"  title="千万不要打开这本数学书（套装2册）"/></a></div>    
    <div class="name"><a href="http://product.dangdang.com/29585917.html" target="_blank" title="千万不要打开这本数学书（套装2册）">千万不要打开这本数学书（套装2册）</a></div>    
    <div class="star"><span class="level"><span style="width: 0%;"></span></span><a href="http://product.dangdang.com/29585917.html?point=comment_point" target="_blank">100条评论</a><span class="tuijian">100%推荐</span></div>    
    <div class="publisher_info"><a href="http://search.dangdang.com/?key=丹妮卡・麦凯拉" title="丹妮卡・麦凯拉；小博集出品" target="_blank">丹妮卡・麦凯拉</a>；<a href="http://search.dangdang.com/?key=小博集出品" title="丹妮卡・麦凯拉；小博集出品" target="_blank">小博集出品</a></div>    
    <div class="publisher_info"><span>2023-06-01</span>&nbsp;<a href="http://search.dangdang.com/?key=湖南少年儿童出版社" target="_blank">湖南少年儿童出版社</a></div>    

            <div class="biaosheng">五星评分：<span>100次</span></div>
                      
    
    <div class="price">        
        <p><span class="price_n">&yen;39.80</span>
                        <span class="price_r">&yen;79.60</span>(<span class="price_s">5.0折</span>)
                    </p>
                    <p class="price_e"></p>
                <div class="buy_button">
                          <a ddname="加入购物车" name="" href="javascript:AddToShoppingCart('29585917');" class="listbtn_buy">加入购物车</a>
                        
                        <a ddname="加入收藏" id="addto_favorlist_29585917" name="" href="javascript:showMsgBox('addto_favorlist_29585917',encodeURIComponent('29585917&platform=3'), 'http://myhome.dangdang.com/addFavoritepop');" class="listbtn_collect">收藏</a>
     
        </div>

    </div>
  
    </li>    
"""
regex = re.compile(
    # '<li>.*?list_num.*?(d+).</div>.*?<img src="(.*?)".*?class="name".*?title="(.*?)">.*?class="star">.*?class="tuijian">(.*?)</span>.*?class="publisher_info">.*?target="_blank">(.*?)</a>.*?class="biaosheng">.*?<span>(.*?)</span></div>.*?<p><spansclass="price_n">&yen;(.*?)</span>.*?</li>',
    '<li>\r\n  .*?<div class="list_num .*?>(\d+).*?</div>.*?<img src="(.+?)".*?title="(.+?)".*?star.*?price.*?</li>',
    re.S)
with open('books.txt', 'w', encoding='utf-8') as f:
    for index in range(0, 26):
        response = requests.get(f'http://bang.dangdang.com/books/fivestars/01.00.00.00.00.00-recent30-0-0-1-{index}',
                                headers=headers)
        if response.status_code != 200:
            continue
        full_text = response.text
        all_books = re.findall(regex, full_text)
        for book in all_books:
            f.write(f'{book[0]} {book[1]} {book[2]} \n')
f.close()
