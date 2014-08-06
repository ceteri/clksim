#!/usr/bin/env python
# encoding: utf-8

from datetime import date, datetime, timedelta
import random
import sys


def select_location (city_prob):
    x = random.uniform(0.0, 1.0)

    for c in city_prob:
        (prob, city, lat, lng) = c

        if prob > x:
            return city, lat, lng


if __name__=='__main__':
    CNV = 0.0666

    LAND_BIAS = {
        "1": 1.0,
        "2": 1.3,
        "3": 1.1,
        "4": 1.2,
        "5": 0.7,
        "6": 0.9,
        "7": 0.8,
        "8": 0.8,
        "9": 0.8,
        }


    city_prob = []

    with open("city_prob.tsv", "r") as f:
        for line in f:
            (prob, city, lat, lng) = line.strip().split("\t")
            city_prob.append([float(prob), city, float(lat), float(lng)])

    file_name = sys.argv[1]
    next_customer = 1000000

    with open(file_name, "r") as f:
        for line in f:
            (date_str, cookie, landing_page) = line.strip().split("\t")
            date = datetime.strptime(date_str, "%Y-%m-%d").date() + timedelta(int(random.uniform(0.0, 1.1)))

            if random.uniform(0.0, 1.0) < CNV * LAND_BIAS[landing_page]:
                next_customer += 1
                (city, lat, lng) = select_location(city_prob)
                lat += random.uniform(-0.02, 0.02)
                lng += random.uniform(-0.03, 0.03)

                print "\t".join([str(date), cookie, str(next_customer), str(lat), str(lng)])
