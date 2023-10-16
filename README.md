# OONI 網路干預開放觀察

[安裝 OONI Probe](https://ooni.org/install/) | [觀測資料](https://explorer.ooni.org/)

[OONI](https://ooni.org/)（Open Observatory of Network Interference）是一個觀察網路審查的專案。由全球的志工協助執行[觀測應用程式](https://ooni.org/install/)並偵測阻擋與回報其[觀察結果](https://explorer.ooni.org/)到該組織。

開放文化基金會（Open Culture Foundation, [OCF](https://ocf.tw/)）身為 OONI 的[社群夥伴](https://ooni.org/partners/open-culture-foundation/)之一，協助區域在網路審查議題上的倡議與 OONI 觀察軟體的推廣安裝。

## OONI Probe

[OONI Probe](https://ooni.org/install/) 是一個測量網路審查的軟體，目前支援 Android, iOS, macOS, Windows 或是 [OONI Probe CLI](https://ooni.org/install/cli)（macOS, Debian/Ubunbtu），完整可支援的項目可以[參考](https://ooni.org/install/all)這裡。

安裝完開啟應用程式後，可直接按下 Run 跑完所有的檢測項目，或是針對各項目逐一檢測。

## OONI Data

檢測後的結果都會透過無識別的方式傳送回 [OONI 資料庫](https://ooni.org/data/)儲存，目前有兩個方式可以取得觀察資料作後續研究與洞悉。

### OONI Explorer

可以透過[線上介面](https://explorer.ooni.org/)依區域、檢測類型、時間區間、網域或是 ASN 項目來交叉比對資料。

### OONI Data Mining

OONI 提供直接存取位於 AWS S3 上的觀察資料（[ooni-data-eu-fra](https://ooni-data-eu-fra.s3.eu-central-1.amazonaws.com/) Amazon S3 bucket, delay one hour），可以作大量數據資料下載。

相關的資料格式可以參考 [ooni/spec](https://github.com/ooni/spec)

## 研究項目 Research

### 各區域觀察資料與 ASN 涵蓋率

- 研究狀態：`進行中`

- 研究主題：主要解析目前 OONI 的觀測資料與各區域已知的 [ASN](https://www.cloudflare.com/zh-tw/learning/network-layer/what-is-an-autonomous-system/) 涵蓋狀況，觀察資料是否平均分散在各區域不同的電信或網路架構中。

- 研究方式：
    1. 透過 OONI Data Mining 的方式建立本地資料庫（AWS S3）與全球已知 ASN 列表清單作初步比對。
    2. 建立線上圖表呈現各區域觀察涵蓋資料。
    3. 後端建立與 OONI Data 即時資料串接。

### 檢測名單更新

- 進行狀態：`籌備中`

- 進行內容：檢視 `TW` 檢測名單中的網站列表是否可用。

- 進行方式：
    1. 撰寫檢查腳本或是增修 [`citizenlab/test-lists`](https://github.com/citizenlab/test-lists) 的[檢查腳本](https://github.com/citizenlab/test-lists/blob/master/scripts/prune-dead-urls.py)可以支援區域的指定檢測。
    2. 檢查是否在其他區域有 `.tw` 結尾的網站列表。
    3. 更新需要放入觀察檢測的網站名單。

## 如何參與

目前可以透過兩個方式參與專案：[寄信報名](mailto:"OCF%20財團法人開放文化基金會"%20<hi@ocf.tw>?subject=[OONI]%20參與計畫&body=請簡短自我介紹，後續會有專案人員與您聯絡)或[實習計畫](https://blog.ocf.tw/2023/09/ooni.html)，歡迎加入我們一起研究 OONI！

---

# OONI-Research

Open Culture Foundation ([OCF](https://ocf.tw/)), as a partner of the OONI community, supports censorship measurement from a local perspective and shares internet censorship findings with the public.

You can find more introductions about OONI, OONI Probe, and OONI Explore [here](https://ooni.org/).

## Research Items

The following items are our ongoing or in-progress research projects.

### Censorship Measurement with an ASN Coverage Rate Analysis

- status: `ongoing`

- subject: Analyzing OONI's current observational data alongside the known ASN coverage in different regions, to observe whether the data is evenly distributed across various telecommunications or network infrastructures in different areas.

- methods:
    1. Create a local database using the OONI Data Mining (from AWS S3) approach for preliminary comparisons with a global known ASN list.
    2. Develop online charts to display observation coverage data in various regions.
    3. Establish real-time data integration with OONI Data on the backend.

### Country-specific Test Lists Updated

- status: `in-progress`

- subject: Check if the website list in the `TW` test list is accessible.

- methods:
    1. Write the scripts or modify the [`citizenlab/test-lists`](https://github.com/citizenlab/test-lists) scripts to support country-specific testing.
    2. Check if there are website lists ending with `.tw` in other regions.
    3. Update the list of websites to be included in observation testing.
