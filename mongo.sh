## Switch Database
use test

## Find One Data
db.zips.findOne()

## Where Clause
db.zips.find({state:"MA"})
db.zips.find({state:"MA", pop:{$gt:30000}})


## Return States with Populations above 10 Million
db.zips.aggregate( [
   { $group: { _id: "$state", totalPop: { $sum: "$pop" } } },
   { $match: { totalPop: { $gte: 10000000 } } }
] )

## Return Average City Population by State
db.zips.aggregate( [
   { $group: { _id: { state: "$state", city: "$city" }, pop: { $sum: "$pop" } } },
   { $group: { _id: "$_id.state", avgCityPop: { $avg: "$pop" } } }
] )