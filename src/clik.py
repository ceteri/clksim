#!/usr/bin/env python
# encoding: utf-8

from datetime import date, datetime, timedelta
import random
import sys


if __name__=='__main__':
    CTR = 0.003

    CAMP_BIAS = {
        "231": 1.0,
        "5150": 1.3,
        "93": 1.1,
        "42": 1.2,
        "123": 0.7,
        "777": 0.9,
        "2608": 0.8,
        }

    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        for line in f:
            (date_str, campaign_id, keyword, cookie) = line.strip().split("\t")

            date = datetime.strptime(date_str, "%Y-%m-%d").date() + timedelta(int(random.uniform(0.0, 1.3)))

            landing_page = random.randint(1, 9)

            if random.uniform(0.0, 1.0) < CTR * CAMP_BIAS[campaign_id]:
                print "\t".join([str(date), cookie, str(landing_page)])
