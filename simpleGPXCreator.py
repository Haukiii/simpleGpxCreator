# Import packages
import gpxpy
from datetime import datetime, timedelta
import random
import geopy.distance

# Start time, default is now (UTC)
timePoint = datetime.now()
# Total distance in meters
distance = 1000
# Pace in m/s, the pace is the same throughout the activity
pace = 4.2
# Interval between points in seconds
interval = 5
# Start latitude
lat = 0
# Start longitude
lon = 0

# Initialize the gpx-data
gpx = gpxpy.gpx.GPX()

# Create first track in our GPX:
gpx_track = gpxpy.gpx.GPXTrack()
gpx.tracks.append(gpx_track)

# Create first segment in our GPX track:
gpx_segment = gpxpy.gpx.GPXTrackSegment()
gpx_track.segments.append(gpx_segment)

# Add the points
numberPoints = int(round(distance / pace / interval,0))

# This chooses a direction and makes sure that the track does not go backwards
direction = random.randrange(0,2)
lower = 0 + direction*180
upper = 180 + direction*180

for p in range(numberPoints):
    angleBearing = random.randrange(lower,upper)
    gpx_segment.points.append(gpxpy.gpx.GPXTrackPoint(lat, lon, time=timePoint))
    newPoint = geopy.distance.distance(meters=pace*interval).destination((lat, lon), bearing=angleBearing)
    lat = newPoint[0]
    lon = newPoint[1]
    timePoint = timePoint + timedelta(seconds=interval)

# Write the gpx-file
with open("output.gpx", "w") as f:
    f.write( gpx.to_xml())