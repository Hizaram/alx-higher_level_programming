#!/usr/bin/python3
"""Script that lists all the cities from the database `hbtn_0e_4_usa`
   ordered by city_id that matches the state_name fed as argument.
   Usage: ./4-cities_by_state.py <MySQL username> <MySQL passwd> <db name>
"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `cities` AS `c` INNER JOIN `states` AS `s` \
              ON `c`.`state_id` = `s`.`id` ORDER BY `c`.`id`")
    print(", ".join([city[2] for city in c.fetchall() if city[4] == sys.argv[4]]))
