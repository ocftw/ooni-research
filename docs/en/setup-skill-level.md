---
title: Self-Skills Evaluation Form
icon: octicons/paste-24
---

# :octicons-paste-24: Self-Skills Evaluation Form

Here is a self-evaluation scale to help quickly assess your understanding of Tor, Tails, and OONI. If you're unsure where to start learning, you can use this evaluation form as a guide for your studies.

## Tor Skills Grading Chart

### :material-checkbox-marked-circle-auto-outline: Tor-Basic

=== ":material-checkbox-marked-circle-outline: Tor: Basic L1"

    - [x] Understand what Tor is.
    - [x] Understand why internet freedom is important, and what anonymous networks are.
    - [x] Is the internet in Taiwan free?
    - [x] Current internet conditions in neighboring countries.

    !!! abstract "Tor: Basic L1"

        ??? question "Understand what Tor is."

            You can start by exploring the "[What is Tor?](https://support.torproject.org/about/what-is-tor/){target="_blank"}" section to gain an understanding.

            Tor typically refers to "The Onion Router," which relays network connections randomly through three nodes. The "Tor Browser" is designed by the Tor team using the open-source browser Firefox to facilitate accessing websites ending in .onion via the onion network.

            :octicons-question-24: **Additional Information**

            1. **Background of Tor**: Tor was originally developed by the U.S. Naval Research Laboratory with the aim of protecting government communications. It was later made available to the public to support freedom of speech and privacy protection.
            2. **How it works**: Tor's name derives from its routing technique—The Onion Router. It encrypts your internet traffic and relays it through multiple nodes, making it difficult to trace.
            3. **Privacy and security advantages**: Using Tor can prevent network monitoring and traffic analysis, serving as a vital tool for privacy protection. Consequently, Tor can circumvent geo-blocking and internet censorship, allowing for freer exploration of information online.
            4. **Disadvantages and limitations**: While Tor offers strong privacy protection, its speed is usually slower than traditional internet connections due to the multiple layers of encryption and nodes. Using Tor does not guarantee complete anonymity; users may still be identifiable if they inadvertently reveal personal information or log into service accounts.
            5. **Legal and ethical considerations**: In some countries or regions, using Tor may be considered illegal or inappropriate, and users should understand local laws to avoid legal issues. There are also illegal activities on the onion network, so users should remain vigilant when browsing.
            6. **Usage tips**: When using Tor, avoid enabling unnecessary plugins, scripts, or downloading untrusted content, as these actions may reveal your real IP address or expose you to security risks.

        ??? question "Understand why internet freedom is important, and what anonymous networks are."

            You can begin by exploring the "[Why Internet Freedom Matters?](./internet-freedom-matter.md){target="_blank"}" section to gain an understanding.

            :octicons-question-24: **Additional Information**

            Taiwan's internet is generally free, but there are severe differences in the level of internet control in the neighboring countries.

            1. **The Importance of Internet Freedom**: Internet freedom involves issues of **freedom of speech**, **information flow**, and **privacy rights**. A free internet allows people to exchange ideas, access information, and express opinions without restrictions, which is crucial for democratic and innovative development. In some countries, strict internet control may lead governments to block websites, restrict social media, and monitor personal traffic, affecting not only basic human rights but also limiting informational diversity and transparency.
            2. **What is an Anonymous Network**: An anonymous network is a technology that allows users to browse the internet while hiding their identities to protect their privacy and security. These networks typically rely on multi-layer encryption and routing technologies, such as Tor's Onion Routing, making users' traffic difficult to trace. Anonymous networks can serve as a safe haven for users in complex political environments, particularly those wishing to circumvent censorship or protect sensitive information.
            3. **Advantages and Risks of Anonymous Networks**: Using an anonymous network can protect privacy and help users bypass internet censorship, access blocked websites, and communicate with a broader audience. However, anonymous networks are also used for some illegal activities, which may attract the attention and intervention of legal authorities. Thus, while gaining anonymity and freedom, users must understand and bear the associated risks.

        ??? question "Is the internet in Taiwan free?"

            Do you think the internet in Taiwan is free? As we reflect on this, we might consider comparative events or reference materials.

            :octicons-question-24: **Additional Information**

            1. **International Rankings and Reports**: According to the annual reports from "Freedom House," Taiwan is generally rated as one of the countries with high internet freedom. This report evaluates global countries on openness of internet access, freedom of speech, and user rights protection. Taiwanese netizens can freely access most international websites and express diverse political viewpoints online, which might face restrictions or risks in some neighboring countries.
            2. **Comparative Events**: In contrast, China employs the "Great Firewall" technology to comprehensively block various international sites like Google, Facebook, and Twitter/X, conducting internet censorship. Since the implementation of the National Security Law, Hong Kong's internet freedom has also been affected, with some websites being blocked. These situations highlight Taiwan's prominence in internet freedom.
            3. **Local Events and Policies**: In Taiwan, while internet freedom of speech is highly secured, challenges such as **fake news** and **cyberbullying** remain, pushing the government and civil organizations to actively seek legal and technical improvements. Regarding internet surveillance, the government may require telecommunications providers to cooperate by providing user information when necessary for investigations, but most of these actions are legally constrained to protect citizens' privacy rights.
            4. **Reference Data**: According to evaluations by multiple international organizations, Taiwan scores high on internet freedom indices. These evaluations are based on the severity of internet censorship, surveillance measures, freedom of speech, and the legal system.

        ??? question "Current internet conditions in neighboring countries."

            This is an open topic, and it is encouraged that you research and understand the state of internet freedom in the countries surrounding Taiwan. Here are some guidelines to get you started:

            **Keywords**

            1. **Internet Freedom Reports** - Learn about the ranking and status of various countries in terms of internet freedom, for example by searching for the "Freedom House Internet Freedom Report."
            2. **Great Firewall** - China's internet censorship mechanism.
            3. **National Security Law** - The law affecting internet freedom in Hong Kong.
            4. **Disinformation and Information Manipulation** - The challenges of misinformation faced by different countries.
            5. **Internet Shutdowns** - Events related to Myanmar and their impact on society.
            6. **Internet Surveillance Laws** - The surveillance measures of different countries and their effects.

            **Events**

            1. **2021 Myanmar Military Coup** - Its impact on internet freedom in the country.
            2. **Singapore's Protection from Online Falsehoods and Manipulation Act (POFMA)** - About the misinformation act and its implementation effects.
            3. **Thailand's Street Protests and Royal Criticism** - Exploring the government's suppression of internet surveillance and freedom of speech.
            4. **Vietnam's Content Blocking Measures** - Specific instances where internet users face heavy control.

