import re


def solution(word, pages):
    info = {}

    for i, page in enumerate(pages):
        index = i
        link = get_page_link(page)
        external_links = get_external_links(page)
        base_score = get_base_score(word, page)
        link_score = 0
        matching_score = 0
        info[link] = [index, external_links, base_score, link_score, matching_score]

    for link, [index, external_links, base_score, link_score, matching_score] in info.items():
        for external_link in external_links:
            if external_link in info:
                info[external_link][-2] += base_score / len(external_links)

    for v in info.values():
        v[-1] = v[-2] + v[-3]

    print(info)
    return sorted(info.values(), key=lambda x: (-x[-1], x[0]))[0][0]


def get_page_link(page):
    return re.search(r"<meta property=\"og:url\" content=\"(https://\S+)\"/>", page).group(1)


def get_tag(tag, page):
    return re.search(r"(?s)<%s>(.*)</%s>" % (tag, tag), page).group(1)


def get_external_links(page):
    return re.findall(r"<a href=\"(https://\S*)\"", page)


def get_base_score(word, page):
    body = get_tag("body", page)
    body = re.sub(r"<a href=\"https://[\S]*\">(.*)</a>", r"\1", body)
    body = body.lower()
    body = re.sub(r"[^a-zA-Z]", ' ', body)
    body = body.split()
    return body.count(word.lower())


word = "Muzi"
pages = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://careers.kakao.com/interview/list\"/>\n</head>  \n<body>\n<a href=\"https://programmers.co.kr/learn/courses/4673\"></a>#!MuziMuzi!)jayg07con&&\n\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://www.kakaocorp.com\"/>\n</head>  \n<body>\ncon%\tmuzI92apeach&2<a href=\"https://hashcode.co.kr/tos\"></a>\n\n\t^\n</body>\n</html>"]


print(solution(word, pages))