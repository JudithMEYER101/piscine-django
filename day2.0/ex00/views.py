import psycopg2
from django.http import HttpResponse


def init(request):
    try:
        connection = psycopg2.connect(
            dbname="formationdjango",
            user="djangouser",
            password="secret",
            host="localhost",
            port="5432"
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex00_movies (
                episode_nb INTEGER PRIMARY KEY,
                title VARCHAR(64) UNIQUE NOT NULL,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL
            );
        """)

        connection.commit()
        cursor.close()
        connection.close()

        return HttpResponse("OK")

    except Exception as error:
        return HttpResponse(str(error))