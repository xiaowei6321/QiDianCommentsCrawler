import requests
from lxml import html

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.qidian.com/book/1042256511/",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\""
}
cookies = {
    "e1": "%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%7D",
    "e2": "",
    "_csrfToken": "2dOILscCUgy7RVmZFfuBb9Lzt0Zhtl6SO70wImbz",
    "_gid": "GA1.2.1889560694.1746446984",
    "newstatisticUUID": "1746446983_61817549",
    "fu": "39595262",
    "Hm_lvt_f00f67093ce2f38f215010b699629083": "1746446985",
    "HMACCOUNT": "AC63DC4D62D5FE1D",
    "supportwebp": "true",
    "supportWebp": "true",
    "traffic_search_engine": "",
    "se_ref": "",
    "Hm_lpvt_f00f67093ce2f38f215010b699629083": "1746448243",
    "_ga": "GA1.1.2023478495.1746446984",
    "traffic_utm_referer": "https%3A//www.google.com/",
    "x-waf-captcha-referer": "https%3A%2F%2Fwww.qidian.com%2Frank%2F",
    "_ga_FZMMH98S83": "GS1.1.1746446984.1.1.1746448329.0.0.0",
    "_ga_PFYW0QLV3P": "GS1.1.1746446985.1.1.1746448329.0.0.0",
    "w_tsfp": "ltv2UU8E3ewC6mwF46vukE2qEjAkdjgnkwBsXqNmeJ94Q7ErU5mB14J+tsj0MHbZ6sxnt9jMsoszd3qAUdIjeRUcRs+RcI8ZkB/Gy99yicxUQ0k5VYnWS1dOJL9wvmJFfWsIJk2wjzoqdNxCmLU1jQ9atCAmyq90XvFqL5kXjB0ZufzCkpxuDW3HlFWQRzaZciVfKr/c9OtwraxQ9z/c5Vv7LFt0A6hewgfHg31dWzox6wPjMK0ddgmuUtutLvgy23S0hSe2M8T1iEg9sg9qpRxLQISqgiDIWWRYMk4pPEq4kOZgP+7oI+VUrDNvSa45Dh5St05A4btop1ocUnWoYgPdWqUhoAJ2R/Jd/c+pfy7E14/uVhpF+o52wAhs+NdY/TJgNTv2LdleTmPDYXAPL9gCPZ2zZXwzBRBTXDVKsxUTaH5KRg=="
}



hrefs = []
def get_catagory(url):

    headers["Referer"] = url

    


    response = requests.get(url, headers=headers, cookies=cookies)

    # print(response.text)


    tree = html.fromstring(response.text)



    # 查找id为bookName的h1
    # h1_id_bookName = tree.xpath('//h1[@id="bookName"]')



    # 查找所有 div class=catalog_volume '
    div_class_catalog_volumes = tree.xpath('//div[@class="catalog-volume"]')

    print(len(div_class_catalog_volumes))

    for div_class_catalog_volume in div_class_catalog_volumes:
        # 查找div下是否有span class=free
        span_class_free = div_class_catalog_volume.xpath('.//span[@class="free"]')
        # print(len(span_class_free))
        if len(span_class_free) > 0:
            # 当前为免费章节
            # 查找所有 li class=chapter-item
            li_class_chapter_items = div_class_catalog_volume.xpath('.//li[@class="chapter-item"]')
            for li_class_chapter_item in li_class_chapter_items:
                # 打印a标签的href
                a_elements = li_class_chapter_item.xpath('./a')
                for a_element in a_elements:
                    href = a_element.xpath('./@href')
                    chapter_name = a_element.text

                    
                    hrefs.append((href,chapter_name))
        
        
    return hrefs

            
def get_title(url):
    headers["Referer"] = url

    response = requests.get(url, headers=headers, cookies=cookies)

    tree = html.fromstring(response.text)




    # 查找id为bookName的h1
    h1_id_bookName = tree.xpath('//h1[@id="bookName"]')

    return h1_id_bookName[0].text

    
    


if __name__ == "__main__":

    # url = "https://www.qidian.com/book/1042256511/"
    url = "https://www.qidian.com/book/1043182343/"
    hrefs = get_catagory(url)


    print(hrefs)

    title = get_title(url)

    print(title)


