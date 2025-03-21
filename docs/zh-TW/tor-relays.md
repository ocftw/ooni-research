```vegalite
{
  "description": "A simple bar chart with embedded data.",
  "data": {"url" : "assets/charts/data/basic_bar_chart.json"},
  "mark": {
    "type": "area",
    "tooltip": true,
    "interpolate": "cardinal",
    "line": true,
    "point": true,
    "tension": 0.5
  },
  "encoding": {
    "color": {"field": "source"},
    "x": {"field": "a",
          "type": "temporal",
          "timeUnit": "yearmonthdate",
          "axis": {"format": "%m/%d"}
         },
    "y": {"field": "b", "type": "quantitative"}
  }
}
```