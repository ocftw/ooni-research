---
title: Tor Relays 观测点
description: 各项观察指标了解目前台湾 Tor Relays 的运作状况。
icon: material/chart-bar

---
<div class="grid cards" markdown>

- 持续与停止运作的数量[^1]
```vegalite
  {
    "description": "Tor Relays Running (count), Taiwan",
    "data": {"url" : "https://anoni.net/api/vega/tor/relays/running?country=tw"},
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

- 每日提供的总带宽[^2]
```vegalite
{
  "description": "Tor Relays Running (observed_bandwidth), Taiwan",
  "data": {"url" : "https://anoni.net/api/vega/tor/relays/running?country=tw"},
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

- 版本数量[^3]
```vegalite
  {
    "description": "Tor Relays Version (count), Taiwan",
    "data": {"url" : "https://anoni.net/api/vega/tor/relays/version?country=tw"},
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

- ASN 每日唯一数量[^4]
```vegalite
  {
    "description": "Tor Relays ASN (count), Taiwan",
    "data": {"url" : "https://anoni.net/api/vega/tor/relays/asn?country=tw"},
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

- 中继点类型数量[^5]
```vegalite
  {
    "description": "Tor Relays Node Type (count), Taiwan",
    "data": {"url" : "https://anoni.net/api/vega/tor/relays/node_type?country=tw"},
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

- 标签类型数量[^6]
```vegalite
  {
    "description": "Tor Relays Flags (count), Taiwan",
    "data": {"url" : "https://anoni.net/api/vega/tor/relays/flags?country=tw"},
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

!!! example "持续开发中"

    - :tools: 目前此页面的**观察数据**与**呈现方式**都还在持续调整中，数据读取的部分是通过[获取数据 API 服务](https://anoni.net/api/readme){target="_blank"}提供，而 API 数据服务也还在持续开发中。

[^1]: 持续与停止运作的数量：计算每日在台湾的 Tor Relay 运作状态数量，计算区间为每小时不重复的 Tor Relay。
[^2]: 每日提供的总带宽：计算每日在台湾的 Tor Relay 总带宽（MB/s），计算区间为每小时不重复的 Tor Relay。
[^3]: 版本数量：计算每日在台湾 Tor Relay 所使用的 Tor 版本号数量，计算区间为每小时不重复的 Tor Relay。
[^4]: ASN 每日唯一数量：计算每日在台湾的 Tor Relay 自治网络编号数量，计算区间为每小时不重复的 Tor Relay。
[^5]: 中继点类型数量：计算每日在台湾的 Tor Relay 类型数量，计算区间为每小时不重复的 Tor Relay。
[^6]: 标签类型数量：计算每日在台湾的 Tor Relay 标签类型数量，计算区间为每小时不重复的 Tor Relay。
