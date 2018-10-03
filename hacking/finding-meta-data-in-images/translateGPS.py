import argparse

parser = argparse.ArgumentParser()
parser.add_argument("lat", help="Latitude values in D,M,S")
parser.add_argument("lon", help="Longitude values in D,M,S")
args = parser.parse_args()

if args.lat and args.lon:
	lat = args.lat.split(',')
	lon = args.lon.split(',')

	dlat = int(lat[0]) + (int(lat[1])/60.0) + (int(lat[2])/3600.0)
	dlon = int(lon[0]) + (int(lon[1])/60.0) + (int(lon[2])/3600.0)

	print dlat, dlon

else:
	print parser.usage


