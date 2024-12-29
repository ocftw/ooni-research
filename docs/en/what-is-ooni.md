---
title: What is OONI?
description: OONI, which stands for "Open Observatory of Network Interference," is a global initiative primarily aimed at monitoring and reporting internet censorship and interference.
icon: material/chat-question

---
# What is OONI?

OONI, short for "*Open Observatory of Network Interference,*" is a global initiative primarily aimed at monitoring and reporting internet censorship and interference. OONI provides open-source tools and collects network test data to help users identify the presence of internet blocking, surveillance, or throttling, and offers real-time and open analysis of internet censorship observations.

## Main Initiatives of the OONI Project

1. **Test Internet Censorship:** [OONI Probe](https://ooni.org/install/ "Download now."){target="_blank"} is an application used to test website or internet accessibility, allowing users to check if specific websites or online services are blocked.
2. **Open Data:** OONI releases [the collected data publicly](https://ooni.org/data/){target="_blank"}, providing free access for [exploration and analysis](https://explorer.ooni.org/ "Explore observation data online."){target="_blank"} to raise awareness of the censorship status of the [global internet](https://explorer.ooni.org/countries "Current number of observations by country."){target="_blank"}.
3. **Advocacy and Research:** Through the analysis of test data, OONI collaborates with researchers and advocates to focus on [global and regional](https://ooni.org/post/){target="_blank"} network interference trends and impacts.
4. **Local Community Collaboration:** OONI works with [other organizations](https://ooni.org/partners/){target="_blank"}, local communities, and projects to enhance testing capabilities and promote the goals of an open internet and barrier-free access.

By participating in OONI's probing activities, users can help raise awareness about global internet openness and support efforts to promote the free flow of digital information.

## How Does It Work?

<figure markdown="span">
    <a href="../assets/images/how-ooni-works.svg">
        <img src="../assets/images/how-ooni-works.svg"
            alt="How OONI Works: Inferring Content Interference by Comparing Web Page Presentations"
            title="How OONI Works: Inferring Content Interference by Comparing Web Page Presentations"
            style="border-radius: 10px;border:1px solid hsl(0, 0%, 0%);">
    </a>
</figure>

- **Probe:** The OONI testing and observation program.
- **Censor:** The entity monitoring the information transmission process, which could be a corporate IT network, telecommunications companies, or state-level network infrastructure. Internet interference can occur through the following methods, but their ultimate goal is to prevent access to website content.
    1. DNS Tampering (DNS anomalies)
    2. IP Blocking (DNS tampering, TCP/IP anomalies)
    3. HTTP Blocking (e.g., blocking pages)
    4. TLS-based Interference (such as connection resets observed after the ClientHello message during a TLS handshake)
- **Tor:** The [Onion Routing Network](https://en.wikipedia.org/wiki/Tor_(network) "Visit Wiki to learn more!"){target="_blank"}, which sends connection requests through three layers of node relays to obtain information.
- **Helper:** The target of testing, which could include: websites, communication software connections, VPN connections, connection performance, etc.

In Taiwan, familiar blocking behaviors and technologies include Chunghwa Telecom’s "[Family Care](https://hicare.hinet.net/CHT/hicare/){target="_blank"}," DNS-based blocking of ads, malicious sites by [AdGuard](https://adguard.com/en/welcome.html){target="_blank"}, and [Pi-Hole](https://pi-hole.net/){target="_blank"}. Additionally, practices such as domain blocking by the Ministry of Digital Affairs and the Taiwan Network Information Center (TWNIC) to fight scams, as detailed [here](https://moda.gov.tw/press/press-releases/6303){target="_blank"}, also fall under website browsing blocking.

!!! question "Is the internet we are on truly free?"

    The examples above typically target blocking malicious websites, online ads, and phishing scams with good intentions (e.g., [DNS RPZ](https://blog.twnic.tw/2020/09/23/15311/){target="_blank"}). But what if certain content is deliberately blocked? Or if blocking actions come from ASNs not yet recorded in observations? **Although current observations show no large-scale blocking**, the diversity of observation data is insufficient, being mostly concentrated on Chunghwa Telecom’s ([AS3462](https://radar.cloudflare.com/en/as3462){target="_blank"}) [observation data](https://explorer.ooni.org/chart/mat?probe_cc=TW&since=2024-10-01&until=2024-12-31&time_grain=month&axis_x=measurement_start_day&axis_y=probe_asn&test_name=web_connectivity){target="_blank"}. Therefore, in the "Regional Observation Data and ASNs Coverage Rate" research project, we will compare how many ASNs in TW remain unobserved.

## How to Install the OONI Probe

The OONI Probe is available in [mobile versions](https://ooni.org/install/){target="_blank"} (Android, iOS), [desktop versions](https://ooni.org/install/){target="_blank"} (Windows 64bit, macOS), and a [command-line interface version](https://ooni.org/install/cli){target="_blank"} without any desktop interface.


<figure markdown="span">
    <a href="../assets/images/ooni_screen_desktop.png">
        <img src="../assets/images/ooni_screen_desktop.png"
            alt="OONI Desktop Application Interface"
            title="OONI Desktop Application Interface"
            style="border-radius: 10px;border:1px solid hsl(0, 0%, 50%);width:75%;">
    </a>
</figure>

The command-line interface can execute all test items using `ooniprobe run`. Alternatively, you can set up a `cronjob` to run observation tests during idle times.

``` bash
# At minute 10 past hour 4, 10, and 22.
10 4,10,22 * * * ooniprobe run > /dev/null 2>&1 &
```

!!! warning "Automatic Execution"

    Currently, the `ooniprobe autorun` command has not been fully implemented. Therefore, use the `cronjob` method to schedule tests for the time being.

## OONI Explorer

<figure markdown="span">
    <a href="../assets/images/ooni_explorer.png">
        <img src="../assets/images/ooni_explorer.png"
            alt="OONI Explore（Delay by One Hour）"
            title="OONI Explore（Delay by One Hour）"
            style="border-radius: 10px;border:1px solid hsl(0, 0%, 50%);width:75%;">
    </a>
</figure>

Observed data is instantly transmitted to OONI's database and can be analyzed online through the [OONI Explorer](https://explorer.ooni.org/chart/mat?probe_cc=TW&since=2024-10-01&until=2025-01-01&time_grain=day&axis_x=measurement_start_day&test_name=web_connectivity){target="_blank"} to assess the conditions and results of various test items across different regions. Additionally, the raw observational data with a one-hour delay can be accessed and downloaded directly from the [S3 storage (Registry of Open Data on AWS)](https://registry.opendata.aws/ooni/){target="_blank"} for more in-depth cross-analysis. Users can choose to view data in real-time or download detailed data for further research according to their analysis needs.

!!! info "Observing AS Data"

    You can select the "Y-axis" item as ASN to filter and separate the observation status of each ASN.

    <figure markdown="span">
        <a href="../assets/images/ooni_explorer_asn.png">
            <img src="../assets/images/ooni_explorer_asn.png"
                alt="OONI Explorer allows you to select the "Y-axis" item as ASN to filter and separate the observation status of each ASN."
                title="OONI Explorer allows you to select the "Y-axis" item as ASN to filter and separate the observation status of each ASN."
                style="border-radius: 10px;border:1px solid hsl(0, 0%, 50%);width:80%;">
        </a>
    </figure>

## :fontawesome-solid-diagram-project: Next Steps

<div class="grid cards" markdown>

- :material-access-point-network: ASNs Observation Data Analysis
- :material-list-status: OONI Website Testing List
- :material-translate-variant: Localization and Translation

</div>
