"""
Python 320 Wn 2023
December 2022
Class: sprouts
Author: Leonard Vaughn (@aqualen)
Due/Submission Date: FIXME
"""

import unittest
import uuid
import time

from google.cloud import monitoring_v3


class TestMetrics(unittest.TestCase):
    def test_something(self):
        # https://cloud.google.com/monitoring/custom-metrics/creating-metrics
        project_id = "test-sprouts"

        keys = "/Users/l/gcp/test-sprouts-5f2330e47aea.json"
        client = monitoring_v3.MetricServiceClient()
        project_name = f"projects/{project_id}"

        series = monitoring_v3.TimeSeries()
        series.metric.type = "custom.googleapis.com/greenhouse" + str(uuid.uuid4())
        series.resource.type = "global"
        # series.resource.labels["instance_id"] = "001"
        # series.resource.labels["zone"] = "us-central1-f"
        series.metric.labels["TestLabel"] = "My Label Data"
        now = time.time()

        seconds = int(now)
        nanos = int((now - seconds) * 10 ** 9)
        interval = monitoring_v3.TimeInterval({"end_time": {"seconds": seconds, "nanos": nanos}})
        point = monitoring_v3.Point({"interval": interval, "value": {"double_value": 3.14}})
        series.points = [point]
        client.create_time_series(name=project_name, time_series=[series])


if __name__ == '__main__':
    unittest.main()
