#!/usr/bin/env python
# encoding: utf-8

from datetime import date, datetime, timedelta
import random
import sys
import uuid


if __name__=='__main__':
    FRAUD_RATE = 0.03
    REPEAT_PROB = 0.4
    REPEAT_DAYS = 1
    DELAY_DAYS = 90

    city_prob = []

    with open("city_prob.tsv", "r") as f:
        for line in f:
            (prob, city, lat, lng) = line.strip().split("\t")
            city_prob.append([float(prob), city, float(lat), float(lng)])

    fraud_loc = random.sample(city_prob, 3)
    prod_dict = {}

    with open("product.tsv", "r") as f:
        for line in f:
            (prod_area, product_id, amount) = line.strip().split("\t")

            if prod_area not in prod_dict:
                prod_dict[prod_area] = []

            prod_dict[prod_area].append([product_id, amount])

    cb_vect = []
    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        for line in f:
            (date_str, transaction_id, customer_id, product_id, amount, lat_str, lng_str) = line.strip().split("\t")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()

            if random.uniform(0.0, 1.0) < FRAUD_RATE:
                while random.uniform(0.0, 1.0) < REPEAT_PROB:
                    date += timedelta(random.randint(0, REPEAT_DAYS))

                    if date > datetime.today().date():
                        break 

                    transaction_id = uuid.uuid1().hex
                    prod_area = random.choice(prod_dict.keys())
                    (product_id, amount) = random.choice(prod_dict[prod_area])
                    (prob, city, lat, lng) = random.choice(fraud_loc)

                    lat += random.uniform(-0.02, 0.02)
                    lng += random.uniform(-0.03, 0.03)

                    print "\t".join([str(date), transaction_id, customer_id, product_id, amount, str(lat), str(lng)])
                    cb_vect.append((date, transaction_id, amount))

    file_name = sys.argv[2]
    cb_vect.sort()

    with open(file_name, "w") as f:
        for (date, transaction_id, amount) in cb_vect:
            date += timedelta(random.randint(0, DELAY_DAYS))

            if date <= datetime.today().date():
                f.write("\t".join([str(date), transaction_id, amount]) + "\n")
