import psycopg2

conn = psycopg2.connect(dbname='n47',
                        user='postgres',
                        password='jasur   ',
                        host='localhost',
                        port=5432)

cur = conn.cursor()



