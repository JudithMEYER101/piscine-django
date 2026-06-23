import os
import psycopg2
from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings


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
            CREATE TABLE IF NOT EXISTS ex08_planets (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                climate VARCHAR,
                diameter INTEGER,
                orbital_period INTEGER,
                population BIGINT,
                rotation_period INTEGER,
                surface_water REAL,
                terrain VARCHAR(128)
            );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS ex08_people (
                id SERIAL PRIMARY KEY,
                name VARCHAR(64) UNIQUE NOT NULL,
                birth_year VARCHAR(32),
                gender VARCHAR(32),
                eye_color VARCHAR(32),
                hair_color VARCHAR(32),
                height INTEGER,
                mass REAL,
                homeworld VARCHAR(64),
                FOREIGN KEY (homeworld)
                REFERENCES ex08_planets(name)
            );
        """)

        connection.commit()
        cursor.close()
        connection.close()

        return HttpResponse("OK")

    except Exception as error:
        return HttpResponse(str(error))


def copy_file(cursor, filepath, table, columns):
    file = open(filepath, "r")

    cursor.copy_from(
        file,
        table,
        sep="\t",
        null="NULL",
        columns=columns
    )

    file.close()


def populate(request):
    results = []

    planets_path = os.path.join(settings.BASE_DIR, "ex08", "planets.csv")
    people_path = os.path.join(settings.BASE_DIR, "ex08", "people.csv")

    try:
        connection = get_connection()
        cursor = connection.cursor()

        try:
            copy_file(
                cursor,
                planets_path,
                "ex08_planets",
                (
                    "name",
                    "climate",
                    "diameter",
                    "orbital_period",
                    "population",
                    "rotation_period",
                    "surface_water",
                    "terrain",
                )
            )
            connection.commit()
            results.append("OK")
        except Exception as error:
            connection.rollback()
            results.append(str(error))

        try:
            copy_file(
                cursor,
                people_path,
                "ex08_people",
                (
                    "name",
                    "birth_year",
                    "gender",
                    "eye_color",
                    "hair_color",
                    "height",
                    "mass",
                    "homeworld",
                )
            )
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
            SELECT ex08_people.name, ex08_people.homeworld, ex08_planets.climate
            FROM ex08_people
            JOIN ex08_planets
            ON ex08_people.homeworld = ex08_planets.name
            WHERE ex08_planets.climate LIKE '%windy%'
            ORDER BY ex08_people.name;
        """)

        rows = cursor.fetchall()

        cursor.close()
        connection.close()

        if len(rows) == 0:
            return HttpResponse("No data available")

        return render(request, "ex08/display.html", {
            "rows": rows,
        })

    except Exception:
        return HttpResponse("No data available")