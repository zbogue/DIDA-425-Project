library(dplyr)

big_health = read.csv("/Users/zebbogue/Downloads/BigCitiesHealth-1.csv")
dim(big_health)

length(unique(big_health$geo_label_citystate))
length(unique(big_health$date_label))
length(unique(big_health$metric_item_label_subtitle))
