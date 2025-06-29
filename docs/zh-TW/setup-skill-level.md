---
title: 自我技能評估表
icon: octicons/paste-24
---

# :octicons-paste-24: 自我技能評估表

這裡提供一份自我評估的量表，方便快速定位對於 Tor、Tails、OONI 瞭解的程度，如果你不知道從哪裡開始學習，可以把評估表當作學習的指引參考。

## Tor 技能分級表

### :material-checkbox-marked-circle-auto-outline: Tor-Basic

=== ":material-checkbox-marked-circle-outline: Tor: Basic L1"

    - [x] 瞭解 Tor 是什麼。
    - [x] 瞭解網路自由為什麼重要、匿名網路是什麼。
    - [x] 臺灣的網路自由嗎？
    - [x] 我們周遭的國家目前的網路狀況。

    !!! abstract "Tor: Basic L1"

        ??? question "瞭解 Tor 是什麼。"

            可以先從這個「[什麼是 Tor？](./what-is-tor.md){target="_blank"}」章節，開始了解。

            通常 Tor 我們是指「洋蔥網路路由」，透過三層節點將網路連線隨機轉送到三台主機進出。「Tor 瀏覽器」是 Tor 團隊利用開源瀏覽器 Firefox 針對洋蔥網路所設計的，方便透過「Tor 瀏覽器」連結 .onion 結尾的網站。

            :octicons-question-24: **補充內容**

            1. **Tor 的背景**：Tor 是最初由美國海軍研究實驗室開發的，其目的是為了保護政府的資訊傳遞。後來開放給大眾使用，以支持言論自由和隱私保護。
            2. **運作方式**：Tor 的名字來自其路由技術—The Onion Router（洋蔥路由）。將你的網路流量加密並隨機轉送多個中繼節點，使網路流量難以被追蹤。
            3. **隱私與安全優點**：使用 Tor 能防止網路監控和流量分析，是隱私保護的重要工具。也因此，Tor 能夠繞過地理封鎖和網路審查，能在網路上更加自由的探索資訊。
            4. **缺點與限制**：儘管 Tor 提供強大的隱私保護，其速度通常比傳統的網際網路連線慢，這是因為流量必須經過多重加密和節點。使用 Tor 也不保證完全匿名，如果使用者不小心透露身份資訊或登入服務帳號，仍有可能被識別。
            5. **法律與道德考量**：在某些國家或地區，使用 Tor 可能被視為違法或不適合，使用者應理解當地法律以免違法。此外，在洋蔥網路中也存在非法活動，使用者在瀏覽時應保持警覺。
            6. **使用技巧**：使用 Tor 時，避免打開不需要的外掛程式、腳本或下載非信任的內容，這些動作可能會洩漏你的真實 IP 或使你暴露於安全風險中。

        ??? question "瞭解網路自由為什麼重要、匿名網路是什麼。"

            可以先從這個「[網路自由為什麼重要？](./internet-freedom-matter.md){target="_blank"}」章節，開始了解。

            :octicons-question-24: **補充內容**

            臺灣的網路算是自由的，但我們周邊鄰近的國家，對於網路管控的程度有著嚴峻的差異。

            1. **網路自由的重要性**：網路自由是一個涉及**言論自由**、**資訊流通**和**隱私權**的議題。自由的網路讓人們可以不受拘束地交流思想、獲取資訊以及表達觀點，這對民主和創新的發展至關重要。在某些國家，網路管控嚴格，政府可能會封鎖網站、限制社交媒體，甚至監控個人流量，這不僅影響了人民的基本人權，也限制了資訊的多樣性與透明度。
            2. 匿名網路是什麼：匿名網路是一種讓使用者能在隱藏身份的情況下瀏覽網路的技術，以保護使用者的隱私及安全。這些網路通常依賴於多層加密及路由技術，例如 Tor 洋蔥路由，讓使用者的流量難以被追蹤。匿名網路在複雜的政治環境下成為一些使用者的安全港，尤其是那些想要規避審查或保護機敏資訊的人。
            3. 匿名網路的優點與風險：使用匿名網路可以保護隱私，並幫助使用者繞過網路審查，到達被封鎖的網站以及和更多的人交流。然而，匿名網路也被一些非法活動所利用，因此可能會引起法律機構的注意和干預。因此，使用者在獲得匿名性和自由的同時，必須理解和承擔由此帶來的風險。

        ??? question "臺灣的網路自由嗎？"

            你覺得臺灣網路自由嗎？當我們在回頭思考這件事的時候，可能可以有一些比較的事件或是參考的資料。

            :octicons-question-24: **補充內容**

            1. **國際排名與報告**：根據「自由之家」（Freedom House）發佈的年度報告，臺灣通常被評為網路自由度高的國家之一。這份報告評估了全球各國在網路訪問的開放性、言論自由以及用戶權利保障等方面的表現。臺灣的網民可以自由地訪問大部分的國際網站，並能在網路上公開表達不同的政治觀點，這在一些鄰近國家可能會面臨限制或風險。
            2. **事件比較**：相比之下，中國實行「防火長城」（Great Firewall）技術，全面封鎖多個國際網站，如 Google、Facebook 和 Twitter/X，進行網路審查。香港在《國安法》實施後，網路自由度也受到影響，出現了部分網頁被封鎖的情況。這些情況使臺灣的網路自由顯得尤為突出。
            3. **當地事件與政策**：在臺灣，雖然網路言論自由受到高度保障，但也面臨著**假消息**和**網路霸凌**的挑戰，政府及民間組織也在積極尋求法律和技術手段加以改善。網路監控方面，政府要求電信業者配合偵查必要時需提供使用者資料，但大多數情況下，這些都受到法律制約，保障公民的隱私權。
            4. **資料參考**：根據多個國際組織的評估，臺灣在網路自由指數上得分較高。這些評估基於網路審查的嚴重性、監控措施、言論自由以及法律制度等方面。

        ??? question "我們周遭的國家目前的網路狀況。"

            這一題是開放的議題，希望可以自行動手搜尋、瞭解臺灣周圍國家網路自由的狀況。以下是一些指引，可以從這裡出發：

            **關鍵字**

            1. **網路自由報告** - 了解各國在網路自由方面的排名及情況，例如搜尋「Freedom House Internet Freedom Report」。
            2. **防火長城（Great Firewall）** - 中國大陸的網路審查機制。
            3. **國家安全法（National Security Law）** - 香港影響網路自由的法律。
            4. **假消息和資訊操縱（Disinformation and Information Manipulation）** - 各國面臨的假消息挑戰。
            5. **網路中斷（Internet Shutdowns）** - 與緬甸相關的事件及其對社會的影響。
            6. **網路監控法規（Internet Surveillance Laws）** - 各國的監控措施和其影響。

            **事件**

            1. **2021 年緬甸軍事政變** - 對該國網路自由的影響。
            2. **新加坡防止網絡謠言法案（POFMA）** - 關於假訊息法案及其實施效果。
            3. **泰國街頭示威與王室批評** - 探討政府對網路監控及言論自由的壓制。
            4. **越南的內容封鎖措施** - 包含網路使用者備受控制的具體事例。

