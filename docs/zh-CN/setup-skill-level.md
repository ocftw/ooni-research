---
title: 自我技能评估表
icon: octicons/paste-24
---

# :octicons-paste-24: 自我技能评估表

这里提供一份自我评估的量表，方便快速定位对于 Tor、Tails、OONI 了解的程度，如果你不知道从哪里开始学习，可以将评估表当作学习的指引参考。

## Tor 技能分级表

### :material-checkbox-marked-circle-auto-outline: Tor-Basic

=== ":material-checkbox-marked-circle-outline: Tor: Basic L1"

    - [x] 了解 Tor 是什么。
    - [x] 了解网络自由为什么重要、匿名网络是什么。
    - [x] 台湾的网络自由吗？
    - [x] 我们周遭的国家目前的网络状况。

    !!! abstract "Tor: Basic L1"

        ??? question "了解 Tor 是什么。"

            可以先从这个「[什么是 Tor？](./what-is-tor.md){target="_blank"}」章节开始了解。

            通常 Tor 我们所指的是「洋葱网络路由」，通过三层节点将网络连接随机转送到三台主机进出。「Tor 浏览器」 是 Tor 团队利用开源浏览器 Firefox 针对洋葱网络所设计的，方便通过「Tor 浏览器」连接 .onion 结尾的网站。

            :octicons-question-24: **补充内容**

            1. **Tor 的背景**：Tor 最初由美国海军研究实验室开发，其目的是为了保护政府的信息传递。后来开放给大众使用，以支持言论自由和隐私保护。
            2. **运作方式**：Tor 的名字来自其路由技术—The Onion Router（洋葱路由）。将你的网络流量加密并随机转送多个中继节点，使网络流量难以被追踪。
            3. **隐私与安全优点**：使用 Tor 能防止网络监控和流量分析，是隐私保护的重要工具。也因此，Tor 能够绕过地理封锁和网络审查，能在网络上更加自由地探索信息。
            4. **缺点与限制**：尽管 Tor 提供强大的隐私保护，其速度通常比传统的互联网连接慢，这是因为流量必须经过多重加密和节点。使用 Tor 也不保证完全匿名，如果用户不小心透露身份信息或登入服务账号，仍有可能被识别。
            5. **法律与道德考量**：在某些国家或地区，使用 Tor 可能被视为违法或不适合，用户应理解当地法律以免违法。此外，在洋葱网络中也存在非法活动，用户在浏览时应保持警觉。
            6. **使用技巧**：使用 Tor 时，避免打开不需要的插件、脚本或下载不信任的内容，这些动作可能会泄露你的真实 IP 或使你暴露于安全风险中。

        ??? question "了解网络自由为什么重要、匿名网络是什么。"

            可以先从这个「[网络自由为什么重要？](./internet-freedom-matter.md){target="_blank"}」章节开始了解。

            :octicons-question-24: **补充内容**

            台湾的网络算是自由的，但我们周边邻近的国家，对于网络管控的程度有着严峻的差异。

            1. **网络自由的重要性**：网络自由是一个涉及**言论自由**、**信息流通**和**隐私权**的议题。自由的网络让人们可以不受拘束地交流思想、获取信息以及表达观点，这对民主和创新的发展至关重要。在某些国家，网络管控严格，政府可能会封锁网站、限制社交媒体，甚至监控个人流量，这不仅影响了人民的基本人权，也限制了信息的多样性与透明度。
            2. **匿名网络是什么**：匿名网络是一种让用户能在隐藏身份的情况下浏览网络的技术，以保护用户的隐私及安全。这些网络通常依赖于多层加密及路由技术，例如 Tor 洋葱路由，让用户的流量难以被追踪。匿名网络在复杂的政治环境下成为一些用户的安全港，尤其是那些想要规避审查或保护机敏信息的人。
            3. **匿名网络的优点与风险**：使用匿名网络可以保护隐私，并帮助用户绕过网络审查，到达被封锁的网站以及和更多的人交流。然而，匿名网络也被一些非法活动所利用，因此可能会引起法律机构的注意和干预。因此，用户在获得匿名性和自由的同时，必须理解和承担由此带来的风险。

        ??? question "台湾的网络自由吗？"

            你觉得台湾网络自由吗？当我们在回头思考这件事的时候，可能可以有一些比较的事件或是参考的资料。

            :octicons-question-24: **补充内容**

            1. **国际排名与报告**：根据「自由之家」（Freedom House）发布的年度报告，台湾通常被评为网络自由度高的国家之一。这份报告评估了全球各国在网络访问的开放性、言论自由以及用户权利保障等方面的表现。台湾的网民可以自由地访问大部分的国际网站，并能在网络上公开表达不同的政治观点，这在一些邻近国家可能会面临限制或风险。
            2. **事件比较**：相比之下，中国实行「防火长城」（Great Firewall）技术，全面封锁多个国际网站，如 Google、Facebook 和 Twitter/X，进行网络审查。香港在《国安法》实施后，网络自由度也受到影响，出现了部分网页被封锁的情况。这些情况使台湾的网络自由显得尤为突出。
            3. **当地事件与政策**：在台湾，虽然网络言论自由受到高度保障，但也面临着**假信息**和**网络霸凌**的挑战，政府及民间组织也在积极寻求法律和技术手段加以改善。网络监控方面，政府要求电信业者配合侦查必要时需提供用户资料，但大多数情况下，这些都受到法律制约，保障公民的隐私权。
            4. **资料参考**：根据多个国际组织的评估，台湾在网络自由指数上得分较高。这些评估基于网络审查的严重性、监控措施、言论自由以及法律制度等方面。

        ??? question "我们周遭的国家目前的网络状况。"

            这一题是开放的议题，希望可以自行动手搜索、了解台湾周围国家网络自由的状况。以下是一些指引，可以从这里出发：

            **关键词**

            1. **网络自由报告** - 了解各国在网络自由方面的排名及情况，例如搜索「Freedom House Internet Freedom Report」。
            2. **防火长城（Great Firewall）** - 中国大陆的网络审查机制。
            3. **国家安全法（National Security Law）** - 香港影响网络自由的法律。
            4. **假消息和信息操纵（Disinformation and Information Manipulation）** - 各国面临的假消息挑战。
            5. **网络中断（Internet Shutdowns）** - 与缅甸相关的事件及其对社会的影响。
            6. **网络监控法规（Internet Surveillance Laws）** - 各国的监控措施和其影响。

            **事件**

            1. **2021年缅甸军事政变** - 对该国网络自由的影响。
            2. **新加坡防止网络谣言法案（POFMA）** - 关于假信息法案及其实施效果。
            3. **泰国街头示威与王室批评** - 探讨政府对网络监控及言论自由的压制。
            4. **越南的内容封锁措施** - 包含网络用户备受控制的具体事例。

