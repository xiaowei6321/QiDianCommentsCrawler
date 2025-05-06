# 获取评论





import requests


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.qidian.com/chapter/1042256511/811481404/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "X-D": "0",
    "X-Yuew-sign": "d8631ca5725d9716a931d54beb17125b",
    "X-Yuew-time": "1746447171",
    "baggage": "sentry-environment=pro,sentry-release=pc-v2025041001,sentry-public_key=52499cfbaf454bbaabe30479d1142afa,sentry-trace_id=e866493735a3464ab0a4ced903df8585",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sentry-trace": "e866493735a3464ab0a4ced903df8585-8cd5c3dd66ea5289",
    "traceparent": "00-2a2a80bc3d179b5053d85af4a6ea54c5-855e3b7f520092d7-01"
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
    "_ga_PFYW0QLV3P": "GS2.1.s1746446985$o1$g1$t1746447163$j0$l0$h0",
    "_ga_FZMMH98S83": "GS2.1.s1746446984$o1$g1$t1746447163$j0$l0$h0",
    "_ga": "GA1.2.2023478495.1746446984",
    "_gat_gtag_UA_199934072_2": "1",
    "w_tsfp": "ltvuV0MF2utBvS0Q7aztkEyvETgmdTE4h0wpEaR0f5thQLErU5mB14J+ucrwMHTa4cxnvd7DsZoyJTLYCJI3dwNBE5qWIosUhQWSkoAtit8QBUFlGJ3eC1EeIL907zdOfnhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5WmI51j8LVMiC7kR0hab0H0WBn1xtxTpdetcMByscZr7SqA="
}


url = "https://www.qidian.com/ajax/chapterReview/reviewList"
params = {
    "bookId": "1042256511",
    "chapterId": "811481404",
    "page": "1",
    "pageSize": "20",
    "segmentId": "1",
    "type": "2",
    "_csrfToken": "2dOILscCUgy7RVmZFfuBb9Lzt0Zhtl6SO70wImbz"
}




def get_comment(bookId,chapterId,segmentId):
    comment_list=[]
    headers["Referer"] = f"https://www.qidian.com/chapter/{bookId}/{chapterId}/"
    params["bookId"] = bookId
    params["chapterId"] = chapterId
    params["segmentId"] = segmentId

    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()





    content_list = response["data"]["list"]



    for content in content_list:
        # print(content["content"])
        comment_list.append(content["content"])

    return comment_list


if __name__ == "__main__":
    # bookId = "1042256511"
    # chapterId = "811481404"
    # segmentId = "1"
    bookId = "1043182343"
    chapterId = "824379142"
    segmentId = "2"
    comment_list = get_comment(bookId,chapterId,segmentId)
    print(comment_list)



