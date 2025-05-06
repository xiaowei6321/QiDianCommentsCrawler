# https://www.qidian.com/book/1043695973/

# 爬取标题

from A1起点爬取目录byUrl import get_catagory,get_title
from A3起点爬取章节内容byUrl import get_chapter_content
from A5起点爬取segmentIdbyUrl import get_segment_id
from A6起点爬取评论bySegmentId和url import get_comment
import os
import json
# url = "https://www.qidian.com/book/1043695973/"
url ="https://www.qidian.com/book/1038504669/"

title = get_title(url)

print(f"正在爬取{title}...")

# 根据title创建目录
os.makedirs(title, exist_ok=True)

# 爬取所有免费章节

hrefs和chapter_names = get_catagory(url)

print(f"正在爬取{len(hrefs和chapter_names)}章节...")

# 创建一个字典来存储段评
chapter_comments = {}

for href,chapter_name in hrefs和chapter_names:
    href = href[0]
    segment_comments = {}
    # 爬取章节内容和segmentIds
    # p_list = get_chapter_content(href)



    bookId = href.split("/")[-3]
    
    chapterId = href.split("/")[-2]

    # 爬取段评
    int_segment_list = get_segment_id(bookId,chapterId)

    for segmentId in int_segment_list:
        comment_list = get_comment(bookId,chapterId,segmentId)
        print(comment_list)

        segment_comments[segmentId] = comment_list

    chapter_comments[chapter_name] = segment_comments

    # 保存到json文件
    with open(f"{title}/{chapter_name}.json", "w", encoding="utf-8") as f:
        json.dump(chapter_comments, f, ensure_ascii=False)


    


    

























