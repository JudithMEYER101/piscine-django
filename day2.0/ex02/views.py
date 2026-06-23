import psycopg2
from django.http import HttpResponse
from django.shortcuts import render


def get_connection():
    return psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5432"
    )


def init(request):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex02_movies (
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


def populate(request):
    movies = [
        (1, "The Phantom Menace", None, "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", None, "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", None, "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", None, "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", None, "Irvin Kershner", "Gary Kutz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", None, "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", None, "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]

    results = []

    try:
        connection = get_connection()
        cursor = connection.cursor()

        for movie in movies:
            try:
                cursor.execute("""
                    INSERT INTO ex02_movies (
                        episode_nb,
                        title,
                        opening_crawl,
                        director,
                        producer,
                        release_date
                    )
                    VALUES (%s, %s, %s, %s, %s, %s);
                """, movie)

                connection.commit()
                results.append("OK")

            except Exception as error:
                connection.rollback()
                results.append(movie[1] + " : " + str(error))

        cursor.close()
        connection.close()

        return HttpResponse("<br>".join(results))

    except Exception as error:
        return HttpResponse(str(error))


def display(request):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT episode_nb, title, opening_crawl, director, producer, release_date
            FROM ex02_movies
            ORDER BY episode_nb;
        """)

        movies = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(movies) == 0:
            return HttpResponse("No data available")

        return render(request, "ex02/display.html", {
            "movies": movies,
        })

    except Exception:
        return HttpResponse("No data available")