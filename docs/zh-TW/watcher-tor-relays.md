---
title: Tor Relays 觀測點
description: 各項觀察指標瞭解目前臺灣 Tor Relays 運作狀況
icon: material/chart-bar

---
<div class="grid cards" markdown>

- 持續與停止運作的數量[^1]
```vegalite
  {
    "description": "Tor Relays Running (count), Taiwan",
    "data": {"url" : "https://ooni-research.ocf.tw/api/vega/tor/relays/running?country=tw"},
    "mark": {
      "type": "area",
      "tooltip": true,
      "interpolate": "cardinal",
      "line": true,
      "point": true,
      "tension": 0.5
    },
    "encoding": {
      "x": {"field": "created_at",
            "type": "temporal",
            "timeUnit": "yearmonthdate",
            "axis": {"format": "%m/%d"},
            "title": "Created At (Month/Day)"
           },
      "y": {"field": "count", "type": "quantitative", "title": "Count"},
      "color": {
        "field": "running",
        "title": "Running",
        "scale": {
            "domain": [false, true],
            "range": ["#ff6384", "#36a2eb"]
        }
      }
    }
  }
```

- 每日提供的總頻寬[^2]
```vegalite
{
  "description": "Tor Relays Running (observed_bandwidth), Taiwan",
  "data": {"url" : "https://ooni-research.ocf.tw/api/vega/tor/relays/running?country=tw"},
  "mark": {
    "type": "area",
    "tooltip": true,
    "interpolate": "step",
    "point": true,
    "tension": 0.5,
    "line": true
  },
  "transform": [
    {"calculate": "datum.observed_bandwidth/1000000", "as": "observed_bandwidth"}
  ],
  "encoding": {
    "x": {"field": "created_at",
          "type": "temporal",
          "timeUnit": "yearmonthdate",
          "axis": {"format": "%m/%d"},
          "title": "Created At (Month/Day)"
         },
    "y": {"field": "observed_bandwidth", "type": "quantitative", "title": "Observed Bandwidth (MB/s)"},
    "color": {
        "field": "running",
        "title": "Running",
        "scale": {
            "domain": [false, true],
            "range": ["#ff6384", "#36a2eb"]
        }
    }
  }
}
```

- 版本數量[^3]
```vegalite
  {
    "description": "Tor Relays Version (count), Taiwan",
    "data": {"url" : "https://ooni-research.ocf.tw/api/vega/tor/relays/version?country=tw"},
    "mark": {
      "type": "area",
      "tooltip": true,
      "interpolate": "cardinal",
      "line": true,
      "point": true,
      "tension": 0.5
    },
    "encoding": {
      "x": {"field": "created_at",
            "type": "temporal",
            "timeUnit": "yearmonthdate",
            "axis": {"format": "%m/%d"},
            "title": "Created At (Month/Day)"
           },
      "y": {"field": "count", "type": "quantitative", "title": "Count"},
      "color": { "field": "version", "title": "Version" }
    }
  }
```

- ASN 每日唯一數量[^4]
```vegalite
  {
    "description": "Tor Relays ASN (count), Taiwan",
    "data": {"url" : "https://ooni-research.ocf.tw/api/vega/tor/relays/asn?country=tw"},
    "mark": {
      "type": "area",
      "tooltip": true,
      "interpolate": "cardinal",
      "line": true,
      "point": true,
      "tension": 0.5
    },
    "encoding": {
      "x": {"field": "created_at",
            "type": "temporal",
            "timeUnit": "yearmonthdate",
            "axis": {"format": "%m/%d"},
            "title": "Created At (Month/Day)"
           },
      "y": {"field": "count", "type": "quantitative", "title": "Count"},
      "color": { "field": "asn", "title": "ASN"}
    }
  }
```

- 中繼點類型數量[^5]
```vegalite
  {
    "description": "Tor Relays Node Type (count), Taiwan",
    "data": {"url" : "https://ooni-research.ocf.tw/api/vega/tor/relays/node_type?country=tw"},
    "mark": {
      "type": "area",
      "tooltip": true,
      "interpolate": "cardinal",
      "line": true,
      "point": true,
      "tension": 1
    },
    "encoding": {
      "x": {"field": "created_at",
            "type": "temporal",
            "timeUnit": "yearmonthdate",
            "axis": {"format": "%m/%d"},
            "title": "Created At (Month/Day)"
           },
      "y": {"field": "count", "type": "quantitative", "title": "Count"},
      "color": { "field": "node", "title": "Node Type" }
    }
  }
```

- 標籤類型數量[^6]
```vegalite
  {
    "description": "Tor Relays Flags (count), Taiwan",
    "data": {"url" : "https://ooni-research.ocf.tw/api/vega/tor/relays/flags?country=tw"},
    "mark": {
      "type": "area",
      "tooltip": true,
      "interpolate": "cardinal",
      "line": true,
      "point": false,
      "tension": 1
    },
    "encoding": {
      "x": {"field": "created_at",
            "type": "temporal",
            "timeUnit": "yearmonthdate",
            "axis": {"format": "%m/%d"},
            "title": "Created At (Month/Day)"
           },
      "y": {"field": "count", "type": "quantitative", "title": "Count"},
      "color": { "field": "flag", "title": "Flags" }
    }
  }
```
</div>

!!! example "持續開發中"

    - :tools: 目前此頁面的**觀察資料**與**呈現方式**都還在持續調整中，資料讀取的部分是透過[擷取資料 API 服務](https://ooni-research.ocf.tw/api/docs){target="_blank"}提供，而 API 資料服務也還在持續開發中。

[^1]: 持續與停止運作的數量：計算每日在臺灣的 Tor Relay 運作狀態數量，計算區間每小時不重複的 Tor Relay。
[^2]: 每日提供的總頻寬：計算每日在臺灣的 Tor Relay 總頻寬（MB/s），計算區間每小時不重複的 Tor Relay。
[^3]: 版本數量：計算每日在臺灣 Tor Relay 所使用的 Tor 版本號數量，計算區間每小時不重複的 Tor Relay。
[^4]: ASN 每日唯一數量：計算每日在臺灣的 Tor Relay 自治網路編號數量，計算區間每小時不重複的 Tor Relay。
[^5]: 中繼點類型數量：計算每日在臺灣的 Tor Relay 類型數量，計算區間每小時不重複的 Tor Relay。
[^6]: 標籤類型數量：計算每日在臺灣的 Tor Relay 標籤類型數量，計算區間每小時不重複的 Tor Relay。
