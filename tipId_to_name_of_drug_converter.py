import requests


def get_tip_data(tip_id):
    url = f"https://cwtung.kmu.edu.tw/tipdb/search_json2.php?chemical=&na=&tid={tip_id}&part=All&classify=All&ch_box=all"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9,de;q=0.8",
        "Connection": "keep-alive",
        "Cookie": "_ga=GA1.3.1209442694.1690282137; _gid=GA1.3.396329590.1691480803; _ga_23Q279T0HY=GS1.3.1691480803.2.1.1691480815.48.0.0",
        "DNT": "1",
        "Referer": "https://cwtung.kmu.edu.tw/tipdb/search.php",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"'
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Request failed with status code: {response.status_code}")
        return None


def extract_name_cid(entry):
    if entry and isinstance(entry, list) and len(entry) >= 4:
        name = entry[0].strip('"')
        cid = entry[3].strip('"')
        return name, cid
    return None, None


def main():
    # We can get these ids from file or data
    tipids = ["TIP011972", "TIP003902", "TIP011966", "TIP009181", "TIP007403", "TIP011396", "TIP012195", "TIP012449",
              "TIP000059",
              "TIP003009", "TIP012443", "TIP004484", "TIP011784", "TIP005329", "TIP005863", "TIP011956", "TIP006773",
              "TIP005452", "TIP005871", "TIP004429", "TIP006571", "TIP005240", "TIP011800", "TIP008478", "TIP005866",
              "TIP006810", "TIP007414", "TIP007405", "TIP009264", "TIP013164", "TIP012182", "TIP005576", "TIP008474",
              "TIP007711", "TIP006483", "TIP008007", "TIP008719", "TIP003191"]

    for tip_id in tipids:
        data = get_tip_data(tip_id)
        if data:
            for entry in data[1:]:
                name, cid = extract_name_cid(entry)
                if name and cid:
                    print(f"Name: {name}, CID: {cid}")
                else:
                    print(f"Unable to extract data for {tip_id}")


if __name__ == "__main__":
    main()
