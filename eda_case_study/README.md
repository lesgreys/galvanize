## Goal
------

Our intent was to analyze global transit rail systems and identify characteristics in the data that would allow to understand trends.


### Exploratory Data Analysis
----

### The Data

The data used was comprised of 6 data sets with following information; cities, lines, station lines, systems, tracks.


Plotted avg track length per city ID, grouped by city ID.

![Avg Track Length per City]('avg_track_length_per_cityID.PNG')


Unsurprisingly, Tokyo comes it with far more stations than any other major city in the world, which reflects the ecosystem’s heavy use on trains as a primary mode of public transportation. Noticeably absent are major cities in populous countries such as India, Indonesia, Pakistan, and Nigeria.

![Station per City]('station_count_by_city_bar_graph_2.png')

Although we were not sure the exact meaning of systems, there was a lot of overlap between the number of systems and stations per country. Tokyo had the most of amount of systems. Followed by Glasgow, Paris, Nantes, & Valencia. Europe held most of the spots within the top ten category. 

![Systems per City]('systems_per_city.png')


Here we take a look at the top ten per city. 

![Top Ten Systems per City]('top_ten_systems_per_city.png')

### Conclusion
--------

In conclusion, the team spent a lot of the time trying to wrangle the data in a more comprehensive format. The seperation of the all the tables created some complexities that segmented the information and made it difficult to combine information as we originally wanted.

We attempted to use the GPS coordinate systems to plot the lines but were unable to achieve the desired result. We would need some extra time to become familiar with the geospacial libraries that would allow us to plot the station lines. 