=== ":material-checkbox-marked-circle-outline: Tor: Basic L2"

    - [x] 了解 Tor 浏览器的连接方式。
    - [x] Tor 桥接（Bridge）类型：Bridge、Snowflake、WebTunnel。
    - [x] 各连接的使用场景、使用时机。
    - [x] 了解是否可以通过 VPN 方式连接 Tor。

    !!! abstract "Tor: Basic L2"

        ??? question "了解 Tor 浏览器的连接方式。"

            「[Tor 浏览器](https://www.torproject.org/zh-CN/download/){target="_blank"}」 是 Tor 团队利用开源浏览器 [Firefox ESR](https://www.mozilla.org/zh-CN/firefox/enterprise/){target="_blank"} 长期支持版本，针对洋葱网络所设计的，方便通过「Tor 浏览器」连接 .onion 结尾的网站。目前 [Brave](https://brave.com/zh-cn/){target="_blank"}、[Mullvad](https://mullvad.net/zh-cn/browser){target="_blank"} 浏览器都可以使用连接 .onion 网站。

            Tor 浏览器与一般浏览器相似，但特别强调**隐私保护**，并有效阻挡**广告追踪**。当您连接到一般网站（非 .onion 地址）时，数据会随机经过三台 Tor 中继传输。若连接到 .onion 网站，则在第三台中继之后进入 .onion 网络。

            :octicons-question-24: **补充内容**

            1. **匿名浏览**：Tor 浏览器主要为保护用户隐私而设计。当你使用 Tor 浏览网络时，你的流量会经过一系列随机选择的中继服务器，进行多层加密和路由。这使得任何试图追踪来源的个人或机构只能看到虚拟的中继服务器 IP，而非你的真实 IP 地址。因此，Tor 有效防止网站和服务提供商记录或追踪你的 IP 地址和浏览行为，提升用户的匿名性。
            2. **规避审查**：在某些国家或地区，政府可能实施网络审查，限制用户访问某些网站或服务。Tor 浏览器可以帮助用户绕过这些封锁，因为其流量会被转送至多个国家的中继服务器，使得监控和过滤机制难以辨识和阻止具体的网络连接请求。这样一来，用户可以自由访问那些被当地网络管理者或政府禁止的内容，享受更自由的网络使用环境。
            3. **安全防护**：Tor 浏览器利用多层加密技术和洋葱路由，强化网络安全防护，特别是在使用公共 Wi-Fi 或其他不安全的网络环境。每一层传输都会进行加密，仅在进入和离开 Tor 网络时解密，各个中继服务器只能看到传入和传出到直接上下游服务器，无法掌握完整的传输路径或最终目的地，从而有效降低中间人攻击的风险，同时保护用户数据不被窃取或篡改。
            4. **临时的访问**：Tor 浏览器的一次性使用设计确保用户的隐私在每次使用结束后都得到彻底保护。当你关闭 Tor 浏览器时，所有的浏览历史、Cookies、登录信息和其他临时缓存数据会自动被清除，防止他人查看你的浏览活动，保障个人资料不被擅取。
            5. **开放源码**：Tor 的开源特性意味着其源代码是公开的，允许开发人员和安全专家进行检视和修正潜在的漏洞，增强整体的安全性。开源社区合作使 Tor 能够持续更新，不仅可以应对新兴的安全威胁，还能吸引来自全球的开发者合作，有助于隐私保护的提升。

        ??? question "Tor 桥接（Bridge）类型：Bridge、Snowflake、WebTunnel。"

            在 Tor 网络中，桥接（Bridge）服务器的存在是为了帮助那些受到网络审查或被封锁的用户连接到 Tor。

            以下是几种不同类型的 Tor 桥接：

            1. **Bridge**：这是最基本的 Tor 桥接类型。桥接是一种不列于公开 Tor 网络中的秘密入口点，因此不易被封锁。用户可以通过手动取得这些桥接来连接到 Tor 网络，绕过常见的封锁措施。（可以参考如何取得 [Tor Bridge](https://bridges.torproject.org/){target="_blank"}）
            2. **Snowflake**：这种桥接类型特别设计用于应对高强度的网络封锁。Snowflake 通过 WebRTC 协议让志愿者使用他们的浏览器成为临时的 Tor 入口点。因为它是动态的，所以需要进行封锁的难度较高。这种桥接能自动连接并提供更多随机的入口点，进一步提升连接的可靠性。（可以参考如何安装 [Snowflake](https://snowflake.torproject.org/){target="_blank"}）
            3. **WebTunnel**：这是一项较新的技术，专门为应对更复杂的封锁策略而设计。WebTunnel 使用 HTTPS 服务器作为入口点来缓解传统桥接可能被封锁的问题。由于使用了 HTTPS 协议，WebTunnel 的流量难以被区分和封锁，进而增加突破封锁的可能性。（可以参考如何建立 [WebTunnel](https://community.torproject.org/relay/setup/webtunnel/){target="_blank"}）

        ??? question "各连接的使用场景、使用时机。"

            1. **Bridge**：
                - **使用场景**：你处于一个对 Tor 有基本封锁的环境，比如说，某些学校、职场或网吧限制对 Tor 的连接使用。
                - **使用时机**：适合需要简单绕过轻度封锁的情况下，可以先尝试基本 Bridge，这通常足以解决大多数基于 IP 的封锁。同时，你可以从 Tor 官方网站或其他来源取得最新的桥接主机清单。
            2. **Snowflake**：
                - **使用场景**：面临类似中国、伊朗等国家的强力封锁时，这些地方经常使用深层包检测（DPI）和 IP 封锁来阻止 Tor 流量。
                - **使用时机**：当使用 Bridge 无法突破封锁，或你需要更随机的连接方式来避免被检测和封锁时，Snowflake 是更好的选择。由于 Snowflake 利用 WebRTC（网页即时通讯技术，让浏览器和设备能在不需要中介服务器的情况下进行点对点连接）进行更为随机且去中心化的连接，再加上全世界志愿者的支持，可以提高连接成功率。
            3. **WebTunnel**：
                - **使用场景**：当你所在的网络不仅封锁了 Tor 入口，还具有更进阶的流量监控机制且能快速识别并封锁 Snowflake。
                - **使用时机**：当面临极端封锁策略且其他桥接类型失败时，尝试 WebTunnel。它的 HTTPS 伪装能更有效地藏匿 Tor 流量于一般网络流量中，例如访问 HTTPS 网站，难以被区分和封锁。

        ??? question "了解是否可以通过 VPN 方式连接 Tor。"

            通过 VPN 来连接到 Tor 是一种常见的做法，被称为「VPN-over-Tor」或「Tor-over-VPN」，但这两者有所不同：

            1. **VPN-over-Tor**：这种方式是先连接到 Tor 网络，然后再通过 Tor 使用 VPN 服务。这种配置比较少见，因为需要 VPN 提供商支持通过 Tor 网络连接，并且可能不会对你的 IP 地址提供额外的保护。
            2. **Tor-over-VPN**：这是比较普遍使用的方法。首先连接到 VPN，然后从 VPN 连接到 Tor。这样的方式对于提升隐私和安全性有一些优点：
                - 原始的 IP 地址被隐藏在 VPN 服务器后，使得 ISP（互联网服务提供商）无法看到你正在使用 Tor。
                - VPN 连接可以帮助绕过对 Tor 网络入口的封锁，特别是在某些国家或网络环境中，被挡住 Tor 入口节点的情况下。

=== ":material-checkbox-marked-circle-outline: Tor: Basic L3"

    - [x] 安装 Tor 浏览器，并实际使用至少一周。
    - [x] 通过**直接连接**与**桥接方式**连接到 Tor 网络。
    - [x] 操作切换当前的连接路径。
    - [x] 连接至 **.onion** 域。

    !!! abstract "Tor: Basic L3"

        ??? question "安装 Tor 浏览器，并实际使用至少一周。"

            1. 前往 [Tor Project 官方网站](https://www.torproject.org/zh-CN/){target="_blank"}，下载适用于你的操作系统的 Tor 浏览器。
            2. 完成下载后，按照指示安装并启动 Tor 浏览器。
            3. 在整个使用的一周内，用 Tor 浏览器进行日常的网络浏览，以熟悉其界面和特性，注意使用时的匿名性和安全性。也留意可能造成的不便之处，有无可以解决的方式。

        ??? question "通过**直接连接**与**桥接方式**连接到 Tor 网络。"

            1. 启动 Tor 浏览器时，通常会看到浏览器正在建立连接。
            2. 输入网址即直接通过 Tor 网络浏览，此途径最适合未封锁 Tor 网络的国家。
            3. 可以通过地址栏上位于左侧第一个图标（Tor Circuit，类似这样的图示 :material-map-marker-path:）点击查看当前的路线与连接方式。
            4. 假如你的网络封锁了 Tor，请选择「设置（Settings）」、「连接（Connection）」、「桥接（Bridges）」，可从内建的桥接服务器类型中选择，或者输入你从其他途径获取的桥接链接信息。

        ??? question "操作切换当前的连接路径。"

            1. 可以通过地址栏上位于左侧第一个图标（Tor Circuit，类似这样的图示 :material-map-marker-path:）点击查看当前的路线与连接方式。
            2. 点击最后一行「New Tor circuit for this site」，让 Tor 浏览器重新建立连接路径。这适合在出口节点刚好被网站阻挡时，尝试切换不同国家的方式连接。

        ??? question "连接至 .onion 域"

            1. 连接到[项目网站](https://ooni-research.ocf.tw/docs/){target="_blank"}、注意地址栏后方出现紫色按钮「.onion available」 按下后即可跳转到 .onion 域。当出现这个按钮表示该网站有主动提供指引连接到 .onion 域。
            2. DuckDuckGo 也提供了 .onion 服务：<https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/>{target="_blank"}

### :material-checkbox-marked-circle-auto-outline: Tor-Advanced

=== ":material-checkbox-marked-circle-auto-outline: Tor: Advanced L1"

    - [x] 清楚理解 Tor、Onion、Tor 浏览器分别所指的技术。
    - [x] 使用 Snowflake 浏览器扩充插件建立 Tor 桥接（Bridge）。
    - [x] 启动 Tor 并通过 SOCKS v5 方式连接。
    - [x] 使用 [metrics.torproject.org](https://metrics.torproject.org){target="_blank"} 查询台湾地区的中继点。

    !!! warning ""
        :wave: 评估参考内容预计在 2025/Q3 完成 Advanced 部分。

=== ":material-checkbox-marked-circle-auto-outline: Tor: Advanced L2"

    - [x] 建立 Tor Relay 中继点。
    - [x] 建立 Tor Bridge 桥接点。
    - [x] 建立 WebTunnel 中继点。
    - [x] 建立 **.onion** 网站。

    !!! warning ""
        :wave: 评估参考内容预计在 2025/Q3 完成 Advanced 部分。

## Tails 技能分级表

### :material-checkbox-marked-circle-auto-outline: Tails-Basic

=== ":material-checkbox-marked-circle-outline: Tails: Basic L1"

    - [x] 了解 Tails 是什么与运作原理。
    - [x] 了解网络自由为什么重要、匿名网络是什么。
    - [x] 台湾的网络自由吗？
    - [x] 我们周遭的国家目前的网络状况。

    !!! abstract "Tails: Basic L1"

        ??? question "了解 Tails 是什么与运作原理。"

            可以先从这个「[什么是 Tails？](./what-is-tails.md){target="_blank"}」章节开始了解。

        ??? question "了解网络自由为什么重要、匿名网络是什么。"

            可以先从这个「[网络自由为什么重要？](./internet-freedom-matter.md){target="_blank"}」章节开始了解。

            :octicons-question-24: **补充内容**

            台湾的网络算是自由的，但我们周边邻近的国家，对于网络管控的程度有着严峻的差异。
            1. **网络自由的重要性**：网络自由是一个涉及**言论自由**、**信息流通**和**隐私权**的议题。自由的网络让人们可以不受拘束地交流思想、获取信息以及表达观点，这对民主和创新的发展至关重要。在某些国家，网络管控严格，政府可能会封锁网站、限制社交媒体，甚至监控个人流量，这不仅影响了人民的基本人权，也限制了信息的多样性与透明度。
            2. **匿名网络是什么**：匿名网络是一种让用户能在隐藏身份的情况下浏览网络的技术，以保护用户的隐私及安全。这些网络通常依赖于多层加密及路由技术，例如 Tor 洋葱路由，让用户的流量难以被追踪。匿名网络在复杂的政治环境下成为一些用户的安全港，尤其是那些想要规避审查或保护机敏信息的人。
            3. **匿名网络的优点与风险**：使用匿名网络可以保护隐私，并帮助用户绕过网络审查，到达被封锁的网站以及和更多的人交流。然而，匿名网络也被一些非法活动所利用，因此可能会引起法律机构的注意和干预。因此，用户在获得匿名性和自由的同时，必须理解和承担由此带来的风险。

        ??? question "台湾的网络自由吗？"

            你觉得台湾网络自由吗？当我们在回头思考这件事的时候，可能可以有一些比较的事件或是参考的资料。

            :octicons-question-24: **补充内容**

            1. **国际排名与报告**：根据「自由之家」（Freedom House）发布的年度报告，台湾通常被评为网络自由度高的国家之一。这份报告评估了全球各国在网络访问的开放性、言论自由以及用户权利保障等方面的表现。台湾的网民可以自由地访问大部分的国际网站，并能在网络上公开表达不同的政治观点，这在一些邻近国家可能会面临限制或风险。
            2. **事件比较**：相比之下，中国实行「防火长城」（Great Firewall）技术，全面封锁多个国际网站，如 Google、Facebook 和 Twitter/X，进行网络审查。香港在《国安法》实施后，网络自由度也受到影响，出现了部分网页被封锁的情况。这些情况使台湾的网络自由显得尤为突出。
            3. **当地事件与政策**：在台湾，虽然网络言论自由受到高度保障，但也面临着**假消息**和**网络霸凌**的挑战，政府及民间组织也在积极寻求法律和技术手段加以改善。网络监控方面，政府要求电信业者配合侦查必要时需提供用户资料，但大多数情况下，这些都受到法律制约，保障公民的隐私权。
            4. **资料参考**：根据多个国际组织的评估，台湾在网络自由指数上得分较高。这些评估基于网络审查的严重性、监控措施、言论自由以及法律制度等方面。

        ??? question "我们周遭的国家目前的网络状况。"

            这一题是开放的议题，希望可以自行动手搜索、了解台湾周围国家网络自由的状况。以下是一些指引，可以从这里出发：

            **关键词**

            1. **网络自由报告** - 了解各国在网络自由方面的排名及情况，例如搜索「Freedom House Internet Freedom Report」。
            2. **防火长城（Great Firewall）** - 中国大陆的网络审查机制。
            3. **国家安全法（National Security Law）** - 香港影响网络自由的法律。
            4. **假消息和信息操纵（Disinformation and Information Manipulation）** - 各国面临的假消息挑战。
            5. **网络中断（Internet Shutdowns）** - 与缅甸相关的事件及其对社会的影响。
            6. **网络监控法规（Internet Surveillance Laws）** - 各国的监控措施和其影响。

            **事件**

            1. **2021年缅甸军事政变** - 对该国网络自由的影响。
            2. **新加坡防止网络谣言法案（POFMA）** - 关于假信息法案及其实施效果。
            3. **泰国街头示威与王室批评** - 探讨政府对网络监控及言论自由的压制。
            4. **越南的内容封锁措施** - 包含网络用户备受控制的具体事例。

=== ":material-checkbox-marked-circle-outline: Tails: Basic L2"

    - [x] 了解如何安装、制作 Tails 操作系统随身碟。
    - [x] 了解电脑如何设置从随身碟启动。
    - [x] 了解 Mac 电脑哪些类型无法使用 Tails。
    - [x] 了解 Tails 使用情境与限制。

    !!! abstract "Tails: Basic L2"

        ??? question "了解如何安装、制作 Tails 操作系统随身碟。"

            - **下载 Tails**：前往 [Tails 官方网站](https://tails.net/){target="_blank"}，下载 Tails ISO 映像文件。
            - **准备工具**：需要一个至少 8GB 的 USB 随身碟以及 [Balena Etcher](https://etcher.balena.io/){target="_blank"} 或 [Rufus](https://rufus.ie/zh_TW/){target="_blank"} 等工具来制作启动随身碟。
            - **安装与制作**：[参阅官网](https://tails.net/install/index.en.html){target="_blank"}所提供的制作流程，选择合适的操作系统执行。

        ??? question "了解电脑如何设置从随身碟启动。"

            - **进入 BIOS/UEFI 设置**：在大多数电脑中，重新启动后会出现按键选项（如 F2、F12、Delete），按下对应的键进入 BIOS 或 UEFI 设置。
            - **调整启动顺序**：在启动菜单中，调整设置使 USB 随身碟成为主要启动设备。保存更改后，重新启动电脑，系统将自动从 USB 启动。

        ??? question "了解 Mac 电脑哪些类型无法使用 Tails。"

            - **不支持的类型**：某些新型 Mac，特别是使用 Apple T2 芯片或 Apple Silicon (M 系列芯片)，由于启动安全机制，可能无法顺利从非苹果认证的 USB 设备启动。

        ??? question "了解 Tails 使用情境与限制。"

            - **使用情境**：Tails 操作系统主要针对需要高隐私保护的人士所设计，例如记者、人权团体或任何希望匿名浏览的人。它不留痕迹地运行在内存中，关闭后不会在电脑上留下数据。
            - **限制**：
                1. **硬件兼容性**：Tails 对于某些硬件驱动程序（特别是新的无线网卡）可能支持有限。
                2. **操作**：由于 Tails 是基于 Linux 的系统、Debian 操作系统、GNOME 桌面环境，对于不熟悉 Linux 环境的人会有一些学习曲线。
                3. **永久存储**：尽管它可以建立持久性加密磁区（Persistent Storage）以保留某些数据，但它的设计初衷是不留痕迹。
                4. **更新频繁**：为了安全性，Tails 经常更新，需要确保持续更新以保护隐私。

=== ":material-checkbox-marked-circle-outline: Tails: Basic L3"

    - [x] 安装 Tails，并实际使用至少一周。
    - [x] 建立持久性加密磁区（Persistent Storage）。
    - [x] 使用 Bridge 桥接设置 Tails 网络连接方式。
    - [x] 使用 OnionShare 软件分享文件。

    !!! abstract "Tails: Basic L3"

        ??? question "安装 Tails，并实际使用至少一周。"

            - 参考之前提到的步骤，下载并制作 Tails 启动随身碟。
            - 插入 USB 随身碟，重新启动并从 USB 启动，以进入 Tails 操作系统。
            - 使用 Tails 进行一般日常的网络操作一周，这期间熟悉 Tails 的功能和设置，如 Tor 浏览、电子邮件的安全使用等。

        ??? question "建立持久性加密磁区（Persistent Storage）。"

            - 打开 Tails 后，在桌面上找到「Applications」菜单，选择「Tails」 > 「Configure persistent volume」。
            - 依照指示设置持久性加密磁区，这个区域让您可以保存一些设置文件、电子邮件等个人资料，这层磁区是通过加密保护方式确保数据安全。
            - 完成加密磁区的建立后，当您重启 Tails 时，可在登录页面时选择是否启用这个加密磁区。

        ??? question "使用 Bridge 桥接设置 Tails 网络连接方式。"

            - 登录 Tails 后，会出现连接到 Tor 的网络设置。
            - 选择设置桥接（Bridge）方式，假设你的地区封锁了直接连接至 Tor。
            - 你可以选择内建的桥接或手动输入您已获得的桥接信息以绕过封锁。

        ??? question "使用 OnionShare 软件分享文件。"

            - OnionShare 是一个可以通过 Tor 网络安全分享文件的小工具。
            - 在 Tails 的「Applications」菜单中找到并启动 OnionShare。
            - 通过拖放方式或选择文件的方式，将想要分享的文件载入 OnionShare。
            - 启动分享后，OnionShare 会生成一个 .onion 地址，您可以将这个网址提供给信任的人，他们即可使用 Tor 浏览器下载。

### :material-checkbox-marked-circle-auto-outline: Tails-Advanced

=== ":material-checkbox-marked-circle-auto-outline: Tails: Advanced L1"

    - [x] 通过 Thunderbird 建立连接 Gmail 邮箱的接收与发送（IMAP 协议）。
    - [x] 更新 Tails 到下一个最新版本。
    - [x] 了解 MAC 地址匿名化（MAC Address Anonymization）。
    - [x] 备份持久性加密磁区（Persistent Storage）。

    !!! warning ""

        :wave: 评估参考内容预计在 2025/Q3 完成 Advanced 部分。

=== ":material-checkbox-marked-circle-auto-outline: Tails: Advanced L2"

    - [x] 使用密码管理器 KeePassXC。
    - [x] 使用 GnuPG 与 Kleopatra 建立加密密钥与加密文件。
    - [x] 通过 Thunderbird 发送加密邮件到 `ooni-research@ocf.tw`（取得公开密钥请参考「[持续关注](./contact.md)」）。
    - [x] 安全的移除文件操作流程。

    !!! warning ""

        :wave: 评估参考内容预计在 2025/Q3 完成 Advanced 部分。

## OONI 技能分级表

### :material-checkbox-marked-circle-auto-outline: OONI-Basic

=== ":material-checkbox-marked-circle-outline: OONI: Basic L1"

    - [x] 了解 OONI 是什么。
    - [x] 了解网络监视（surveillance）与网络审查（censorship）是什么。
    - [x] OONI 检测的运作方式。
    - [x] 台湾与其他国家在网络监视与网络审查的差异。

    !!! abstract "OONI: Basic L1"

        ??? question "了解 OONI 是什么"

            可以先从这个「[什么是 OONI？](./what-is-ooni.md){target="_blank"}」章节开始了解。

        ??? question "了解网络监视（surveillance）与网络审查（censorship）是什么。"

            - **网络监视（surveillance）**：指政府、组织或个人监看和记录用户的网络活动，如电子邮件、搜索历史、网站浏览及通话的过程。监视通常会牵涉到使用监控技术，如数据包检测，以获得特定的网络流量信息。
            - **网络审查（censorship）**：指限制或控制用户对互联网某些信息的访问。这可能包括封锁网站、过滤内容或禁止某些关键词搜索等。审查往往是由政府实施，但也可能由企业或其他机构施行。

        ??? question "OONI 检测的运作方式。"

            - OONI 提供了免费的开源测试工具 OONI Probe，用户可以在自己的网络环境执行这些测试来检测他们的网络是否被审查。
            - OONI Probe 测试会定期发送请求至多个网站和服务，确认在[名单上](./ooni-weblists.md){target="_blank"}的网站、服务是否可以正常访问。
            - 测试结果会**匿名上传**到 OONI 的数据服务器中，并于 [OONI Explorer](https://explorer.ooni.org/zh-CN){target="_blank"} 上公开，供研究者和公众使用，以促进对网络自由的理解。

        ??? question "台湾与其他国家在网络监视与网络审查的差异。"

            - **台湾**：台湾的网络环境相对自由，政府并未大规模实施网络审查或监控。用户可自由浏览互联网的各种内容，政府对于个人隐私权的保护也相对重视。
            - **其他国家**：例如，中国大陆执行严格的网络封锁和审查政策，通常被称为「防火长城」（Great Firewall），限制访问许多外国网站和服务。北韩等国则对网络访问进行更极端的限制，仅允许极少数精选内容。其他一些国家，如俄罗斯和伊朗，也进行不同程度的网络监控和网站封锁。
            - 可以参考「[网络自由为什么重要？](./internet-freedom-matter.md){target="_blank"}」章节。

=== ":material-checkbox-marked-circle-outline: OONI: Basic L2"

    - [x] 安装并使用 OONI Probe 产生检测报告。
    - [x] 了解是否可以使用 VPN 方式使用 OONI Probe 检测。
    - [x] 了解 OONI Probe 使用时的风险。
    - [x] 了解 ASN 自治网络的运作。

    !!! abstract "OONI: Basic L2"

        ??? question "安装并使用 OONI Probe 产生检测报告"

            - **安装 OONI Probe**：通过 OONI 官方网站[下载](https://ooni.org/install/){target="_blank"} OONI Probe 应用程序。
            - **使用 OONI Probe**：
                - 启动应用程序后，您可以选择要进行的测试类型，例如测试网站封锁、即时通讯程序的连通性、或中间盒（middleboxes）的干扰。
                - 点击开始测试后，OONI Probe 会自动执行检测并生成结果。
                - 结果会上传至 OONI 的服务器，并显示在您的应用程序中，也可以在 OONI Explorer 网站上查看更详细的报告。

        ??? question "了解是否可以使用 VPN 方式使用 OONI Probe 检测"

            - 不建议使用 VPN 进行 OONI Probe 测试，因为 VPN 会改变您的流量路径和 IP 地址，这可能导致检测到被改变的网络环境，而非您实际所在的网络中的审查或干扰。
            - 目的在于**测试本地网络**的审查情形，应该在不使用 VPN 的情况下进行，才能准确测量真实的网络状况。

        ??? question "了解 OONI Probe 使用时的风险"

            - 使用 OONI Probe 进行检测可能会引起您所在网络管理员的注意，尤其在网络审查较严格的国家。因此，应了解所在区域的网络政策，衡量使用 OONI Probe 所可能带来的风险。
            - 在进行测试时，OONI Probe 会访问不同的网站、服务，这可能会触发网络监控系统的观察与记录。

        ??? question "了解 ASN 自治网络的运作"

            - ASN 是用于识别自治网络（AS）的唯一标识码。
            - 自治网络是一或多个 IP 区块的集合，并由一个或多个网络服务提供商（ISP）或大型企业单位间进行的路由。每个 AS 通过 ASN 在互联网上相互通信，以便实现路由信息和 IP 数据包的交换。ASN 系统机制让全球互联网更有效率地运作，并确保不同网络之间的流量能够正确到达目标地。可以参考「[ASNs 自治网络观测数据分析](./ooni-asns-coverage.md){target="_blank"}」中第一段的介绍。

=== ":material-checkbox-marked-circle-outline:OONI: Basic L3"

    - [x] 通过 OONI Explorer 整理台湾近半年的观测数据。
    - [x] 通过 OONI Explorer 比较三个国家的观测数据。
    - [x] 查看当前网络封锁的报告。
    - [x] 创建 OONI Run 检测链接并找到该链接的线上报告内容。

    !!! abstract "OONI: Basic L3"

        ??? question "通过 OONI Explorer 整理台湾近半年的观测数据。"

            - 前往 [OONI Explorer](https://explorer.ooni.org/zh-CN/){target="_blank"} 网站。
            - 在国家栏中找到「台湾」作为观测地点。
            - 使用日期范围选择功能，设置为过去六个月的时间范围。
            - 查看不同类型的测试结果，例如网站封锁、即时通讯应用程序的连接情况等。
            - 您可以下载或记录这段期间出现的相关数据和事件，以进行进一步分析。

        ??? question "通过 OONI Explorer 比较三个国家的观测数据"

            - 在 OONI Explorer 页面上，纵轴（Rows）选择「国家」，使用过滤器（Filters）分别选择您需要比较的三个国家。（[参考设置](https://explorer.ooni.org/zh-CN/chart/mat?test_name=web_connectivity&axis_x=measurement_start_day&since=2025-05-01&until=2025-05-30&time_grain=day&axis_y=probe_cc){target="_blank"}）
            - 查看这些国家在不同种类测试中的结果差异，包括网站封锁、中间人攻击检测等。
            - 导出 CSV 数据比较数据。

        ??? question "查看当前网络封锁的报告。"

            - 在 OONI Explorer 首页中，通常会有关于全球网络审查和封锁的最新报告和趋势。
            - 浏览「[搜索](https://explorer.ooni.org/zh-CN/search){target="_blank"}」或搜索特定服务和网站以查看它们当前连通性状况。
            - 可以查看「[网络审查](https://explorer.ooni.org/zh-CN/social-media){target="_blank"}」下不同的测试类型，例如：社交网站、新闻媒体等。

        ??? question "创建 OONI Run 检测链接并找到该链接的线上报告内容。"

            - 在 [OONI Run](https://run.ooni.org/){target="_blank"} 页面上提供电子邮件获取登录链接。
            - 通过链接登录后，根据表单上的必填项目完成填写。
            - 在「Add URL+」项目中新增要检测的网站网址。完成后按下「Create Link」完成创建。
            - 分享网址或点击网址后、依引导开启 OONI Probe 开始检测。（[参考检测](https://run.ooni.org/v2/10182){target="_blank"}）
            - 网址后方 `https://run.ooni.org/v2/10182` 的数字 `10182` 即为 OONI Run Link ID，可以在 OONI Explorer 直接输入 ID 找到检测结果。（[参考结果](https://explorer.ooni.org/search?since=2025-04-29&until=2026-07-01&failure=false&ooni_run_link_id=10182){target="_blank"}）

### :material-checkbox-marked-circle-auto-outline: OONI-Advanced

=== ":material-checkbox-marked-circle-auto-outline: OONI: Advanced L1"

    - [x] 使用命令行的方式启动 OONI Probe。
    - [x] 了解网站观测名单收录方式。

    !!! warning ""
        :wave: 评估参考内容预计在 2025/Q3 完成 Advanced 部分。

=== ":material-checkbox-marked-circle-auto-outline: OONI: Advanced L2"

    - [x] 通过原始观测数据（Raw Data）进行数据整理与分析。
    - [x] 协助名单整理与修正。

    !!! warning ""

        :wave: 评估参考内容预计在 2025/Q3 完成 Advanced 部分。
