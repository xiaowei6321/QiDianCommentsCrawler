import requests
from lxml import html


headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Pragma": "no-cache",
    "Referer": "https://www.qidian.com/chapter/1043182343/824380554/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "X-D": "0",
    "X-Yuew-sign": "896d21740c52bf2a166e77788467dec5",
    "X-Yuew-time": "1746456894",
    "baggage": "sentry-environment=pro,sentry-release=pc-v2025041001,sentry-public_key=52499cfbaf454bbaabe30479d1142afa,sentry-trace_id=b1fbf7f8eb15471daf22f28411b47409,sentry-sample_rate=0.01,sentry-sampled=false",
    "sec-ch-ua": "\"Google Chrome\";v=\"135\", \"Not-A.Brand\";v=\"8\", \"Chromium\";v=\"135\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sentry-trace": "b1fbf7f8eb15471daf22f28411b47409-8231db722339b1a4-0",
    "traceparent": "00-c793925a1404cfab3249b96598ccfbbb-e77ed687c228ae2c-01"
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
    "traffic_search_engine": "",
    "se_ref": "",
    "traffic_utm_referer": "https%3A%2F%2Fwww.google.com%2F",
    "_gat_gtag_UA_199934072_2": "1",
    "_ga": "GA1.1.2023478495.1746446984",
    "Hm_lpvt_f00f67093ce2f38f215010b699629083": "1746456854",
    "_ga_FZMMH98S83": "GS2.1.s1746456676$o4$g1$t1746456891$j0$l0$h0",
    "_ga_PFYW0QLV3P": "GS2.1.s1746456676$o4$g1$t1746456891$j0$l0$h0",
    "w_tsfp": "ltvuV0MF2utBvS0Q7aztkU2mHzglcTs4h0wpEaR0f5thQLErU5mB14J/uMP+MXbZ5Mxnvd7DsZoyJTLYCJI3dwMUFJqUdosZ2V+VmoIs3d9GBRRuGM3ZXwEdJ7gm7GZBeXhCNxS00jA8eIUd379yilkMsyN1zap3TO14fstJ019E6KDQmI5uDW3HlFWQRzaLbjcMcuqPr6g18L5a5T+Otgn4eFJ1A7JLg0KT0yEWDnkg4Bbpd+tdPB2vJs6vSqA="
}



url = "https://www.qidian.com/ajax/chapterReview/reviewSummary"
params = {
    "bookId": "1043182343",
    "chapterId": "824380554",
    "_csrfToken": "2dOILscCUgy7RVmZFfuBb9Lzt0Zhtl6SO70wImbz"
}
# response = requests.get(url, headers=headers, cookies=cookies, params=params)

# print(response.text)
# print(response)


def get_segment_id(bookId,chapterId):
    int_segment_list=[]


    headers["Referer"] = url
    params["bookId"] = bookId
    params["chapterId"] = chapterId


    response = requests.get(url, headers=headers, cookies=cookies, params=params).json()

    # print(response) 
    segment_list = response["data"]["list"]

    for segment in segment_list:
        # print(segment["segmentId"])
        # print(segment["segmentName"])
        # print(f"segmentId:{segment['segmentId']},reviewNum:{segment['reviewNum']}")
        int_segment_list.append(segment["segmentId"])

    return int_segment_list

    




if __name__ == "__main__":
    bookId = "1043182343"
    chapterId = "824380554"
    int_segment_list =  get_segment_id(bookId,chapterId)

    print(int_segment_list)



