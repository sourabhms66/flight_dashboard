import pymysql

class DB:

    def __init__(self):
        # constructor
        # connect to datbase
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                user='root',
                password='your_password',
                database='indigo'  # if you want to connect to a specific database
            )
            self.mycursor = self.conn.cursor()
            print('connection established')
        except:
            print('Connection error!')

    def fletch_city_name(self):
        city = []
        self.mycursor.execute("""
        SELECT distinct(Source) FROM flights
        union
        SELECT distinct(Destination) FROM flights
        """)
        data = self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
        return city

    def fletch_all_flights(self,source,destination):
        self.mycursor.execute("""
        SELECT Airline,Date_of_Journey,Source,Destination,Route,Dep_Time,Duration,Total_Stops,Price from flights
        where Source = '{}' and Destination = '{}'
        
        """.format(source,destination))
        data = self.mycursor.fetchall()
        return data

    def fletch_airline_frequency(self):
        airline = []
        freq = []
        self.mycursor.execute("""
        SELECT airline,count(*) from flights
        group by airline
        """)
        data = self.mycursor.fetchall()

        for i in data:
            airline.append(i[0])
            freq.append(i[1])
        return airline,freq

    def busy_airport(self):
        city = []
        freq = []
        self.mycursor.execute("""
        SELECT Source, count(*) from (select Source from flights
        union all select Destination from flights) t
        group by t.Source""")
        data = self.mycursor.fetchall()
        for i in data:
            city.append(i[0])
            freq.append(i[1])
        return city, freq

    def daily_frequency(self):
        date = []
        freq = []
        self.mycursor.execute("""
        SELECT Date_of_Journey, count(*) from flights
        group by Date_of_Journey""")
        data = self.mycursor.fetchall()
        for i in data:
            date.append(i[0])
            freq.append(i[1])
        return date, freq

