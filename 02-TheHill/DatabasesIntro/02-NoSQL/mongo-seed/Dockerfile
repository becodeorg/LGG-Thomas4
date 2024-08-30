FROM mongo

COPY country_leaders.json /country_leaders.json
CMD mongoimport --host mongodb --db becode --collection leaders --type json --file /country_leaders.json --jsonArray