=== ":material-checkbox-marked-circle-outline: Tor: Basic L2"

    - [x] 瞭解 Tor 瀏覽器的連線方式。
    - [x] Tor 橋接（Bridge）類型：Bridge、Snowflake、WebTunnel。
    - [x] 各連線的使用場景、使用時機。
    - [x] 瞭解是否可以透過 VPN 方式連線 Tor。

    !!! abstract "Tor: Basic L2"

        ??? question "瞭解 Tor 瀏覽器的連線方式。"

            「[Tor 瀏覽器](https://www.torproject.org/zh-TW/download/){target="_blank"}」是 Tor 團隊利用開源瀏覽器 [Firefox ESR](https://www.mozilla.org/zh-TW/firefox/enterprise/){target="_blank"} 長期支援版本，針對洋蔥網路所設計的，方便透過「Tor 瀏覽器」連結 .onion 結尾的網站。目前 [Brave](https://brave.com/zh-tw/){target="_blank"}、[Mullvad](https://mullvad.net/zh-hant/browser){target="_blank"} 瀏覽器都可以使用連結 .onion 網站。

            Tor 瀏覽器與一般瀏覽器相似，但特別強調**隱私保護**，並有效阻擋**廣告追蹤**。當您連線到一般網站（非 .onion 網址）時，資料會隨機經過三台 Tor 中繼傳輸。若連線到 .onion 網站，則在第三台中繼之後進入 .onion 網路。

            :octicons-question-24: **補充內容**

            1. **匿名瀏覽**：Tor 瀏覽器主要為保護使用者隱私而設計。當你使用 Tor 瀏覽網路時，你的流量會經過一系列隨機選擇的中繼伺服器，進行多層加密和路由。這使得任何試圖追蹤來源的個人或機構只能看到虛擬的中繼伺服器 IP，而非你的真實 IP 地址。因此，Tor 有效防止網站和服務提供商記錄或追蹤你的 IP 地址和瀏覽行為，提升使用者的匿名性。
            2. **規避審查**：在某些國家或地區，政府可能實施網路審查，限制使用者訪問某些網站或服務。Tor 瀏覽器可以幫助使用者繞過這些封鎖，因為其流量會被轉送至多個國家的中繼伺服器，使得監控和過濾機制難以辨識和阻止具體的網路連線請求。這樣一來，使用者可以自由訪問那些被當地網路管理者或政府禁止的內容，享受更自由的網路使用環境。
            3. **安全防護**：Tor 瀏覽器利用多層加密技術和洋蔥路由，強化網路安全防護，特別是在使用公共 Wi-Fi 或其他不安全的網路環境。每一層傳輸都會進行加密，僅在進入和離開 Tor 網路時解密，各個中繼伺服器只能看到傳入和傳出到直接上下游伺服器，無法掌握完整的傳輸路徑或最終目的地，從而有效降低中間人攻擊的風險，同時保護使用者資料不被竊取或篡改。
            4. **臨時的訪問**：Tor 瀏覽器的一次性使用設計確保使用者的隱私在每次使用結束後都得到徹底保護。當你關閉 Tor 瀏覽器時，所有的瀏覽歷史、Cookies、登入資訊和其他臨時緩存資料會自動被清除，防止他人查看你的瀏覽活動，保障個人資料不被擅取。
            5. **開放原始碼**：Tor 的開源特性意味著其原始碼是公開的，允許開發人員和安全專家進行檢視和修正潛在的漏洞，增強整體的安全性。開源社群合作使 Tor 能夠持續更新，不僅可以應對新興的安全威脅，還能吸引來自全球的開發者合作，有助於隱私保護的提升。

        ??? question "Tor 橋接（Bridge）類型：Bridge、Snowflake、WebTunnel。"

            在 Tor 網路中，橋接（Bridge）伺服器的存在是為了幫助那些受到網路審查或被封鎖的使用者連上 Tor。

            以下是幾種不同類型的 Tor 橋接：

            1. **Bridge**：這是最基本的 Tor 橋接類型。橋接是一種不列於公開 Tor 網路中的秘密入口點，因此不易被封鎖。使用者可以透過手動取得這些橋接來連線到 Tor 網路，繞過常見的封鎖措施。（可以參考如何取得 [Tor Bridge](https://bridges.torproject.org/){target="_blank"}）
            2. **Snowflake**：這種橋接類型特別設計用於應對高強度的網路封鎖。Snowflake 透過 WebRTC 協議讓志工使用他們的瀏覽器成為臨時的 Tor 入口點。因為它是動態的，所以需要做封鎖的難度較高。這種橋接能自動連接並提供更多隨機的入口點，進一步提升連線的可靠性。（可以參考如何安裝 [Snowflake](https://snowflake.torproject.org/){target="_blank"}）
            3. **WebTunnel**：這是一項較新的技術，專門為應對更複雜的封鎖策略而設計。WebTunnel 使用 HTTPS 伺服器作為入口點來緩解傳統橋接可能被封鎖的問題。由於使用了 HTTPS 協議，WebTunnel 的流量難以被區分和封鎖，進而增加突破封鎖的可能性。（可以參考如何建立 [WebTunnel](https://community.torproject.org/relay/setup/webtunnel/){target="_blank"}）

        ??? question "各連線的使用場景、使用時機。"

            1. **Bridge**：
                  - **使用場景**：你處於一個對 Tor 有基本封鎖的環境，比如說，某些學校、職場或網咖限制對 Tor 的連線使用。
                  - **使用時機**：適合需要簡單繞過輕度封鎖的情況下，可以先嘗試基本 Bridge，這通常足以解決大多數基於 IP 的封鎖。同時，你可以從 Tor 官方網站或其他來源取得最新的橋接主機清單。
            2. **Snowflake**：
                  - **使用場景**：面臨類似中國、伊朗等國家的強力封鎖時，這些地方經常使用深層封包檢測（DPI）和 IP 封鎖來阻止 Tor 流量。
                  - **使用時機**：當使用 Bridge 無法突破封鎖，或你需要更隨機的連接方式來避免被偵測和封鎖時，Snowflake 是更好的選擇。由於 Snowflake 利用 WebRTC（網頁即時通訊技術，讓瀏覽器和設備能在不需要中介伺服器的情況下進行點對點連接）進行更為隨機且去中心化的連接，再加上全世界志工的支援，可以提高連線成功率。
            3. **WebTunnel**：
                  - **使用場景**：當你所在的網路不但封鎖了 Tor 入口，還具有更進階的流量監控機制且能快速識別並封鎖 Snowflake。
                  - **使用時機**：當面臨極端封鎖策略且其他橋接類型失敗時，嘗試 WebTunnel。他的 HTTPS 偽裝能更有效地藏匿 Tor 流量於一般網路流量中，例如訪問 HTTPS 網站，難以被區分和封鎖。

        ??? question "瞭解是否可以透過 VPN 方式連線 Tor。"

            透過 VPN 來連接到 Tor 是一種常見的做法，被稱為「VPN-over-Tor」或「Tor-over-VPN」，但這兩者有所不同：

            1. VPN-over-Tor：這種方式是先連接到 Tor 網路，然後再透過 Tor 使用 VPN 服務。這種配置比較少見，因為需要 VPN 提供商支援透過 Tor 網路連接，並且可能不會對你的 IP 地址提供額外的保護。
            2. Tor-over-VPN：這是比較普遍使用的方法。首先連接到 VPN，然後從 VPN 連接到 Tor。這樣的方式對於提升隱私和安全性有一些優點：
                  - 原始的 IP 地址被隱藏在 VPN 伺服器後，使得 ISP（網際網路服務提供商）無法看到你正在使用 Tor。
                  - VPN 連接可以幫助繞過對 Tor 網路入口的封鎖，特別是在某些國家或網路環境中，被擋住 Tor 入口節點的情況下。

=== ":material-checkbox-marked-circle-outline: Tor: Basic L3"

    - [x] 安裝 Tor 瀏覽器，並實際使用至少一週。
    - [x] 透過**直接連線**與**橋接方式**連線到 Tor 網路。
    - [x] 操作切換目前的連線路徑。
    - [x] 連線至 **.onion** 網域。

    !!! abstract "Tor: Basic L3"

        ??? question "安裝 Tor 瀏覽器，並實際使用至少一週。"

            1. 前往 [Tor Project 官方網站](https://www.torproject.org/zh-TW/){target="_blank"}，下載適用於你的作業系統的 Tor 瀏覽器。
            2. 完成下載後，按照指示安裝並啟動 Tor 瀏覽器。
            3. 在整個使用的一週內，用 Tor 瀏覽器進行日常的網路瀏覽，以熟悉其界面和特性，注意使用時的匿名性和安全性。也留意可能造成的不便之處，有無可以解決的方式。

        ??? question "透過**直接連線**與**橋接方式**連線到 Tor 網路。"

            1. 啟動 Tor 瀏覽器時，通常會看到瀏覽器正在建立連線。
            2. 輸入網址即直接透過 Tor 網路瀏覽，此途徑最適合未封鎖 Tor 網路的國家。
            3. 可以透過網址列上位於左側第一個圖示（Tor Circuit，類是這樣的圖示 :material-map-marker-path:）點擊查看目前的路線與連線方式。
            4. 假設你的網路封鎖了 Tor，請選擇「設定（Settings）」、「連線（Connection）」、「橋接（Bridges）」，可從內建的橋接伺服器類型中選擇，或者輸入你從其他途徑取得的橋接連結資訊。

        ??? question "操作切換目前的連線路徑。"

            1. 可以透過網址列上位於左側第一個圖示（Tor Circuit，類是這樣的圖示 :material-map-marker-path:）點擊查看目前的路線與連線方式。
            2. 點擊最後一行「New Tor circuit for this site」，讓 Tor 瀏覽器重新建立連線路徑。這個適合在出口節點剛好被網站阻擋時，嘗試切換不同國家的方式連線。

        ??? question "連線至 .onion 網域"

            1. 連線到[專案網站](https://anoni.net/docs/){target="_blank"}、注意網址列後方出現紫色按鈕「.onion available」 按下後即可跳轉到 .onion 網域。當出現這個按鈕表示該網站有主動提供指引連線到 .onion 網域。
            2. DuckDuckGo 也提供了 .onion 服務：<https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/>{target="_blank"}

### :material-checkbox-marked-circle-auto-outline: Tor-Advanced

=== ":material-checkbox-marked-circle-auto-outline: Tor: Advanced L1"

    - [x] 清楚理解 Tor、Onion、Tor 瀏覽器分別所指的技術。
    - [x] 使用 Snowflake 瀏覽器過充套件建立 Tor 橋接（Bridge）。
    - [x] 啟動 Tor 並透過 SOCKS v5 方式連結。
    - [x] 使用 [metrics.torproject.org](https://metrics.torproject.org){target="_blank"} 查詢臺灣地區的中繼點。

    !!! warning ""

        :wave: 評量參考內容預計在 2025/Q3 完成 Advanced 部分。

=== ":material-checkbox-marked-circle-auto-outline: Tor: Advanced L2"

    - [x] 建立 Tor Relay 中繼點。
    - [x] 建立 Tor Bridge 橋接點。
    - [x] 建立 WebTunnel 中繼點。
    - [x] 建立 **.onion** 網站。

    !!! warning ""

        :wave: 評量參考內容預計在 2025/Q3 完成 Advanced 部分。

## Tails 技能分級表

### :material-checkbox-marked-circle-auto-outline: Tails-Basic

=== ":material-checkbox-marked-circle-outline: Tails: Basic L1"

    - [x] 瞭解 Tails 是什麼與運作原理。
    - [x] 瞭解網路自由為什麼重要、匿名網路是什麼。
    - [x] 臺灣的網路自由嗎？
    - [x] 我們周遭的國家目前的網路狀況。

    !!! abstract "Tails: Basic L1"

        ??? question "瞭解 Tails 是什麼與運作原理。"

            可以先從這個「[什麼是 Tails？](./what-is-tails.md){target="_blank"}」章節，開始了解。

        ??? question "瞭解網路自由為什麼重要、匿名網路是什麼。"

            可以先從這個「[網路自由為什麼重要？](./internet-freedom-matter.md){target="_blank"}」章節，開始了解。

            :octicons-question-24: **補充內容**

            臺灣的網路算是自由的，但我們周邊鄰近的國家，對於網路管控的程度有著嚴峻的差異。

            1. **網路自由的重要性**：網路自由是一個涉及**言論自由**、**資訊流通**和**隱私權**的議題。自由的網路讓人們可以不受拘束地交流思想、獲取資訊以及表達觀點，這對民主和創新的發展至關重要。在某些國家，網路管控嚴格，政府可能會封鎖網站、限制社交媒體，甚至監控個人流量，這不僅影響了人民的基本人權，也限制了資訊的多樣性與透明度。
            2. 匿名網路是什麼：匿名網路是一種讓使用者能在隱藏身份的情況下瀏覽網路的技術，以保護使用者的隱私及安全。這些網路通常依賴於多層加密及路由技術，例如 Tor 洋蔥路由，讓使用者的流量難以被追蹤。匿名網路在複雜的政治環境下成為一些使用者的安全港，尤其是那些想要規避審查或保護機敏資訊的人。
            3. 匿名網路的優點與風險：使用匿名網路可以保護隱私，並幫助使用者繞過網路審查，到達被封鎖的網站以及和更多的人交流。然而，匿名網路也被一些非法活動所利用，因此可能會引起法律機構的注意和干預。因此，使用者在獲得匿名性和自由的同時，必須理解和承擔由此帶來的風險。

        ??? question "臺灣的網路自由嗎？"

            你覺得臺灣網路自由嗎？當我們在回頭思考這件事的時候，可能可以有一些比較的事件或是參考的資料。

            :octicons-question-24: **補充內容**

            1. **國際排名與報告**：根據「自由之家」（Freedom House）發佈的年度報告，臺灣通常被評為網路自由度高的國家之一。這份報告評估了全球各國在網路訪問的開放性、言論自由以及用戶權利保障等方面的表現。臺灣的網民可以自由地訪問大部分的國際網站，並能在網路上公開表達不同的政治觀點，這在一些鄰近國家可能會面臨限制或風險。
            2. **事件比較**：相比之下，中國實行「防火長城」（Great Firewall）技術，全面封鎖多個國際網站，如 Google、Facebook 和 Twitter/X，進行網路審查。香港在《國安法》實施後，網路自由度也受到影響，出現了部分網頁被封鎖的情況。這些情況使臺灣的網路自由顯得尤為突出。
            3. **當地事件與政策**：在臺灣，雖然網路言論自由受到高度保障，但也面臨著**假消息**和**網路霸凌**的挑戰，政府及民間組織也在積極尋求法律和技術手段加以改善。網路監控方面，政府要求電信業者配合偵查必要時需提供使用者資料，但大多數情況下，這些都受到法律制約，保障公民的隱私權。
            4. **資料參考**：根據多個國際組織的評估，臺灣在網路自由指數上得分較高。這些評估基於網路審查的嚴重性、監控措施、言論自由以及法律制度等方面。

        ??? question "我們周遭的國家目前的網路狀況。"

            這一題是開放的議題，希望可以自行動手搜尋、瞭解臺灣周圍國家網路自由的狀況。以下是一些指引，可以從這裡出發：

            **關鍵字**

            1. **網路自由報告** - 了解各國在網路自由方面的排名及情況，例如搜尋「Freedom House Internet Freedom Report」。
            2. **防火長城（Great Firewall）** - 中國大陸的網路審查機制。
            3. **國家安全法（National Security Law）** - 香港影響網路自由的法律。
            4. **假消息和資訊操縱（Disinformation and Information Manipulation）** - 各國面臨的假消息挑戰。
            5. **網路中斷（Internet Shutdowns）** - 與緬甸相關的事件及其對社會的影響。
            6. **網路監控法規（Internet Surveillance Laws）** - 各國的監控措施和其影響。

            **事件**

            1. **2021 年緬甸軍事政變** - 對該國網路自由的影響。
            2. **新加坡防止網絡謠言法案（POFMA）** - 關於假訊息法案及其實施效果。
            3. **泰國街頭示威與王室批評** - 探討政府對網路監控及言論自由的壓制。
            4. **越南的內容封鎖措施** - 包含網路使用者備受控制的具體事例。

=== ":material-checkbox-marked-circle-outline: Tails: Basic L2"

    - [x] 瞭解如何安裝、製作 Tails 作業系統隨身碟。
    - [x] 瞭解電腦如何設定從隨身碟開機。
    - [x] 瞭解 Mac 電腦哪些類型無法使用 Tails。
    - [x] 瞭解 Tails 使用情境與限制。

    !!! abstract "Tails: Basic L2"

        ??? question "瞭解如何安裝、製作 Tails 作業系統隨身碟。"

            - **下載 Tails**：前往 [Tails 官方網站](https://tails.net/){target="_blank"}，下載 Tails ISO 映像檔。
            - **準備工具**：需要一個至少 8GB 的 USB 隨身碟以及 [Balena Etcher](https://etcher.balena.io/){target="_blank"} 或 [Rufus](https://rufus.ie/zh_TW/){target="_blank"} 等工具來製作開機隨身碟。
            - **安裝與製作**：[參閱官網](https://tails.net/install/index.en.html){target="_blank"}所提供的製作流程，選擇合適的作業系統執行。

        ??? question "瞭解電腦如何設定從隨身碟開機。"

            -  **進入 BIOS/UEFI 設定**：在大多數電腦中，重新啟動後會出現按鍵選項（如 F2、F12、Delete），按下對應的鍵進入 BIOS 或 UEFI 設定。
            -  **調整開機順序**：在開機選單中，調整設定使 USB 隨身碟成為主要開機裝置。儲存變更後，重新啟動電腦，系統將自動從 USB 開機。

        ??? question "瞭解 Mac 電腦哪些類型無法使用 Tails。"

            - **不支援的類型**：某些新型 Mac，特別是使用 Apple T2 晶片或 Apple Silicon (M 系列晶片)，由於啟動安全機制，可能會無法順利從非蘋果認證的 USB 裝置啟動。

        ??? question "瞭解 Tails 使用情境與限制。"

            - **使用情境**：Tails 作業系統主要針對需要高隱私保護的人士所設計，例如記者、人權團體或任何希望匿名瀏覽的人。它不留痕跡的運行在記憶體中，關閉後不會在電腦上留下資料。
            - **限制**：
                1. **硬體相容性**：Tails 對於某些硬體驅動程式（特別是新的無線網卡）可能支援有限。
                2. **操作**：由於 Tails 是基於 Linux 的系統、Debian 作業系統、GNOME 桌面環境，對於不熟悉 Linux 環境的人會有一些學習曲線。
                3. **永久儲存**：儘管它可以建立持久性加密磁區（Persistent Storage）以保留某些資料數據，但它的設計初衷是不留痕跡。
                4. **更新頻繁**：為了安全性，Tails 經常更新，需要確保持續更新以保護隱私。

=== ":material-checkbox-marked-circle-outline: Tails: Basic L3"

    - [x] 安裝 Tails，並實際使用至少一週。
    - [x] 建立持久性加密磁區（Persistent Storage）。
    - [x] 使用 Bridge 橋接設定 Tails 網路連線方式。
    - [x] 使用 OnionShare 軟體分享檔案。

    !!! abstract "Tails: Basic L3"

        ??? question "安裝 Tails，並實際使用至少一週。"

            - 參考之前提到的步驟，下載並製作 Tails 開機隨身碟。
            - 插入 USB 隨身碟，重新開機並從 USB 開機，以進入 Tails 作業系統。
            - 使用 Tails 進行一般日常的網路操作一週，這期間熟悉 Tails 的功能和設定，如 Tor 瀏覽、電子郵件的安全使用等。

        ??? question "建立持久性加密磁區（Persistent Storage）。"

            - 開啟 Tails 後，在桌面上找到「Applications」選單，選擇「Tails」>「Configure persistent volume」。
            - 依照指示設定持久性加密磁區，這個區域讓您可以保存一些設定檔案、電子郵件等個人資料，這層磁區是透過加密保護方式確保資料數據安全。
            - 完成加密磁區的建立後，當您重啟 Tails 時，可在登入頁面時選擇是否啟用這個加密磁區。

        ??? question "使用 Bridge 橋接設定 Tails 網路連線方式。"

            - 登入 Tails 後，會出現連線到 Tor 的網路設定。
            - 選擇設定橋接（Bridge）方式，假設你的地區封鎖了直接連接至 Tor。
            - 你可以選擇內建的橋接或手動輸入您已獲得的橋接資訊以繞過封鎖。

        ??? question "使用 OnionShare 軟體分享檔案。"

            - OnionShare 是一個可以透過 Tor 網路安全分享檔案的小工具。
            - 在 Tails 的「Applications」選單中找到並啟動 OnionShare。
            - 透過拖放方式或選取檔案的方式，將想要分享的檔案載入 OnionShare。
            - 啟動分享後，OnionShare 會生成一個 .onion 網址，您可以將這網址提供給信任的人，他們即可使用 Tor 瀏覽器下載。

### :material-checkbox-marked-circle-auto-outline: Tails-Advanced

=== ":material-checkbox-marked-circle-auto-outline: Tails: Advanced L1"

    - [x] 透過 Thunderbird 建立連接 Gmail 信箱的接收與傳送（IMAP 協定）。
    - [x] 更新 Tails 到下一個最新版本。
    - [x] 瞭解 MAC 位址匿名化（MAC Address Anonymization）。
    - [x] 備份持久性加密磁區（Persistent Storage）。

    !!! warning ""

        :wave: 評量參考內容預計在 2025/Q3 完成 Advanced 部分。

=== ":material-checkbox-marked-circle-auto-outline: Tails: Advanced L2"

    - [x] 使用密碼管理器 KeePassXC。
    - [x] 使用 GnuPG 與 Kleopatra 建立加密金鑰與加密檔案。
    - [x] 透過 Thunderbird 寄送加密郵件到 `ooni-research@ocf.tw`（取得公開金鑰請參考「[持續關注](./contact.md)」）。
    - [x] 安全的移除檔案操作流程。

    !!! warning ""

        :wave: 評量參考內容預計在 2025/Q3 完成 Advanced 部分。

## OONI 技能分級表

### :material-checkbox-marked-circle-auto-outline: OONI-Basic

=== ":material-checkbox-marked-circle-outline: OONI: Basic L1"

    - [x] 瞭解 OONI 是什麼。
    - [x] 瞭解網路監視（surveillance）與網路審查（censorship）是什麼。
    - [x] OONI 檢測的運作方式。
    - [x] 臺灣與其他國家在網路監視與網路審查的差異。

    !!! abstract "OONI: Basic L1"

        ??? question "瞭解 OONI 是什麼"

            可以先從這個「[什麼是 OONI？](./what-is-ooni.md){target="_blank"}」章節，開始了解。

        ??? question "瞭解網路監視（surveillance）與網路審查（censorship）是什麼。"

            - **網路監視（surveillance）**：指政府、組織或個人監看和記錄使用者的網路活動，如電子郵件、搜尋歷史、網站瀏覽及通話的過程。監視通常會牽涉到使用監控技術，如資料數據封包檢測，以獲得特定的網路流量資訊。
            - **網路審查（censorship）**：指限制或控制使用者對網際網路上某些資訊的訪問。這可能包括封鎖網站、過濾內容或禁止某些關鍵字搜尋等。審查往往是由政府實施，但也可能由企業或其他機構施行。

        ??? question "OONI 檢測的運作方式。"

            - OONI 提供了免費的開源測試工具 OONI Probe，使用者可以在自己的網路環境執行這些測試來檢測他們的網路是否被審查。
            - OONI Probe 測試會定期發送請求至多個網站和服務，確認在[名單上](./ooni-weblists.md){target="_blank"}的網站、服務是否可以正常訪問。
            - 測試結果會**匿名上傳**到 OONI 的資料伺服器中，並於 [OONI Explorer](https://explorer.ooni.org/zh-Hant){target="_blank"} 上公開，供研究者和公眾使用，以促進對網路自由的理解。

        ??? question "臺灣與其他國家在網路監視與網路審查的差異。"

            - **臺灣**：臺灣的網路環境相對自由，政府並未大規模實施網路審查或監控。使用者可自由瀏覽網際網路的各種內容，政府對於個人隱私權的保護也相對重視。
            - **其他國家**：例如，中國大陸執行嚴格的網路封鎖和審查政策，通常被稱為「防火長城」（Great Firewall），限制訪問許多外國網站和服務。北韓等國則對網路訪問進行更極端的限制，僅允許極少數精選內容。其他一些國家，如俄羅斯和伊朗，也進行不同程度的網路監控和網站封鎖。
            - 可以參考「[網路自由為什麼重要？](./internet-freedom-matter.md){target="_blank"}」章節。

=== ":material-checkbox-marked-circle-outline: OONI: Basic L2"

    - [x] 安裝並使用 OONI Probe 產生檢測報告。
    - [x] 瞭解是否可以使用 VPN 方式使用 OONI Probe 檢測。
    - [x] 瞭解 OONI Probe 使用時的風險。
    - [x] 瞭解 ASN 自治網路的運作。

    !!! abstract "OONI: Basic L2"

        ??? question "安裝並使用 OONI Probe 產生檢測報告"

            - **安裝 OONI Probe**：透過 OONI 官方網站[下載](https://ooni.org/install/){target="_blank"} OONI Probe 應用程式。
            - **使用 OONI Probe**：
                - 啟動應用程式後，您可以選擇要進行的測試類型，例如測試網站封鎖、即時通訊應用程序的連接性、或中間盒（middleboxes）干擾。
                - 點選開始測試後，OONI Probe 會自動執行檢測並產生結果。
                - 結果會上傳至 OONI 的伺服器，並顯示在您的應用程式中，也可以在 OONI Explorer 網站上檢視更詳細的報告。

        ??? question "瞭解是否可以使用 VPN 方式使用 OONI Probe 檢測"

            - 不建議使用 VPN 於 OONI Probe 測試，因為 VPN 會改變您的流量路徑和 IP 地址，這可能會導致檢測到被改變的網路環境，而非您實際所在的網路中可能存在的審查或干擾。
            - 目的是**測試本地網路**的審查情形，應該在不使用 VPN 的情況下進行，才能測量真實的網路狀況。

        ??? question "瞭解 OONI Probe 使用時的風險"

            - 使用 OONI Probe 進行檢測可能會引起您所在網路管理員的注意，尤其在網路審查較嚴格的國家。因此，應了解所在區域的網路政策，衡量使用 OONI Probe 所可能帶來的風險。
            - 在進行測試時，OONI Probe 會訪問不同的網站、服務，這可能會促發網絡監控系統的觀察與紀錄。

        ??? question "瞭解 ASN 自治網路的運作"

            - ASN 是用於識別自治網路（AS）的唯一標識碼。
            - 自治網路是一個或多個 IP 區塊的集合，並由一個或多個網路服務提供者（ISP）或大型企業單位間進行的路由。每個 AS 通過 ASN 在網際網路上相互通訊，以便達到路由資訊和 IP 資料包的交換。ASN 系統機制讓全社界網際網路更有效率的運作，並確保不同網路之間的流量能夠正確到達目標地。可以參考「[ASNs 自治網路觀測資料分析](./ooni-asns-coverage.md){target="_blank"}」中第一段的介紹。

=== ":material-checkbox-marked-circle-outline:OONI: Basic L3"

    - [x] 透過 OONI Explorer 整理臺灣近半年的觀測資料。
    - [x] 透過 OONI Explorer 比較三個國家的觀測資料。
    - [x] 檢視目前網路封鎖的報告。
    - [x] 建立 OONI Run 檢測連結並找到該連結的線上報告內容。

    !!! abstract "OONI: Basic L3"

        ??? question "透過 OONI Explorer 整理臺灣近半年的觀測資料。"

            - 前往 [OONI Explorer](https://explorer.ooni.org/zh-Hant/){target="_blank"} 網站。
            - 在國家欄中找到「台灣」作為觀測地點。
            - 使用日期範圍選擇功能，設定為過去六個月的時間範圍。
            - 查看不同類型的測試結果，例如網站封鎖、即時通訊應用程式的連接情況等。
            - 您可以下載或記錄這段期間出現的相關數據和事件，以進行進一步分析。

        ??? question "透過 OONI Explorer 比較三個國家的觀測資料"

            - 在 OONI Explorer 頁面上，縱軸（Rows）選擇「國家」，使用篩選器（Filters）分別選擇您需要比較的三個國家。（[參考設定](https://explorer.ooni.org/zh-Hant/chart/mat?test_name=web_connectivity&axis_x=measurement_start_day&since=2025-05-01&until=2025-05-30&time_grain=day&axis_y=probe_cc){target="_blank"}）
            - 查看這些國家在不同種類測試中的結果差異，包括網站封鎖、中間人攻擊檢測等。
            - 匯出 CSV 資料比較資料數據。

        ??? question "檢視目前網路封鎖的報告。"

            - 在 OONI Explorer 主頁中，通常會有關於全球網路審查和封鎖的最新報告和趨勢。
            - 瀏覽「[搜尋](https://explorer.ooni.org/zh-Hant/search){target="_blank"}」或搜尋特定服務和網站以查看它們目前連接性狀況。
            - 可以查看「[網路審查](https://explorer.ooni.org/zh-Hant/social-media){target="_blank"}」底下不同的測試類型，例如：社群網站、新聞媒體...等。

        ??? question "建立 OONI Run 檢測連結並找到該連結的線上報告內容。"

            - 在 [OONI Run](https://run.ooni.org/){target="_blank"} 頁面上提供電子郵件取得登入連結。
            - 透過連結登入後，依表單上的必填項目完成填寫。
            - 在「Add URL+」項目新增要檢測的網站網址。完成後按下「Create Link」完成建立。
            - 分享網址或點擊網址後、依引導開啟 OONI Probe 開始檢測。（[參考檢測](https://run.ooni.org/v2/10182){target="_blank"}）
            - 網址後方 `https://run.ooni.org/v2/10182` 的數字 `10182` 即為 OONI Run Link ID，可以在 OONI Explorer 直接輸入 ID 找到檢測結果。（[參考結果](https://explorer.ooni.org/search?since=2025-04-29&until=2026-07-01&failure=false&ooni_run_link_id=10182){target="_blank"}）

### :material-checkbox-marked-circle-auto-outline: OONI-Advanced

=== ":material-checkbox-marked-circle-auto-outline: OONI: Advanced L1"

    - [x] 使用命令列的方式啟動 OONI Probe。
    - [x] 瞭解網站觀測名單收錄方式。

    !!! warning ""

        :wave: 評量參考內容預計在 2025/Q3 完成 Advanced 部分。

=== ":material-checkbox-marked-circle-auto-outline: OONI: Advanced L2"

    - [x] 透過原始觀測資料（Raw Data）進行資料數據整理與分析。
    - [x] 協助名單整理與修正。

    !!! warning ""

        :wave: 評量參考內容預計在 2025/Q3 完成 Advanced 部分。
