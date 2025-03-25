library(dplyr)

big_health = read.csv("/Users/zebbogue/Downloads/BigCitiesHealth-1.csv")
dim(big_health)

length(unique(big_health$geo_label_citystate))
length(unique(big_health$date_label))
length(unique(big_health$metric_item_label_subtitle))
unique(big_health$metric_subcat_label)

ny_inactivity = big_health %>% group_by(geo_label_citystate = "New York City, NY") %>%
group_by(metric_item_label = "Adult Physical Inactivity")
  

unique(ny_inactivity$date_label)                        

az_inactivity = big_health %>% group_by(metric_item_label = "Physical Inactivity") %>% 
  group_by(geo_label_citystate = "Phoenix, AZ")

unique(az_inactivity$date_label)

unique(big_health$metric_subcat_label)


cardio_disease = big_health %>% filter(metric_subcat_label == "Cardiovascular Disease")

cardio_disease %>% filter(geo_label_citystate == "Los Angeles, CA")



