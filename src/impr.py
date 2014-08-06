#!/usr/bin/env python
# encoding: utf-8

from datetime import date, timedelta
import random
import sys
import uuid


MONTH_BIAS = {
    1: 0.7,
    2: 0.2,
    3: 0.4,
    4: 0.5,
    5: 0.5,
    6: 0.7,
    7: 0.5,
    8: 0.4,
    9: 0.3,
    10: 0.6,
    11: 0.8,
    12: 0.9,
    }


class Campaign (object):
    def __init__ (self, campaign_id, network, rate_metric, rate_amount, keyword, min_lat):
        self.campaign_id = campaign_id
        self.network = network
        self.rate_metric = rate_metric
        self.rate_amount = float(rate_amount)
        self.keyword = keyword
        self.min_lat = min_lat


    def generate (self, year, month):
        day = random.randint(1, 31)
        d = date(year, month, 1) + timedelta(day)
        cookie = uuid.uuid1().hex

        print "\t".join([str(d), self.campaign_id, self.keyword, cookie])


def load_campaigns (file_name):
    with open(file_name, "r") as f:
        camp_vect = []
        count = 0

        for line in f:
            if count > 0:
                (campaign_id, network, rate_metric, rate_amount, keyword, min_lat) = line.strip().split("\t")
                camp_vect.append(Campaign(campaign_id, network, rate_metric, rate_amount, keyword, min_lat))

            count += 1

    return camp_vect


if __name__=='__main__':
    camp_vect = load_campaigns(sys.argv[1])
    N_IMPRESSION = int(sys.argv[2])

    # generate impressions

    for _ in xrange(N_IMPRESSION):
        c = random.choice(camp_vect)

        year = random.randint(2009, 2013)
        month = random.randint(1, 12)

        count = 0
        count += 1 if (random.uniform(0.0, 3.5) > c.rate_amount) else 0
        count += 1 if (random.uniform(0.0, 1.0) < MONTH_BIAS[month]) else 0

        for _ in xrange(count):
            c.generate(year, month)
