---
title: ASNs 自治網路觀測資料分析
icon: material/access-point-network
---

# :material-access-point-network: ASNs 自治網路觀測資料分析

## 什麼是自治系統 AS？

<figure markdown="span" style="width: 80%;">
    <a target="_blank"
       href="https://www.cloudflare.com/zh-tw/learning/network-layer/what-is-an-autonomous-system/">
        <img src="../assets/images/autonomous-system-diagram.svg"
            alt="ASNs 在實際網路上串連在一起，圖示來源：https://www.cloudflare.com/zh-tw/learning/network-layer/what-is-an-autonomous-system/"
            title="ASNs 在實際網路上串連在一起，圖示來源：https://www.cloudflare.com/zh-tw/learning/network-layer/what-is-an-autonomous-system/"
        >
    </a>
    <caption>ASNs 在實際網路上串連在一起（[圖片來源](https://www.cloudflare.com/zh-tw/learning/network-layer/what-is-an-autonomous-system/){target="_blank"}）。</caption>
</figure>

大家每日使用的網路可以簡單的理解為一個由許多互相連結的設備與系統組成的整體，這些設備包括電腦、行動裝置、伺服器、路由器及交換器等，主要功能是讓資料可以在彼此之間進行交換與傳輸。

當我們講到更大規模的網路，例如網際網路（Internet），它其實是由許多個小型網路（如：公司網路、家庭網路、電信網路⋯等）所組成的一個全球性網路。在這樣的架構裡面，自治系統（Autonomous System、AS）是非常重要的概念。

AS 可以被理解為一個單一的管理實體（例如：一家公司、一所大學或國家）所控制的網路群組，它擁有統一的路由策略（進來的流量與出去的流量該往那裡走）。每個 AS 的運作基本上是獨立的，但通過全球路由協定與其他 AS 互相連結，形成整個網際網路的基礎結構。在 AS 之間，使用一種名為 BGP（Border Gateway Protocol、邊界閘道通訊協定）的路由協定來進行資料交換與路由選擇。BGP 可以讓不同的 AS 知道該如何將資料包送到目的地，並且決定使用哪一條路徑是最有效的。每個 AS 都有一個獨一無二的識別號碼，稱為 AS 編號（AS Number、ASN），用以在 BGP 裡面標示這個系統。

!!! tip "郵政系統"

    我們常常用郵政系統來比喻 AS 的運作方式。可以想像 AS 就像是各地的郵件處理中心。這些郵件處理中心的責任是將來自同一區域的郵件集結起來，然後根據各自的運輸策略（可比擬為 BGP 的路由策略）將這些郵件有效率地傳遞到正確的目的地。這個過程中，郵件一旦抵達收件者所在地的郵件處理中心，處理中心會進一步將郵件分配到更精細的位置，如街道、巷弄等。

    這個過程與網際網路的 IP 封包傳遞非常相似：當資料封包抵達目標 AS 時，該 AS 會依據資料封包內的 IP 地址，將資料精確地傳送到最終使用者的設備上，完成這一整個資料傳遞的任務。

    透過這樣的現實生活的例子，我們可以更容易理解 AS 在網際網路中運作的角色與重要性：就像郵件系統依靠處理中心進行運作，網際網路也依賴 AS 來管理和進行資料的傳遞。

## AS 會作壞事嗎？

那你可能會有疑問，AS 聽起來是一群非常「自治」的團體組成，會有人或團體想要作壞事嗎？是的，AS 有時也會涉及到一些不良行為，這些行為可能是有意的，也可能是由意外或錯誤造成的。以下是一些 AS「作壞事」的常見案例和情況：

1. **BGP 劫持（BGP Hijacking）：**這是一種常見問題，可能是有意或無意造成的。AS 可能錯誤地宣告它擁有某些 IP 位址的最佳路由，導致其他AS 將資料錯誤地發送到該 AS。這不僅會造成流量中斷，還可能被利用來攔截或篡改資料。
2. **BGP 洩漏（BGP Leak）：**這種情況發生在一個 AS 意外地將某些路由對不該收到這些資訊流量的其他 AS 進行重新宣告，可能導致廣泛的流量重定向和網路擁堵。
3. **不良內容傳播或主動攻擊：**某些 AS 可能會涉及散佈惡意軟體、垃圾郵件或組織 DDoS 攻擊的活動。這可能是因為 AS 內的伺服器遭到攻擊者利用，或者有些 AS 故意參與這些活動以獲取非法利益。
4. **違反網路中立性規範：**某些 AS，尤其是大型網路供應商（ISP），可能會對某些類型的流量進行限制或優先處理，以此影響網路的公平性。

??? question "自治系統 AS 有哪些組成者？"

    自治系統（AS）是由不同類型的網路管理實體組成的，每個 AS 可能代表一個單獨的組織或一群網路實體。

    這些組成者通常包括：

    1. **網際網路服務供應商（ISP）：**這些公司提供網路服務給個人、家庭和企業。大型 ISP 通常擁有多個 AS 以便進行不同地理區域或服務的管理。
    2. **學術機構與大學：**許多大學和學術研究機構擁有自己的 AS，以管理其校園網路並直接連接到網際網路。
    3. **企業與公司：**大型企業可能擁有自己的 AS，用來管理其全球或區域性辦公室間的連接，確保營運和資料的安全性。
    4. **內容交付網路（CDN）供應商：**這些公司專注於提供快速、可靠的內容傳遞服務，也會擁有自己的 AS 佈局以更有效地接觸全球用戶。
    5. **政府組織：**一些政府機構擁有自己的 AS 來管理內部及與其他政府或公共服務的網路連接。
    6. **非營利組織及其他獨立機構：**例如一些研究機構、技術協會或專業團體，可能擁有自己的 AS 以支持其獨立運營。

??? question "如何查詢目前使用的 ASN？"

    想要知道目前連上網路的 IP 是隸屬於哪家電信與 ASN 編號，可以透過以下服務查詢：

    1. [ip.me](https://ip.me/){target="_blank"}：連上網站後，會有相關的資訊提供，也可以找到 ASN 編號。
    2. [Is BGP safe yet? No.](https://isbgpsafeyet.com/){target="_blank"}：網站服務提供檢查與查詢目前使用的 ISP 的 BGP 是否有狀況。
    3. [Cloudflare Radar（AS3462）](https://radar.cloudflare.com/zh-tw/as3462){target="_blank"}：或是透過 Cloudflare Radar 服務觀察 ASN 流量趨勢與歷程。

## OONI Probe 觀測分析

[OONI](http://ooni.org/){target="_blank"} 是由全球一群志工夥伴協助透過 [Probe 觀測程式](https://ooni.org/install/){target="_blank"}，檢測所在地區是否有網路封鎖、內容審查等問題。透過 OONI Probe 檢查後的檢測資訊會上傳到專案的[公開資料庫](https://registry.opendata.aws/ooni/){target="_blank"}保存紀錄，並提供後續分析與利用。

2023/11 ~ 2024/03 期間，我們有透過[程式抓取](https://github.com/ocftw/ooni-research/tree/main/asn_coverage){target="_blank"}分析公開資料，初步檢視目前觀測資料的樣態，究竟是觀測資料不足還存在其他的問題。

根據 2023/12 的[報告](https://ocf.tw/p/ooni/report/202312.html){target="_blank"}中的發現，目前臺灣的觀察資料在 OONI Explorer 資料庫中排名在前十名，以數量上來說是足夠的，但就資料樣本而言，大部份的觀察資料都集中在 AS3462 與 AS18041 所貢獻的觀測資料，約佔所有觀測資料的 78.94%。臺灣目前約有 437 組 ASNs，觀測資料中不重複的 ASNs 數量僅有 7.32%，多樣性的觀測顯為不足。

此時的資料顯示，目前的觀察還不夠全面與多樣，無法反應目前臺灣的網路樣態，如包含：三大電信業者、有線電視的寬頻服務、固網、第二類電信（虛擬行動網路服務）⋯等。

詳細的內容可以參考以下報告。

[2023/12 觀察報告](https://ocf.tw/p/ooni/report/202312.html){ .md-button .md-button--primary target="_blank" }
