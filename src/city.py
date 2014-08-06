#!/usr/bin/env python
# encoding: utf-8

if __name__=='__main__':
    city_dict = {}
    city_vect = []

    with open("dat/city_pop.tsv", "r") as f:
        count = 0

        for line in f:
            (city, population) = line.strip().split("\t")

            if (count > 0) and (city not in city_dict):
                city_dict[city] = int(population)

            count += 1

    with open("dat/city_geo.tsv", "r") as f:
        count = 0

        for line in f:
            (city, latitude, longitude) = line.strip().split("\t")

            if (count > 0) and (city in city_dict):
                city_vect.append([city_dict[city], city, float(latitude), float(longitude)])

            count += 1

    city_vect.sort(reverse=True)
    sum_pop = float(sum([ v[0] for v in city_vect]))
    cum_prob = 0.0

    for (pop, city, lat, lng) in city_vect:
        cum_prob += pop/sum_pop
        print "%0.6f\t%s\t%0.4f\t%0.4f" % (cum_prob, city, lat, lng)
