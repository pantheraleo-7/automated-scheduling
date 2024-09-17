import pandas as pd


pd.options.future.infer_string = True # remove once pandas 3.0 releases

agency = pd.read_csv('GTFS/agency.txt', index_col=0)
stops = pd.read_csv('GTFS/stops.txt', index_col=1)
routes = pd.read_csv('GTFS/routes.txt', index_col=1)
trips = pd.read_csv('GTFS/trips.txt', index_col=2)
stop_times = pd.read_csv('GTFS/stop_times.txt', index_col=0)

stop_times.arrival_time = pd.to_timedelta(stop_times.arrival_time)
stop_times.departure_time = pd.to_timedelta(stop_times.departure_time)
