
from bs4 import BeautifulSoup
import pandas as pd


file_path = "../data/20250727nigata6R"

def get_csv_netkeiba_time_index(file_path):
    file_path = str(file_path)
    with open(file_path + ".html", "r", encoding="utf-8") as file:
        html = file.read()


    soup = BeautifulSoup(html, "html.parser")


    # 出馬表テーブルを抽出
    table = soup.select_one("#Speed_List table")


    # テーブルのヘッダを抽出
    header_rows = table.find_all("thead")[0].find_all("tr")
    headers = []

    # ヘッダーの1行目と2行目からカラム名を取得（結合）
    for th in header_rows[0].find_all("th"):
        rowspan = th.get("rowspan")
        colspan = th.get("colspan")
        text = th.get_text(strip=True).replace("\n", "")
        if rowspan == "2":
            headers.append(text)
        elif colspan:  # 3列分の「近走成績」など
            span_headers = [span_th.get_text(strip=True) for span_th in header_rows[1].find_all("th")]
            headers.extend(span_headers)



    # テーブルのヘッダを抽出
    header_rows = table.find_all("thead")[0].find_all("tr")
    headers = []


    # ヘッダーの1行目と2行目からカラム名を取得（結合）
    for th in header_rows[0].find_all("th"):
        rowspan = th.get("rowspan")
        colspan = th.get("colspan")
        text = th.get_text(strip=True).replace("\n", "")
        if rowspan == "2":
            headers.append(text)
        elif colspan:  # 3列分の「近走成績」など
            span_headers = [span_th.get_text(strip=True) for span_th in header_rows[1].find_all("th")]
            headers.extend(span_headers)


    # データ行を抽出
    rows = []
    for tr in table.select("tbody tr"):
        cols = tr.find_all("td")
        row_data = []
        for td in cols:
            # セレクトボックスなどは除き、テキストのみ取得
            span = td.find("span", class_="Sort_Function_Data_Hidden")
            if span:
                try:
                    time_index = span.get_text(strip=True)[1:]
                    time_index = float(time_index)
                    row_data.append(time_index)
                except ValueError:
                    umamei = span.get_text(strip=True)
                    row_data.append(umamei)
                
            else:
                row_data.append(td.get_text(strip=True).replace("\n", ""))
        rows.append(row_data)


    # pandasでデータフレームに変換
    df = pd.DataFrame(rows, columns=headers)
    df = df.drop(columns=["印", "単勝オッズ","人気"])

    df.to_csv(file_path + ".csv", index=False, encoding="utf-8")
    




