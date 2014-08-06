#!/usr/bin/env python
# encoding: utf-8

from datetime import date, datetime, timedelta
import random
import sys
import uuid


if __name__=='__main__':
    REPEAT_PROB = 0.95
    REPEAT_DAYS = 11

    prod_dict = {}

    with open("product.tsv", "r") as f:
        for line in f:
            (prod_area, product_id, amount) = line.strip().split("\t")

            if prod_area not in prod_dict:
                prod_dict[prod_area] = []

            prod_dict[prod_area].append([product_id, amount])


    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        for line in f:
            (date_str, cookie, customer_id, lat_str, lng_str) = line.strip().split("\t")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            cust_prod = random.sample(prod_dict.keys(), random.randint(1, 3))

            while random.uniform(0.0, 1.0) < REPEAT_PROB:
                date += timedelta(random.randint(0, REPEAT_DAYS))

                if date > datetime.today().date():
                    break 

                lat = float(lat_str) + random.uniform(-0.02, 0.02)
                lng = float(lng_str) + random.uniform(-0.03, 0.03)

                transaction_id = uuid.uuid1().hex
                prod_area = random.choice(cust_prod)
                (product_id, amount) = random.choice(prod_dict[prod_area])

                print "\t".join([str(date), transaction_id, customer_id, product_id, amount, str(lat), str(lng)])
