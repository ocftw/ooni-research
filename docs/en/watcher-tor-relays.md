---
title: Tor Relays
description: Various observation indicators to understand the current operation status of Tor Relays in Taiwan.
icon: material/chart-bar

---
<div class="grid cards" markdown>

- Number of Active and Inactive Relays[^1]
```vegalite
  {
    "description": "Tor Relays Running (count), Taiwan",
    "data": {"url" : "https://tor-watcher.toomore.net/api/vega/tor/relays/running?country=tw"},
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

- Total Daily Bandwidth Provision[^2]
```vegalite
{
  "description": "Tor Relays Running (observed_bandwidth), Taiwan",
  "data": {"url" : "https://tor-watcher.toomore.net/api/vega/tor/relays/running?country=tw"},
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

- Version Count[^3]
```vegalite
  {
    "description": "Tor Relays Version (count), Taiwan",
    "data": {"url" : "https://tor-watcher.toomore.net/api/vega/tor/relays/version?country=tw"},
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

- Daily Unique ASN Count[^4]
```vegalite
  {
    "description": "Tor Relays ASN (count), Taiwan",
    "data": {"url" : "https://tor-watcher.toomore.net/api/vega/tor/relays/asn?country=tw"},
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

- Number of Relay Types[^5]
```vegalite
  {
    "description": "Tor Relays Node Type (count), Taiwan",
    "data": {"url" : "https://tor-watcher.toomore.net/api/vega/tor/relays/node_type?country=tw"},
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

- Number of Flags Types[^6]
```vegalite
  {
    "description": "Tor Relays Flags (count), Taiwan",
    "data": {"url" : "https://tor-watcher.toomore.net/api/vega/tor/relays/flags?country=tw"},
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

!!! example "In ongoing development"

    - :tools: The **observation data** and **presentation format** on this page are still being adjusted. The data retrieval is provided through the [Data Extraction API Service](https://tor-watcher.toomore.net/api/docs){target="_blank"}, which is also under continuous development.

[^1]: Number of Active and Inactive Relays: Calculate the daily count of operational Tor Relays in Taiwan, ensuring each unique Tor Relay is counted once per hour in the calculation interval.
[^2]: Total Daily Bandwidth Provision: Calculate the total daily bandwidth (MB/s) of Tor Relays in Taiwan, ensuring each unique Tor Relay is counted once per hour in the calculation interval.
[^3]: Version Count: Calculate the number of different Tor version numbers used by Tor Relays in Taiwan daily, ensuring each unique Tor Relay is counted once per hour in the calculation interval.
[^4]: Daily Unique ASN Count: Calculate the daily count of Autonomous System Numbers (ASN) for Tor Relays in Taiwan, ensuring each unique Tor Relay is counted once per hour in the calculation interval.
[^5]: Number of Relay Types: Calculate the daily number of Tor Relay types in Taiwan, ensuring each unique Tor Relay is counted once per hour in the calculation interval.
[^6]: Number of Flags Types: Calculate the daily number of Tor Relay flag types in Taiwan, ensuring each unique Tor Relay is counted once per hour in the calculation interval.
