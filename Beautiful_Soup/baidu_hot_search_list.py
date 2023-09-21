import requests
from bs4 import BeautifulSoup  # attention: use "pip install beautifulsoup4"

# 发送HTTP请求获取网页内容
url = "https://top.baidu.com/board?tab=realtime"
response = requests.get(url)
html_content = response.text

# 创建Beautiful Soup对象
soup = BeautifulSoup(html_content, "html.parser")

# 查找新闻热搜列表的父元素
hot_searches = soup.find("div", class_="container-bg_lQ801")

# 遍历热搜列表的子元素，提取热搜词

print("Baidu Hot Search")
print("Created By Beautiful Soup")
print("\n")

index = 0

for item in hot_searches.find_all("div", class_="category-wrap_iQLoo horizontal_1eKyQ"):

    index += 1

    _hot_word_title = item.find("div", class_="c-single-text-ellipsis")
    hot_word_title = _hot_word_title.text.strip()

    _hot_word_index = item.find("div", class_="hot-index_1Bl1a")
    hot_word_index = _hot_word_index.text.strip()

    _hot_word_content = item.find("div", class_="hot-desc_1m_jR large_nSuFU")
    hot_word_content = _hot_word_content.get_text("$$").split("$$")[
        0].strip()

    _hot_word_url = item.find("a", class_="img-wrapper_29V76")
    hot_word_url = _hot_word_url.get("href").strip()

    print("No.", index)
    print("- Title:", hot_word_title)
    print("- Index:", hot_word_index)
    print("- Content:", hot_word_content)
    print("- URL:", hot_word_url)
    print("\n")
