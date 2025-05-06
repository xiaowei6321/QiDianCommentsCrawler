import requests
from lxml import html

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.qidian.com/chapter/1042256511/811481404/",
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
    "_csrfToken": "2dOILscCUgy7RVmZFfuBb9Lzt0Zhtl6SO70wImbz",
    "_gid": "GA1.2.1889560694.1746446984",
    "newstatisticUUID": "1746446983_61817549",
    "fu": "39595262",
    "Hm_lvt_f00f67093ce2f38f215010b699629083": "1746446985",
    "HMACCOUNT": "AC63DC4D62D5FE1D",
    "e2": "",
    "e1": "%7B%22l6%22%3A%22%22%2C%22l7%22%3A%22%22%2C%22l1%22%3A3%2C%22l3%22%3A%22%22%2C%22pid%22%3A%22qd_p_qidian%22%2C%22eid%22%3A%22qd_A16%22%7D",
    "supportwebp": "true",
    "supportWebp": "true",
    "traffic_utm_referer": "https%3A%2F%2Fwww.google.com%2F",
    "traffic_search_engine": "",
    "se_ref": "",
    "Hm_lpvt_f00f67093ce2f38f215010b699629083": "1746447163",
    "_ga": "GA1.2.2023478495.1746446984",
    "x-waf-captcha-referer": "https%3A%2F%2Fwww.qidian.com%2Fbook%2F1042256511%2F",
    "_ga_PFYW0QLV3P": "GS2.1.s1746446985$o1$g1$t1746447343$j0$l0$h0",
    "_ga_FZMMH98S83": "GS2.1.s1746446984$o1$g1$t1746447343$j0$l0$h0",
    "w_tsfp": "ltv2UU8E3ewC6mwF46vukE2qEj8kcTwtlw1sXqNmeJ94Q7ErU5mB14J+ucjzNHzd58xnt9jMsoszd3qAUdIjeRUTRsiVeosUkB/Gy99yicxUQ0k5VYnWS1YaI7ojvzkVemIIIkbn3zwtI9BDmLUyi19asychmfgiXvFqL5kXjB0ZufzCkpxuDW3HlFWQRzaZciVfKr/c9OtwraxQ9z/c5Vv7LFt0A6hewgfHg31dWzox6wPjMK0ddgmuUtutLvgy23S0hSe2M8T1iEg9sg9qpRxLUIqrgiDIWXdEJAlpYF63g78xedi5KvRg+2gLVr4XDR1V6hoaxPc7j1FNe2/6J2vOXK4j5F4eFa0E6s/aKnOUlt65Yh1bntwukVk1vpQA7jlnZR//LN9eQGDPZXcae/sSd47obH9hCgAWACVG9B1EOysKX74jP4+W6xOyf0dag+BmYOa+LeBYPy/HVqC4F/s="
}



def get_chapter_content(url):
    p_list=[]

    headers["Referer"] = url
    response = requests.get(url, headers=headers, cookies=cookies)

    # print(response.text)

    # id = c-811481404
    id ="c-"+url.split("/")[-2]

    # print(id)

    tree = html.fromstring(response.text)

    # 获取id为c-811481404的main下所有p
    # p_elements = tree.xpath(f'//*[@id="{id}"]/p')
    # main_element = tree.xpath(f'//*[@id="c-811481404"]')
    main_element = tree.xpath(f'//*[@id="{id}"]')
    
    # print(len(main_element))
    p_elements = main_element[0].xpath('./p')


    # print(len(p_elements))

    for p_element in p_elements:
        p_list.append(p_element.text)

    return p_list



if __name__ == "__main__":
    # url = "https://www.qidian.com/chapter/1042256511/811481404/"
    # url="https://www.qidian.com/chapter/1042256511/811683763/"
    url="https://www.qidian.com/chapter/1043182343/824379142/"
    p_list = get_chapter_content(url)

    print(p_list)