=== ":material-checkbox-marked-circle-outline: Tor: Basic L2"

    - [x] Understand how Tor browser connects.
    - [x] Types of Tor bridges: Bridge, Snowflake, WebTunnel.
    - [x] Use cases and timing for each connection.
    - [x] Can you connect to Tor via VPN?

    !!! abstract "Tor: Basic L2"

        ??? question "Understand how Tor browser connects."

            The "[Tor Browser](https://www.torproject.org/zh-TW/download/){target="_blank"}" is designed by the Tor team using the open-source [Firefox ESR](https://www.mozilla.org/zh-TW/firefox/enterprise/){target="_blank"}, a long-term support version, tailored for the onion network to facilitate accessing websites ending in .onion. Currently, both [Brave](https://brave.com/zh-tw/){target="_blank"} and [Mullvad](https://mullvad.net/zh-hant/browser){target="_blank"} browsers can be used to connect to .onion websites.

            The Tor Browser is similar to regular browsers but emphasizes **privacy protection** and effectively blocks **ad tracking**. When connecting to regular websites (non-.onion URLs), data is randomly transmitted through three Tor relays. For .onion websites, a connection enters the .onion network after the third relay.

            :octicons-question-24: **Additional Information**

            1. **Anonymous Browsing**: The Tor Browser is primarily designed to protect user privacy. When you browse the internet with Tor, your traffic passes through a series of randomly selected relay servers, undergoing multiple layers of encryption and routing. This ensures that any entity trying to track the origin can only see the IPs of virtual relays, not your actual IP address. Thus, Tor effectively prevents websites and service providers from logging or tracking your IP address and browsing behavior, enhancing user anonymity.
            2. **Circumventing Censorship**: In some countries or regions, governments may enforce internet censorship, restricting user access to certain websites or services. The Tor Browser helps users bypass these blocks since its traffic is relayed through servers in multiple countries, complicating recognition and blocking by surveillance and filtering systems. This allows users to freely access content banned by local network administrators or governments, enjoying a more liberated internet environment.
            3. **Security Protection**: Tor Browser uses multi-layer encryption technology and onion routing to enhance network security, particularly when using public Wi-Fi or other insecure network environments. Each layer of transmission is encrypted, only decrypted upon entering and exiting the Tor network. Each relay server only sees incoming and outgoing data to the directly adjacent servers, preventing knowledge of the full transmission path or final destination. This effectively reduces the risk of man-in-the-middle attacks while protecting user data from theft or tampering.
            4. **Temporary Access**: One-time usage design of the Tor Browser ensures that user privacy is thoroughly protected after each session. When you close the Tor Browser, all browsing history, cookies, login information, and other temporary cache data are automatically cleared, preventing others from viewing your browsing activity and safeguarding personal data against unauthorized access.
            5. **Open Source**: Tor's open-source nature means its code is publicly available, allowing developers and security experts to review and fix potential vulnerabilities, enhancing overall security. Open-source community collaboration enables Tor to be continuously updated, addressing emerging security threats and attracting developers worldwide to cooperate, contributing to the enhancement of privacy protection.

        ??? question "Types of Tor bridges: Bridge, Snowflake, WebTunnel."

            In the Tor network, bridge servers exist to help users facing internet censorship or blocks connect to Tor. Below are different types of Tor Bridges:

            1. **Bridge**: This is the most basic type of Tor bridge. Bridges serve as secret entry points not listed on the public Tor network, making them harder to block. Users can manually obtain these bridges to connect to the Tor network and bypass common blocking measures. (Refer to how to obtain a [Tor Bridge](https://bridges.torproject.org/){target="_blank"})
            2. **Snowflake**: This type of bridge is specifically designed to counter high-intensity internet censorship. Snowflake employs the WebRTC protocol, allowing volunteers to use their browsers as temporary Tor entry points. Due to its dynamic nature, it is more challenging to block. This bridge can automatically connect and offer more random entry points, further enhancing connectivity reliability. (Refer to how to install [Snowflake](https://snowflake.torproject.org/){target="_blank"})
            3. **WebTunnel**: This is a newer technology designed to tackle more complex blocking strategies. WebTunnel uses HTTPS servers as entry points to mitigate the issue of traditional bridges being blocked. Since it uses the HTTPS protocol, WebTunnel traffic is difficult to distinguish and block, thereby increasing the chances of bypassing censorship. (Refer to how to set up a [WebTunnel](https://community.torproject.org/relay/setup/webtunnel/){target="_blank"})

        ??? question "Use cases and timing for each connection."

            1. **Bridge**:
                  - **Use Case**: You are in an environment with basic Tor blocking, such as certain schools, workplaces, or internet cafes that restrict access to Tor.
                  - **When to Use**: Suitable for situations requiring simple circumvention of mild blocking. You can first attempt a basic Bridge, which is usually sufficient to bypass most IP-based blockings. You can obtain the latest bridge host list from the official Tor website or other sources.
            2. **Snowflake**:
                  - **Use Case**: Facing severe censorship in countries like China and Iran, where deep packet inspection (DPI) and IP blocking are commonly used to prevent Tor traffic.
                  - **When to Use**: When Bridges are unable to bypass censorship or when you need a more randomized connection to avoid detection and blocking, Snowflake is a better choice. Snowflake utilizes WebRTC (a technology that enables browsers and devices to connect directly without a middle server) for more randomized and decentralized connections, supported by global volunteers, thereby improving the connection success rate.
            3. **WebTunnel**:
                  - **Use Case**: When your network not only blocks Tor entries but also has advanced traffic monitoring mechanisms capable of quickly identifying and blocking Snowflake.
                  - **When to Use**: When encountering extreme blocking strategies and other bridge types fail, try WebTunnel. Its HTTPS disguise can more effectively hide Tor traffic within regular internet traffic, such as accessing HTTPS websites, making it difficult to distinguish and block.

        ??? question "Can you connect to Tor via VPN?"

            Connecting to Tor through a VPN is a common practice, known as either "VPN-over-Tor" or "Tor-over-VPN," and there are differences between the two:

            1. **VPN-over-Tor**: This method involves first connecting to the Tor network and then using a VPN service through Tor. This configuration is less common as it requires the VPN provider to support connections through the Tor network, and it might not offer additional protection for your IP address.
            2. **Tor-over-VPN**: This is the more commonly used approach. You first connect to a VPN, and then connect to Tor from the VPN. This method has several advantages for enhancing privacy and security:
                  - Your original IP address is hidden behind the VPN server, preventing ISPs (Internet Service Providers) from seeing that you are using Tor.
                  - The VPN connection can help bypass blocks on Tor network entries, especially in certain countries or network environments where Tor entry nodes are blocked.

=== ":material-checkbox-marked-circle-outline: Tor: Basic L3"

    - [x] Install the Tor browser and use it for at least one week.
    - [x] Connect to the Tor network via **direct connection** and **bridge connection**.
    - [x] Operate switching current connection paths.
    - [x] Connect to **.onion** domain.

    !!! abstract "Tor: Basic L3"

        ??? question "Install the Tor browser and use it for at least one week."

            1. Visit the [Tor Project official website](https://www.torproject.org/){target="_blank"} to download the Tor Browser suitable for your operating system.
            2. Once the download is complete, follow the instructions to install and launch the Tor Browser.
            3. Use the Tor Browser for daily web browsing throughout the week to familiarize yourself with its interface and features. Pay special attention to anonymity and security while using it. Also, note any inconveniences you encounter and explore possible solutions.

        ??? question "Connect to the Tor network via **direct connection** and **bridge connection**."

            1. When you launch the Tor Browser, you will usually see the browser establishing a connection.
            2. Enter the URL to browse directly through the Tor network. This method is best suited for countries that do not block the Tor network.
            3. You can click on the first icon (similar to :material-map-marker-path:) located to the left of the address bar to view the current route and connection method.
            4. If your network blocks Tor, go to "Settings," then "Connection," and select "Bridges." You can choose from built-in bridge types or enter bridge information that you have obtained from other sources.

        ??? question "Operate switching current connection paths."

            1. You can click on the first icon (a Tor Circuit icon, similar to :material-map-marker-path:) to the left of the address bar to view the current route and connection method.
            2. Click on the last line "New Tor circuit for this site" to have the Tor Browser re-establish the connection path. This is useful when the exit node is being blocked by the website, allowing you to attempt connecting through different countries.

        ??? question "Connect to **.onion** domain."

            1. Connect to the [project website](https://anoni.net/docs/en/){target="_blank"}. Notice a purple button saying ".onion available" that appears at the end of the address bar. Clicking it will redirect you to the .onion domain, indicating that the site actively provides guidance to connect to its .onion domain.
            2. DuckDuckGo also offers a .onion service: [https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/](https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion/){target="_blank"}

### :material-checkbox-marked-circle-auto-outline: Tor-Advanced

=== ":material-checkbox-marked-circle-auto-outline: Tor: Advanced L1"

    - [x] Clearly understand what Tor, Onion, and Tor Browser each refer to in terms of technology.
    - [x] Use the Snowflake browser add-on to set up a Tor bridge.
    - [x] Start Tor and connect via SOCKS v5.
    - [x] Use [metrics.torproject.org](https://metrics.torproject.org){target="_blank"} to query relays in Taiwan.

    !!! warning ""

        :wave: The assessment reference material for the Advanced section is expected to be completed by 2025/Q3.

=== ":material-checkbox-marked-circle-auto-outline: Tor: Advanced L2"

    - [x] Establish a Tor Relay.
    - [x] Set up a Tor Bridge.
    - [x] Create a WebTunnel relay.
    - [x] Build a **.onion** website.

    !!! warning ""

        :wave: The assessment reference material for the Advanced section is expected to be completed by 2025/Q3.

## Tails Skills Grading Chart

### :material-checkbox-marked-circle-auto-outline: Tails-Basic

=== ":material-checkbox-marked-circle-outline: Tails: Basic L1"

    - [x] Understand what Tails is and how it works.
    - [x] Understand why internet freedom is important, and what anonymous networks are.
    - [x] Is the internet in Taiwan free?
    - [x] Current internet conditions in neighboring countries.

    !!! abstract "Tails: Basic L1"

        ??? question "Understand what Tails is and how it works."

            You can start by exploring the "[What is Tails?](https://tails.net/){target="_blank"}" section to gain an understanding.

        ??? question "Understand why internet freedom is important, and what anonymous networks are."

            You can begin by exploring the "[Why Internet Freedom Matters?](./internet-freedom-matter.md){target="_blank"}" section to gain an understanding.

            :octicons-question-24: **Additional Information**

            Taiwan's internet is generally free, but there are severe differences in the level of internet control in the neighboring countries.

            1. **The Importance of Internet Freedom**: Internet freedom involves issues of **freedom of speech**, **information flow**, and **privacy rights**. A free internet allows people to exchange ideas, access information, and express opinions without restrictions, which is crucial for democratic and innovative development. In some countries, strict internet control may lead governments to block websites, restrict social media, and monitor personal traffic, affecting not only basic human rights but also limiting informational diversity and transparency.
            2. **What is an Anonymous Network**: An anonymous network is a technology that allows users to browse the internet while hiding their identities to protect their privacy and security. These networks typically rely on multi-layer encryption and routing technologies, such as the Tor Onion Routing, making users' traffic difficult to trace. Anonymous networks can serve as a safe haven for users in complex political environments, particularly those wishing to circumvent censorship or protect sensitive information.
            3. **Advantages and Risks of Anonymous Networks**: Using an anonymous network can protect privacy and help users bypass internet censorship, access blocked websites, and communicate with a broader audience. However, anonymous networks are also used for some illegal activities, which may attract the attention and intervention of legal authorities. Thus, while gaining anonymity and freedom, users must understand and bear the associated risks.

        ??? question "Is the internet in Taiwan free?"

            Do you think the internet in Taiwan is free? As we reflect on this, we might consider comparative events or reference materials.

            :octicons-question-24: **Additional Information**

            1. **International Rankings and Reports**: According to the annual reports from "Freedom House," Taiwan is generally rated as one of the countries with high internet freedom. This report evaluates global countries on openness of internet access, freedom of speech, and user rights protection. Taiwanese netizens can freely access most international websites and express diverse political viewpoints online, which might face restrictions or risks in some neighboring countries.
            2. **Comparative Events**: In contrast, China employs the "Great Firewall" technology to comprehensively block various international sites like Google, Facebook, and Twitter/X, conducting internet censorship. Since the implementation of the National Security Law, Hong Kong's internet freedom has also been affected, with some websites being blocked. These situations highlight Taiwan's prominence in internet freedom.
            3. **Local Events and Policies**: In Taiwan, while internet freedom of speech is highly secured, challenges such as **fake news** and **cyberbullying** remain, pushing the government and civil organizations to actively seek legal and technical improvements. Regarding internet surveillance, the government may require telecommunications providers to cooperate by providing user information when necessary for investigations, but most of these actions are legally constrained to protect citizens' privacy rights.
            4. **Reference Data**: According to evaluations by multiple international organizations, Taiwan scores high on internet freedom indices. These evaluations are based on the severity of internet censorship, surveillance measures, freedom of speech, and the legal system.

        ??? question "Current internet conditions in neighboring countries."

            This is an open topic, and it is encouraged that you research and understand the state of internet freedom in the countries surrounding Taiwan. Here are some guidelines to get you started:

            **Keywords**

            1. **Internet Freedom Reports** - Learn about the ranking and status of various countries in terms of internet freedom, for example by searching for the "Freedom House Internet Freedom Report."
            2. **Great Firewall** - China's internet censorship mechanism.
            3. **National Security Law** - The law affecting internet freedom in Hong Kong.
            4. **Disinformation and Information Manipulation** - The challenges of misinformation faced by different countries.
            5. **Internet Shutdowns** - Events related to Myanmar and their impact on society.
            6. **Internet Surveillance Laws** - The surveillance measures of different countries and their effects.

            **Events**

            1. **2021 Myanmar Military Coup** - Its impact on internet freedom in the country.
            2. **Singapore's Protection from Online Falsehoods and Manipulation Act (POFMA)** - About the misinformation act and its implementation effects.
            3. **Thailand's Street Protests and Royal Criticism** - Exploring the government's suppression of internet surveillance and freedom of speech.
            4. **Vietnam's Content Blocking Measures** - Specific instances where internet users face heavy control.

=== ":material-checkbox-marked-circle-outline: Tails: Basic L2"

    - [x] Understand how to install, make a Tails USB system.
    - [x] Know how to set a computer to boot from USB.
    - [x] Which types of Mac computers cannot use Tails.
    - [x] Usage scenarios and limitations of Tails.

    !!! abstract "Tails: Basic L2"

        ??? question "Understand how to install, make a Tails USB system."

            - **Download Tails**: Visit the [Tails official website](https://tails.net/){target="_blank"} to download the Tails ISO image.
            - **Prepare Tools**: You will need a USB flash drive with at least 8GB of space and a tool like [Balena Etcher](https://etcher.balena.io/){target="_blank"} or [Rufus](https://rufus.ie/){target="_blank"} to create a bootable USB drive.
            - **Installation and Creation**: [Refer to the official website](https://tails.net/install/index.en.html){target="_blank"} for the creation process and choose the appropriate operating system to execute it.

        ??? question "Know how to set a computer to boot from USB."

            - **Enter BIOS/UEFI Settings**: On most computers, after restarting, you will see key options (such as F2, F12, Delete). Press the corresponding key to enter BIOS or UEFI settings.
            - **Adjust Boot Order**: In the boot menu, adjust the settings to make the USB flash drive the primary boot device. Save the changes and restart the computer. The system will automatically boot from the USB.

        ??? question "Which types of Mac computers cannot use Tails."

            - **Unsupported Types**: Certain newer Mac models, particularly those using the Apple T2 chip or Apple Silicon (M series chips), may have boot security mechanisms that prevent them from booting from non-Apple certified USB devices.

        ??? question "Usage scenarios and limitations of Tails."

            - **Use Case**: The Tails operating system is primarily designed for individuals needing high privacy protection, such as journalists, human rights organizations, or anyone wanting to browse anonymously. It runs without a trace in memory and leaves no data on the computer after shutdown.
            - **Limitations**:
                1. **Hardware Compatibility**: Tails might have limited support for some hardware drivers, particularly new wireless network cards.
                2. **Operation**: Since Tails is based on a Linux system, specifically Debian OS with a GNOME desktop environment, there is a learning curve for users unfamiliar with Linux environments.
                3. **Permanent Storage**: Although it can create a Persistent Storage encrypted partition to retain certain data, it is designed to leave no trace.
                4. **Frequent Updates**: For security reasons, Tails updates often. It is necessary to keep it continuously updated to protect your privacy.

=== ":material-checkbox-marked-circle-outline: Tails: Basic L3"

    - [x] Install Tails, and use it for at least one week.
    - [x] Establish persistent storage.
    - [x] Use Bridge configuration for Tails network connection.
    - [x] Share files using OnionShare.

    !!! abstract "Tails: Basic L3"

        ??? question "Install Tails, and use it for at least one week."

            - Follow the previously mentioned steps to download and create a bootable Tails USB drive.
            - Insert the USB flash drive, restart the computer, and boot from the USB to enter the Tails operating system.
            - Use Tails for regular daily internet activities for one week. During this time, familiarize yourself with Tails' features and settings, such as Tor browsing and secure email usage.

        ??? question "Establish persistent storage."

            - After launching Tails, find the "Applications" menu on the desktop and select "Tails" > "Configure persistent volume."
            - Follow the instructions to set up the persistent encrypted storage. This area allows you to save settings files, emails, and other personal data, with encryption ensuring the security of your data.
            - Once the encrypted storage is created, you can choose to enable it at the login screen when you restart Tails.

        ??? question "Use Bridge configuration for Tails network connection."

            - After logging into Tails, a network configuration for connecting to Tor will appear.
            - Choose to configure a bridge if your region blocks direct connections to Tor.
            - You can select from the built-in bridges or manually enter bridge information you have obtained to bypass the block.

        ??? question "Share files using OnionShare."

            - OnionShare is a tool for securely sharing files through the Tor network.
            - Find and launch OnionShare in the "Applications" menu within Tails.
            - Load files you want to share into OnionShare by dragging and dropping them, or by selecting the files.
            - After starting the share, OnionShare will generate a .onion address that you can share with trusted individuals. They can then use the Tor Browser to download the files.

### :material-checkbox-marked-circle-auto-outline: Tails-Advanced

=== ":material-checkbox-marked-circle-auto-outline: Tails: Advanced L1"

    - [x] Use Thunderbird to set up reception and sending for a Gmail account (IMAP protocol).
    - [x] Update Tails to the latest version.
    - [x] Understand MAC address anonymization.
    - [x] Backup persistent storage.

    !!! warning ""

        :wave: The assessment reference material for the Advanced section is expected to be completed by 2025/Q3.

=== ":material-checkbox-marked-circle-auto-outline: Tails: Advanced L2"

    - [x] Use the KeePassXC password manager.
    - [x] Create encryption keys and encrypt files using GnuPG and Kleopatra.
    - [x] Send encrypted mail to `ooni-research@ocf.tw` via Thunderbird (refer to [Stay Updated](./contact.md) for public keys).
    - [x] Secure file deletion procedures.

    !!! warning ""

        :wave: The assessment reference material for the Advanced section is expected to be completed by 2025/Q3.

## OONI Skills Grading Chart

### :material-checkbox-marked-circle-auto-outline: OONI-Basic

=== ":material-checkbox-marked-circle-outline: OONI: Basic L1"

    - [x] Understand what OONI is.
    - [x] Understand what network surveillance and censorship are.
    - [x] How OONI tests operate.
    - [x] Differences in network surveillance and censorship between Taiwan and other countries.

    !!! abstract "OONI: Basic L1"

        ??? question "Understand what OONI is."

            You can start by exploring the "[What is OONI?](./what-is-ooni.md){target="_blank"}" section to gain an understanding.

        ??? question "Understand what network surveillance and censorship are."

            - **Internet Surveillance**: Refers to the monitoring and recording of users' online activities by governments, organizations, or individuals, such as emails, search history, website browsing, and communications. Surveillance often involves the use of monitoring technologies, like data packet inspection, to obtain specific internet traffic information.
            - **Internet Censorship**: Refers to the restriction or control of users' access to certain information on the internet. This can include blocking websites, filtering content, or prohibiting certain keyword searches. Censorship is often implemented by governments but can also be enacted by corporations or other organizations.

        ??? question "How OONI tests operate."

            - OONI provides a free open-source testing tool called OONI Probe, which allows users to run tests in their own network environments to detect if their network is being censored.
            - OONI Probe tests systematically send requests to various websites and services to check if the sites and services listed on the [web list](./ooni-weblists.md){target="_blank"} can be accessed normally.
            - The test results are **anonymously uploaded** to OONI's data servers and made publicly available on [OONI Explorer](https://explorer.ooni.org/){target="_blank"} for researchers and the public, facilitating a better understanding of internet freedom.

        ??? question "Differences in network surveillance and censorship between Taiwan and other countries."

            - **Taiwan**: Taiwan's internet environment is relatively free, with the government not implementing widespread internet censorship or surveillance. Users are free to browse a wide range of content on the internet, and the government places a relatively strong emphasis on protecting individual privacy rights.
            - **Other Countries**: For example, Mainland China enforces strict internet blocking and censorship policies, often referred to as the "Great Firewall," which restricts access to many foreign websites and services. Countries like North Korea impose more extreme restrictions on internet access, allowing only a very limited selection of content. Other countries, such as Russia and Iran, also engage in varying degrees of internet surveillance and website blocking.
            - You can refer to the section "[Why Internet Freedom Matters?](./internet-freedom-matter.md){target="_blank"}" for more information.

=== ":material-checkbox-marked-circle-outline: OONI: Basic L2"

    - [x] Install and use OONI Probe to generate test reports.
    - [x] Can you use OONI Probe with VPN?
    - [x] Risks of using OONI Probe.
    - [x] How ASN Autonomous Networks work.

    !!! abstract "OONI: Basic L2"

        ??? question "Install and use OONI Probe to generate test reports."

            - **Install OONI Probe**: Download the OONI Probe application through the [OONI official website](https://ooni.org/install/){target="_blank"}.
            - **Using OONI Probe**:
                - After launching the application, you can choose the type of test you want to run, such as testing website blocking, connectivity of instant messaging apps, or interference from middleboxes.
                - Once you tap to start the test, OONI Probe will automatically perform the detection and generate results.
                - The results are uploaded to OONI's servers and displayed in your application, and you can also view more detailed reports on the OONI Explorer website.

        ??? question "Can you use OONI Probe with VPN?"

            - It is not recommended to use a VPN with OONI Probe tests, as a VPN will alter your traffic path and IP address, potentially resulting in detection of a changed network environment rather than any censorship or interference that might exist in your actual network.
            - The goal is to **test the local network** for censorship conditions, so tests should be conducted without a VPN to accurately measure the true network situation.

        ??? question "Risks of using OONI Probe."

            - Using OONI Probe for testing can attract the attention of network administrators, especially in countries with strict internet censorship. Therefore, it's important to be aware of the local internet policies and assess the potential risks of using OONI Probe.
            - During testing, OONI Probe will access various websites and services, which could trigger observation and logging by network monitoring systems.

        ??? question "How ASN Autonomous Networks work."

            - An ASN is a unique identifier used to identify an Autonomous System (AS).
            - An Autonomous System is a collection of one or more IP blocks, managed by one or more Internet Service Providers (ISPs) or large enterprise units for routing. Each AS communicates on the Internet using an ASN to facilitate the exchange of routing information and IP packets. The ASN system ensures more efficient operation of the global Internet and guarantees that traffic between different networks can reach its intended destination correctly. You can refer to the introduction in the first paragraph of "[ASNs Autonomous System Observational Data Analysis](./ooni-asns-coverage.md){target="_blank"}" for more information.

=== ":material-checkbox-marked-circle-outline:OONI: Basic L3"

    - [x] Use OONI Explorer to organize Taiwan's observation data for the past six months.
    - [x] Compare observation data for three countries using OONI Explorer.
    - [x] Review current internet blocking reports.
    - [x] Create an OONI Run test link and find the online report content of that link.

    !!! abstract "OONI: Basic L3"

        ??? question "Use OONI Explorer to organize Taiwan's observation data for the past six months."

            - Visit the [OONI Explorer](https://explorer.ooni.org/){target="_blank"} website.
            - Find "Taiwan" as the observed location in the country column.
            - Use the date range selector to set the time frame to the past six months.
            - Review the results of different types of tests, such as website blocking, and the connectivity of instant messaging applications.
            - You can download or record relevant data and events from this period for further analysis.

        ??? question "Compare observation data for three countries using OONI Explorer."

            - On the OONI Explorer page, select "Country" for the vertical axis (Rows) and use the filters to choose the three countries you want to compare. ([Reference Settings](https://explorer.ooni.org/chart/mat?test_name=web_connectivity&axis_x=measurement_start_day&since=2025-05-01&until=2025-05-30&time_grain=day&axis_y=probe_cc){target="_blank"}).
            - Review the differences in test results for these countries, including website blocking, detection of man-in-the-middle attacks, etc.
            - Export the data as a CSV file for data comparison.

        ??? question "Review current internet blocking reports."

            - On the OONI Explorer homepage, there are typically the latest reports and trends regarding global internet censorship and blocking.
            - Browse the ["Search"](https://explorer.ooni.org/search){target="_blank"} or look up specific services and websites to check their current connectivity status.
            - You can view different types of tests under ["Internet Censorship"](https://explorer.ooni.org/social-media){target="_blank"}, such as social media, news media, etc.

        ??? question "Create an OONI Run test link and find the online report content of that link."

            - On the [OONI Run](https://run.ooni.org/){target="_blank"} page, provide your email to receive a login link.
            - After logging in through the link, fill out the mandatory fields on the form.
            - In the "Add URL+" section, add the website URL you want to test. Once completed, click "Create Link" to finalize the setup.
            - Share the URL or click on it, and follow the instructions to open OONI Probe to start the test. ([Test Reference](https://run.ooni.org/v2/10182){target="_blank"}).
            - The number `10182` at the end of the URL `https://run.ooni.org/v2/10182` is the OONI Run Link ID, which you can enter directly in OONI Explorer to find the test results. ([Result Reference](https://explorer.ooni.org/search?since=2025-04-29&until=2026-07-01&failure=false&ooni_run_link_id=10182){target="_blank"}).

### :material-checkbox-marked-circle-auto-outline: OONI-Advanced

=== ":material-checkbox-marked-circle-auto-outline: OONI: Advanced L1"

    - [x] Start OONI Probe using command line.
    - [x] Understand how website observation lists are compiled.

    !!! warning ""

        :wave: The assessment reference material for the Advanced section is expected to be completed by 2025/Q3.

=== ":material-checkbox-marked-circle-auto-outline: OONI: Advanced L2"

    - [x] Sort and analyze data using raw observation data.
    - [x] Assist in compiling and correcting lists.

    !!! warning ""

        :wave: The assessment reference material for the Advanced section is expected to be completed by 2025/Q3.
