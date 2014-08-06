## clksim
This code implements a simple *clickstream simulator* written in Python, along with a few TSV data files used to seed it.
It has been used for generating the log files used in the [CCAI workshop](http://liber118.com/course/ccai/).

The simulations used here are embarrassingly simplistic.
Even so, these generate realistic log files that provide:

  * impressions based on ad campaigns, with seasonal variation
  * landing pages and click-through
  * registrations
  * orders
  * chargebacks

There are some geo aspects in the fraud simulation, which students have used for excellent visualizations.
The fraud patterns are somewhat realistic -- based on what we'd experienced in a popular e-commerce firm, circa 2011.
Students have used the generated log data to build:

  * marketing funnel KPI + optimization
  * anti-fraud classifiers
  * product recommenders

The product recommender aspects are rather light -- that part could be embellished much more.

### Schema

`city_prob.tsv`: *fraud_prob, city, latitude, longitude*

`product.tsv`: *prod_area, product_id, amount*

`campaign.tsv`: *campaign_id, network, rate_metric, rate_amount, keyword, min_lat*

`impression.tsv`: *date, campaign_id, keyword, cookie*

`clicks.tsv`: *date, cookie, landing_page*

`register.tsv`: *date, cookie, customer_id, latitude, longitude*

`orders.tsv`: *date, transaction_id, customer_id, product_id, amount, latitude, longitude*

`chargeback.tsv`: *date, transaction_id, amount*

### Usage

    # geo distribution by cities
    # probability, city, latitude, longitude
    ./src/city.py > city_prob.tsv

    # product catalog
    # product_area, product_id, amount
    ./src/prod.py > product.tsv

    # online marketing campaigns -- hard-coded
    # campaign_id, network, rate_metric, rate_amount, keyword
    ls dat/campaign.tsv

    # ad impressions
    # date, campaign_id, keyword, cookie
    ./src/impr.py dat/campaign.tsv 10000000 | sort > impression.tsv

    # click-through
   #  date, cookie, landing_page
    ./src/clik.py impression.tsv | sort > clicks.tsv

    # customer registrations
    # date, cookie, customer_id, latitude, longitude
    ./src/regs.py clicks.tsv | sort > register.tsv

    # e-commerce orders
    # date, transaction_id, customer_id, product_id, amount, latitude, longitude
    ./src/ords.py register.tsv | sort > valid_orders.tsv

    # chargebacks
    # date, transaction_id, amount
    ./src/frau.py valid_orders.tsv chargeback.tsv > fraud_orders.tsv
    cat valid_orders.tsv fraud_orders.tsv | sort > orders.tsv

### Packaging Results
The following commands create a tarball for the workshop:

    rm -rf datasets.tgz
    tar cvzf datasets.tgz SCHEMA.md campaign.tsv city_geo.tsv \
      impression.tsv clicks.tsv register.tsv orders.tsv chargeback.tsv
