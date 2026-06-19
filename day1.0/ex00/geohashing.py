import sys
import antigravity


def geohashing():
    """Get longitude and Latitude and date+DOW (StockMarcket value)
        l and L gives us a zone and date+DOW is used to get a random offset
        inside l and L"""

    if len(sys.argv) != 4:
        print("Error: expected latitude, longitude and datedow.")
        return

    try:
        latitude = float(sys.argv[1])
        longitude = float(sys.argv[2])
        datedow = sys.argv[3].encode()
        antigravity.geohash(latitude, longitude, datedow)
    except Exception as error:
        print("Error:", error)


if __name__ == '__main__':
    geohashing()