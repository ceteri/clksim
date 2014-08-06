#!/usr/bin/env python
# encoding: utf-8

import random


if __name__=='__main__':
    for prod_area in xrange(11+1):
        for _ in xrange(random.randint(23, 93)):
            product_id = "%x" % random.randint(0, 911 * 1000)
            amount = random.uniform(0.69, 23.00)

            print "\t".join([str(prod_area), product_id, "%0.2f" % amount])
