import psycopg2
from django.http import HttpResponse
from django.shortcuts import render, redirect


def get_connection():
    return psycopg2.connect(
        dbname="formationdjango",
        user="djangouser",
        password="secret",
        host="localhost",
        port="5432"
    )


def get_movies():
    return [
        (1, "The Phantom Menace", None, "George Lucas", "Rick McCallum", "1999-05-19"),
        (2, "Attack of the Clones", None, "George Lucas", "Rick McCallum", "2002-05-16"),
        (3, "Revenge of the Sith", None, "George Lucas", "Rick McCallum", "2005-05-19"),
        (4, "A New Hope", None, "George Lucas", "Gary Kurtz, Rick McCallum", "1977-05-25"),
        (5, "The Empire Strikes Back", None, "Irvin Kershner", "Gary Kutz, Rick McCallum", "1980-05-17"),
        (6, "Return of the Jedi", None, "Richard Marquand", "Howard G. Kazanjian, George Lucas, Rick McCallum", "1983-05-25"),
        (7, "The Force Awakens", None, "J. J. Abrams", "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "2015-12-11"),
    ]


def init(request):
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex06_movies (
                episode_nb INTEGER PRIMARY KEY,
                title VARCHAR(64) UNIQUE NOT NULL,
                opening_crawl TEXT,
                director VARCHAR(32) NOT NULL,
                producer VARCHAR(128) NOT NULL,
                release_date DATE NOT NULL,
                created TIMESTAMP NOT NULL DEFAULT now(),
                updated TIMESTAMP NOT NULL DEFAULT now()
            );
        """)

        cursor.execute("""
            CREATE OR REPLACE FUNCTION update_changetimestamp_column()
            RETURNS TRIGGER AS $$
            BEGIN
                NEW.updated = now();
                NEW.created = OLD.created;
                RETURN NEW;
            END;
            $$ language 'plpgsql';
        """)

        cursor.execute("""
            DROP TRIGGER IF EXISTS update_films_changetimestamp
            ON ex06_movies;
        """)

        cursor.execute("""
            CREATE TRIGGER update_films_changetimestamp
            BEFORE UPDATE ON ex06_movies
            FOR EACH ROW
            EXECUTE PROCEDURE update_changetimestamp_column();
        """)

        connection.commit()
        cursor.close()
        connection.close()

        return HttpResponse("OK")

    except Exception as error:
        return HttpResponse(str(error))


def populate(request):
    results = []

    try:
        connection = get_connection()
        cursor = connection.cursor()

        for movie in get_movies():
            try:
                cursor.execute("""
                    INSERT INTO ex06_movies (
                        episode_nb,
                        title,
                        opening_crawl,
                        director,
                        producer,
                        release_date
                    )
                    VALUES (%s, %s, %s, %s, %s, %s)
                    ON CONFLICT (episode_nb) DO NOTHING;
                """, movie)

                connection.commit()
                results.append("OK")

            except Exception as error:
                connection.rollback()
                results.append(str(error))

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
            SELECT episode_nb, title, opening_crawl, director, producer,
                   release_date, created, updated
            FROM ex06_movies
            ORDER BY episode_nb;
        """)

        movies = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(movies) == 0:
            return HttpResponse("No data available")

        return render(request, "ex06/display.html", {
            "movies": movies,
        })

    except Exception:
        return HttpResponse("No data available")


def get_titles():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT title
        FROM ex06_movies
        ORDER BY episode_nb;
    """)

    titles = cursor.fetchall()

    cursor.close()
    connection.close()

    return titles


def update(request):
    try:
        if request.method == "POST":
            title = request.POST.get("title")
            opening_crawl = request.POST.get("opening_crawl")

            if title is not None and opening_crawl is not None:
                connection = get_connection()
                cursor = connection.cursor()

                cursor.execute("""
                    UPDATE ex06_movies
                    SET opening_crawl = %s
                    WHERE title = %s;
                """, (opening_crawl, title))

                connection.commit()
                cursor.close()
                connection.close()

            return redirect("/ex06/update")

        titles = get_titles()

        if len(titles) == 0:
            return HttpResponse("No data available")

        return render(request, "ex06/update.html", {
            "titles": titles,
        })

    except Exception:
        return HttpResponse("No data available")