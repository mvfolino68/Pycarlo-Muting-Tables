template = {
    "description": "Completeness Check",
    "labels": ["POC Audience"],
    "notify_rule_run_failure": True,
    "schedule": {
        "type": "fixed",
        "interval_minutes": 1440,
        "start_time": "2023-10-05T20:53:37.877000+00:00",
        "timezone": "UTC",
    },
    "event_rollup_until_changed": False,
    "sql": "SELECT * FROM {{table}} WHERE {{field}} IS NULL OR {{field}} <> '' AND {{datefield}} = current_date() - INTERVAL {{lookback_days}} DAY",
    "variables": {
        "field": ["{{field}}"],
        "table": ["{{table}}"],
        "datefield": ["timestamp"],
        "lookback_days": [1],
    },
    "comparisons": [{"type": "threshold", "operator": "GT", "threshold_value": 0.0}],
}
