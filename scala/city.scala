val city_pop = sc.textFile("dat/city_pop.tsv").map(_.split("\t")).map(r => (r(0), r))
val city_geo = sc.textFile("dat/city_geo.tsv").map(_.split("\t")).map(r => (r(0), r))

case class City (pop: Float, name: String, lat: Float, lng: Float)

val city_vect = city_pop.join(city_geo).map( 
 r => City(r._2._1(1).toFloat, r._1, r._2._2(1).toFloat, r._2._2(2).toFloat)
).map( r => (r.pop, r) ).sortByKey(false)

val sum_pop = city_vect.map(r => r._1).sum()
var cum_prob = 0.0

val cities = city_vect.map( r => r._2 ).collect

def cdf (c: City): String = {
  cum_prob += c.pop / sum_pop
  "%f\t%s\t%f\t%f".format(cum_prob, c.name, c.lat, c.lng)
}

sc.makeRDD( for (c <- cities) yield cdf(c) ).saveAsTextFile("city_prob")
