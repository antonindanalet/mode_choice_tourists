import os
from pathlib import Path
import biogeme.database as db
import biogeme.biogeme as bio
from biogeme import models
from biogeme.expressions import Beta, Variable, DefineVariable
import get_data


def run():
    df = get_data.get_data()
    estimate_model(df)


def estimate_model(df):
    database = db.Database('tms', df)

    transport_mode = Variable('transport_mode')
    age = Variable('age')
    country = Variable('country')
    stars = Variable('stars')
    urban_rural_typology = Variable('urban_rural_typology')
    accommodation_type = Variable('accommodation_type')
    region = Variable('region')
    age_train = DefineVariable('age_train', (transport_mode == 1) * age, database)
    age_car = DefineVariable('age_car', (transport_mode == 3) * age, database)
    urban = DefineVariable('urban', urban_rural_typology == 1, database)
    rural = DefineVariable('rural', urban_rural_typology == 3, database)
    region_geneva = DefineVariable('region_geneva', region == 1, database)
    region_lausanne = DefineVariable('region_lausanne', region == 2, database)
    region_neuchatel = DefineVariable('region_neuchatel', region == 3, database)
    region_fribourg = DefineVariable('region_fribourg', region == 4, database)
    region_biel_jura = DefineVariable('region_biel_jura', region == 5, database)
    region_bern = DefineVariable('region_bern', region == 6, database)
    region_westalpen = DefineVariable('region_westalpen', region == 7, database)
    region_basel = DefineVariable('region_basel', region == 8, database)
    region_berner_oberland = DefineVariable('region_berner_oberland', region == 9, database)
    region_aareland = DefineVariable('region_aareland', region == 10, database)
    region_zentralschweiz = DefineVariable('region_zentralschweiz', region == 11, database)
    region_zurich = DefineVariable('region_zurich', region == 12, database)
    region_sopraceneri = DefineVariable('region_sopraceneri', region == 13, database)
    region_sottoceneri = DefineVariable('region_sottoceneri', region == 14, database)
    region_bodensee = DefineVariable('region_bodensee', region == 15, database)
    region_ostalpen = DefineVariable('region_ostalpen', region == 16, database)

    # Parameters to be estimated
    ASC_train = Beta('ASC_train', 0, None, None, 0)
    ASC_bicycle = Beta('ASC_bicycle', 0, None, None, 0)
    ASC_car = Beta('ASC_car', 0, None, None, 1)
    ASC_bus = Beta('ASC_bus', 0, None, None, 0)
    ASC_other = Beta('ASC_other', 0, None, None, 0)
    ASC_tour_bus = Beta('ASC_tour_bus', 0, None, None, 0)
    ASC_long_distance_bus = Beta('ASC_long_distance_bus', 0, None, None, 0)
    beta_stars_train = Beta('beta_stars_train', 0, None, None, 0)
    beta_stars_bicycle = Beta('beta_stars_bicycle', 0, None, None, 1)
    beta_stars_bus = Beta('beta_stars_bus', 0, None, None, 0)
    beta_stars_long_distance_bus = Beta('beta_stars_long_distance_bus', 0, None, None, 1)
    beta_stars_other = Beta('beta_stars_other', 0, None, None, 0)
    beta_stars_tour_bus = Beta('beta_stars_tour_bus', 0, None, None, 0)
    beta_hotel_train = Beta('beta_hotel_train', 0, None, None, 1)
    beta_holiday_homes_train = Beta('beta_holiday_homes_train', 0, None, None, 0)
    beta_camping_train = Beta('beta_camping_train', 0, None, None, 0)
    beta_collective_accommodation_train = Beta('beta_collective_accommodation_train', 0, None, None, 1)

    beta_hotel_bicycle = Beta('beta_hotel_bicycle', 0, None, None, 1)
    beta_holiday_homes_bicycle = Beta('beta_holiday_homes_bicycle', 0, None, None, 0)
    beta_camping_bicycle = Beta('beta_camping_bicycle', 0, None, None, 0)
    beta_collective_accommodation_bicycle = Beta('beta_collective_accommodation_bicycle', 0, None, None, 1)

    beta_hotel_long_distance_bus = Beta('beta_hotel_long_distance_bus', 0, None, None, 1)
    beta_holiday_homes_long_distance_bus = Beta('beta_holiday_homes_long_distance_bus', 0, None, None, 0)
    beta_camping_long_distance_bus = Beta('beta_camping_long_distance_bus', 0, None, None, 1)
    beta_collect_accomm_long_distance_bus = Beta('beta_collect_accomm_long_distance_bus', 0, None, None, 1)

    beta_hotel_bus = Beta('beta_hotel_bus', 0, None, None, 1)
    beta_holiday_homes_bus = Beta('beta_holiday_homes_bus', 0, None, None, 0)
    beta_camping_bus = Beta('beta_camping_bus', 0, None, None, 0)
    beta_collective_accommodation_bus = Beta('beta_collective_accommodation_bus', 0, None, None, 1)

    beta_hotel_tour_bus = Beta('beta_hotel_tour_bus', 0, None, None, 1)
    beta_holiday_homes_tour_bus = Beta('beta_holiday_homes_tour_bus', 0, None, None, 0)
    beta_camping_tour_bus = Beta('beta_camping_tour_bus', 0, None, None, 0)
    beta_collective_accommodation_tour_bus = Beta('beta_collective_accommodation_tour_bus', 0, None, None, 0)

    beta_hotel_other = Beta('beta_hotel_other', 0, None, None, 1)
    beta_holiday_homes_other = Beta('beta_holiday_homes_other', 0, None, None, 0)
    beta_camping_other = Beta('beta_camping_other', 0, None, None, 0)
    beta_collective_accommodation_other = Beta('beta_collective_accommodation_other', 0, None, None, 0)

    beta_france_belgium_train = Beta('beta_france_belgium_train', -1, None, None, 0)
    beta_italy_train = Beta('beta_italy_train', -1, None, None, 0)
    beta_spain_train = Beta('beta_spain_train', -1, None, None, 0)
    beta_poland_czech_republic_train = Beta('beta_poland_czech_republic_train', -1, None, None, 0)
    beta_northern_europe_train = Beta('beta_northern_europe_train', 0, None, None, 1)
    beta_austria_train = Beta('beta_austria_train', -1, None, None, 0)
    beta_finland_train = Beta('beta_finland_train', 0, None, None, 1)
    beta_norway_train = Beta('beta_norway_train', 0, None, None, 1)
    beta_sweden_train = Beta('beta_sweden_train', 0, None, None, 1)
    beta_scandinavia_train = Beta('beta_scandinavia_train', 0, None, None, 1)
    beta_denmark_train = Beta('beta_denmark_train', -1, None, None, 0)
    beta_russia_train = Beta('beta_russia_train', 0, None, None, 0)
    beta_australia_train = Beta('beta_australia_train', 0, None, None, 1)
    beta_new_zealand_train = Beta('beta_new_zealand_train', 0, None, None, 1)
    beta_asia_train = Beta('beta_asia_train', 1, None, None, 0)
    beta_east_asia_train = Beta('beta_east_asia_train', 0, None, None, 1)
    beta_middle_east_train = Beta('beta_middle_east_train', -1, None, None, 0)
    beta_germany_train = Beta('beta_germany_train', -1, None, None, 0)
    beta_united_kingdom_train = Beta('beta_united_kingdom_train', 0, None, None, 0)
    beta_america_australasia_train = Beta('beta_america_australasia_train', 1, None, None, 0)

    beta_belgium_bus = Beta('beta_belgium_bus', 0, None, None, 0)
    beta_france_germany_bus = Beta('beta_france_germany_bus', 0, None, None, 0)
    beta_italy_spain_bus = Beta('beta_italy_spain_bus', 0, None, None, 1)
    beta_poland_bus = Beta('beta_poland_bus', 0, None, None, 1)
    beta_czech_republic_bus = Beta('beta_czech_republic_bus', 0, None, None, 1)
    beta_brazil_bus = Beta('beta_brazil_bus', 0, None, None, 1)
    beta_northern_europe_bus = Beta('beta_northern_europe_bus', 0, None, None, 1)
    beta_austria_bus = Beta('beta_austria_bus', 0, None, None, 1)
    beta_finland_bus = Beta('beta_finland_bus', 0, None, None, 1)
    beta_norway_bus = Beta('beta_norway_bus', 0, None, None, 1)
    beta_sweden_bus = Beta('beta_sweden_bus', 0, None, None, 1)
    beta_scandinavia_bus = Beta('beta_scandinavia_bus', 0, None, None, 1)
    beta_denmark_bus = Beta('beta_denmark_bus', 0, None, None, 1)
    beta_russia_bus = Beta('beta_russia_bus', 0, None, None, 1)
    beta_india_bus = Beta('beta_india_bus', 0, None, None, 0)
    beta_australia_bus = Beta('beta_australia_bus', 0, None, None, 1)
    beta_new_zealand_bus = Beta('beta_new_zealand_bus', 0, None, None, 1)
    beta_australasia_bus = Beta('beta_australasia_bus', 0, None, None, 1)
    beta_southeast_asia_bus = Beta('beta_southeast_asia_bus', 0, None, None, 0)
    beta_united_kingdom_bus = Beta('beta_united_kingdom_bus', 0, None, None, 1)
    beta_north_america_bus = Beta('beta_north_america_bus', 0, None, None, 1)
    beta_china_bus = Beta('beta_china_bus', 0, None, None, 1)
    beta_east_asia_bus = Beta('beta_east_asia_bus', 0, None, None, 1)
    beta_middle_east_bus = Beta('beta_middle_east_bus', 0, None, None, 0)
    beta_japan_bus = Beta('beta_japan_bus', 0, None, None, 1)
    beta_korea_bus = Beta('beta_korea_bus', 0, None, None, 1)
    beta_us_bus = Beta('beta_us_bus', 0, None, None, 1)
    beta_canada_bus = Beta('beta_canada_bus', 0, None, None, 1)

    beta_belgium_tour_bus = Beta('beta_belgium_tour_bus', 0, None, None, 0)
    beta_france_tour_bus = Beta('beta_france_tour_bus', 0, None, None, 0)
    beta_italy_tour_bus = Beta('beta_italy_tour_bus', 0, None, None, 0)
    beta_spain_tour_bus = Beta('beta_spain_tour_bus', 0, None, None, 0)
    beta_russia_poland_czech_republic_tour_bus = Beta('beta_russia_poland_czech_republic_tour_bus', 0, None, None, 1)
    beta_brazil_tour_bus = Beta('beta_brazil_tour_bus', 0, None, None, 0)
    beta_austria_tour_bus = Beta('beta_austria_tour_bus', 0, None, None, 1)
    beta_sweden_tour_bus = Beta('beta_sweden_tour_bus', 0, None, None, 1)
    beta_india_tour_bus = Beta('beta_india_tour_bus', 0, None, None, 0)
    beta_australasia_tour_bus = Beta('beta_australasia_tour_bus', 0, None, None, 0)
    beta_germany_denmark_tour_bus = Beta('beta_germany_denmark_tour_bus', 0, None, None, 0)
    beta_united_kingdom_tour_bus = Beta('beta_united_kingdom_tour_bus', 0, None, None, 1)
    beta_north_america_tour_bus = Beta('beta_north_america_tour_bus', 0, None, None, 1)
    beta_china_tour_bus = Beta('beta_china_tour_bus', 0, None, None, 0)
    beta_middle_east_tour_bus = Beta('beta_middle_east_tour_bus', 0, None, None, 0)
    beta_japan_korea_tour_bus = Beta('beta_japan_korea_tour_bus', 0, None, None, 1)
    beta_us_tour_bus = Beta('beta_us_tour_bus', 0, None, None, 1)
    beta_east_asia_tour_bus = Beta('beta_east_asia_tour_bus', 0, None, None, 1)
    beta_canada_tour_bus = Beta('beta_canada_tour_bus', 0, None, None, 1)
    beta_northern_europe_tour_bus = Beta('beta_northern_europe_tour_bus', 0, None, None, 1)
    beta_southeast_asia_tour_bus = Beta('beta_southeast_asia_tour_bus', 0, None, None, 1)
    beta_australia_tour_bus = Beta('beta_australia_tour_bus', 0, None, None, 1)
    beta_new_zealand_tour_bus = Beta('beta_new_zealand_tour_bus', 0, None, None, 1)
    beta_scandinavia_tour_bus = Beta('beta_scandinavia_tour_bus', 0, None, None, 1)

    beta_belgium_bicycle = Beta('beta_belgium_bicycle', 0, None, None, 1)
    beta_france_bicycle = Beta('beta_france_bicycle', 0, None, None, 1)
    beta_italy_bicycle = Beta('beta_italy_bicycle', 0, None, None, 1)
    beta_spain_bicycle = Beta('beta_spain_bicycle', 0, None, None, 1)
    beta_russia_poland_czech_republic_bicycle = Beta('beta_russia_poland_czech_republic_bicycle', 0, None, None, 1)
    beta_brazil_bicycle = Beta('beta_brazil_bicycle', 0, None, None, 1)
    beta_austria_bicycle = Beta('beta_austria_bicycle', 0, None, None, 0)
    beta_norway_bicycle = Beta('beta_norway_bicycle', 0, None, None, 1)
    beta_australasia_bicycle = Beta('beta_australasia_bicycle', 0, None, None, 1)
    beta_germany_bicycle = Beta('beta_germany_bicycle', 0, None, None, 1)
    beta_denmark_bicycle = Beta('beta_denmark_bicycle', 0, None, None, 1)
    beta_north_america_bicycle = Beta('beta_north_america_bicycle', 0, None, None, 1)
    beta_china_bicycle = Beta('beta_china_bicycle', 0, None, None, 1)
    beta_us_bicycle = Beta('beta_us_bicycle', 0, None, None, 1)
    beta_east_asia_bicycle = Beta('beta_east_asia_bicycle', 0, None, None, 1)
    beta_canada_bicycle = Beta('beta_canada_bicycle', 0, None, None, 1)
    beta_southeast_asia_bicycle = Beta('beta_southeast_asia_bicycle', 0, None, None, 1)
    beta_australia_bicycle = Beta('beta_australia_bicycle', 0, None, None, 1)
    beta_scandinavia_bicycle = Beta('beta_scandinavia_bicycle', 0, None, None, 1)
    beta_denmark_scandinavia_bicycle = Beta('beta_denmark_scandinavia_bicycle', 0, None, None, 0)
    beta_united_kingdom_bicycle = Beta('beta_united_kingdom_bicycle', 0, None, None, 1)

    beta_china_long_distance_bus = Beta('beta_china_long_distance_bus', 0, None, None, 0)
    beta_india_long_distance_bus = Beta('beta_india_long_distance_bus', 0, None, None, 0)
    beta_poland_long_distance_bus = Beta('beta_poland_long_distance_bus', 0, None, None, 1)
    beta_brazil_long_distance_bus = Beta('beta_brazil_long_distance_bus', 0, None, None, 0)

    beta_urban_train = Beta('beta_urban_train', 0, None, None, 0)
    beta_urban_bicycle = Beta('beta_urban_bicycle', 0, None, None, 1)
    beta_urban_bus = Beta('beta_urban_bus', 0, None, None, 0)
    beta_urban_long_distance_bus = Beta('beta_urban_long_distance_bus', 0, None, None, 0)
    beta_urban_tour_bus = Beta('beta_urban_tour_bus', 0, None, None, 0)
    beta_urban_other = Beta('beta_urban_other', 0, None, None, 1)

    beta_rural_train = Beta('beta_rural_train', 0, None, None, 0)
    beta_rural_bicycle = Beta('beta_rural_bicycle', 0, None, None, 1)
    beta_rural_bus = Beta('beta_rural_bus', 0, None, None, 1)
    beta_rural_long_distance_bus = Beta('beta_rural_long_distance_bus', 0, None, None, 1)
    beta_rural_tour_bus = Beta('beta_rural_tour_bus', 0, None, None, 1)
    beta_rural_other = Beta('beta_rural_other', 0, None, None, 0)

    beta_region_geneva_train = Beta('beta_region_geneva_train', 0, None, None, 0)
    beta_region_lausanne_train = Beta('beta_region_lausanne_train', 0, None, None, 1)
    beta_region_neuchatel_train = Beta('beta_region_neuchatel_train', 0, None, None, 1)
    beta_region_fribourg_train = Beta('beta_region_fribourg_train', 0, None, None, 0)
    beta_region_biel_jura_train = Beta('beta_region_biel_jura_train', 0, None, None, 1)
    beta_region_westalpen_train = Beta('beta_region_westalpen_train', 0, None, None, 1)
    beta_region_basel_train = Beta('beta_region_basel_train', 0, None, None, 1)
    beta_region_berner_oberland_train = Beta('beta_region_berner_oberland_train', 0, None, None, 0)
    beta_region_aareland_train = Beta('beta_region_aareland_train', 0, None, None, 1)
    beta_region_zentralschweiz_train = Beta('beta_region_zentralschweiz_train', 0, None, None, 1)
    beta_region_zurich_train = Beta('beta_region_zurich_train', 0, None, None, 1)
    beta_region_sopraceneri_train = Beta('beta_region_sopraceneri_train', 0, None, None, 0)
    beta_region_sottoceneri_train = Beta('beta_region_sottoceneri_train', 0, None, None, 1)
    beta_region_bodensee_train = Beta('beta_region_bodensee_train', 0, None, None, 0)
    beta_region_ostalpen_train = Beta('beta_region_ostalpen_train', 0, None, None, 1)
    beta_region_bern_train = Beta('beta_region_bern_train', 0, None, None, 1)

    beta_region_geneva_bus = Beta('beta_region_geneva_bus', 0, None, None, 0)
    beta_region_lausanne_bus = Beta('beta_region_lausanne_bus', 0, None, None, 1)
    beta_region_neuchatel_bus = Beta('beta_region_neuchatel_bus', 0, None, None, 1)
    beta_region_fribourg_bus = Beta('beta_region_fribourg_bus', 0, None, None, 0)
    beta_region_biel_jura_bus = Beta('beta_region_biel_jura_bus', 0, None, None, 1)
    beta_region_westalpen_bus = Beta('beta_region_westalpen_bus', 0, None, None, 1)
    beta_region_basel_bus = Beta('beta_region_basel_bus', 0, None, None, 0)
    beta_region_berner_oberland_bus = Beta('beta_region_berner_oberland_bus', 0, None, None, 1)
    beta_region_aareland_bus = Beta('beta_region_aareland_bus', 0, None, None, 1)
    beta_region_zentralschweiz_bus = Beta('beta_region_zentralschweiz_bus', 0, None, None, 1)
    beta_region_zurich_bus = Beta('beta_region_zurich_bus', 0, None, None, 0)
    beta_region_sopraceneri_bus = Beta('beta_region_sopraceneri_bus', 0, None, None, 0)
    beta_region_sottoceneri_bus = Beta('beta_region_sottoceneri_bus', 0, None, None, 1)
    beta_region_bodensee_bus = Beta('beta_region_bodensee_bus', 0, None, None, 1)
    beta_region_ostalpen_bus = Beta('beta_region_ostalpen_bus', 0, None, None, 1)
    beta_region_bern_bus = Beta('beta_region_bern_bus', 0, None, None, 1)

    beta_region_geneva_bicycle = Beta('beta_region_geneva_bicycle', 0, None, None, 1)
    beta_region_lausanne_bicycle = Beta('beta_region_lausanne_bicycle', 0, None, None, 1)
    beta_region_neuchatel_bicycle = Beta('beta_region_neuchatel_bicycle', 0, None, None, 1)
    beta_region_fribourg_bicycle = Beta('beta_region_fribourg_bicycle', 0, None, None, 1)
    beta_region_biel_jura_bicycle = Beta('beta_region_biel_jura_bicycle', 0, None, None, 1)
    beta_region_westalpen_bicycle = Beta('beta_region_westalpen_bicycle', 0, None, None, 0)
    beta_region_basel_bicycle = Beta('beta_region_basel_bicycle', 0, None, None, 1)
    beta_region_berner_oberland_bicycle = Beta('beta_region_berner_oberland_bicycle', 0, None, None, 0)
    beta_region_aareland_bicycle = Beta('beta_region_aareland_bicycle', 0, None, None, 1)
    beta_region_zentralschweiz_bicycle = Beta('beta_region_zentralschweiz_bicycle', 0, None, None, 1)
    beta_region_zurich_bicycle = Beta('beta_region_zurich_bicycle', 0, None, None, 1)
    beta_region_sopraceneri_bicycle = Beta('beta_region_sopraceneri_bicycle', 0, None, None, 1)
    beta_region_sottoceneri_bicycle = Beta('beta_region_sottoceneri_bicycle', 0, None, None, 1)
    beta_region_bodensee_bicycle = Beta('beta_region_bodensee_bicycle', 0, None, None, 1)
    beta_region_ostalpen_bicycle = Beta('beta_region_ostalpen_bicycle', 0, None, None, 1)
    beta_region_bern_bicycle = Beta('beta_region_bern_bicycle', 0, None, None, 1)

    beta_region_geneva_tour_bus = Beta('beta_region_geneva_tour_bus', 0, None, None, 1)
    beta_region_lausanne_tour_bus = Beta('beta_region_lausanne_tour_bus', 0, None, None, 0)
    beta_region_neuchatel_tour_bus = Beta('beta_region_neuchatel_tour_bus', 0, None, None, 1)
    beta_region_fribourg_tour_bus = Beta('beta_region_fribourg_tour_bus', 0, None, None, 1)
    beta_region_biel_jura_tour_bus = Beta('beta_region_biel_jura_tour_bus', 0, None, None, 1)
    beta_region_westalpen_tour_bus = Beta('beta_region_westalpen_tour_bus', 0, None, None, 0)
    beta_region_basel_tour_bus = Beta('beta_region_basel_tour_bus', 0, None, None, 1)
    beta_region_berner_oberland_tour_bus = Beta('beta_region_berner_oberland_tour_bus', 0, None, None, 1)
    beta_region_aareland_tour_bus = Beta('beta_region_aareland_tour_bus', 0, None, None, 1)
    beta_region_zentralschweiz_tour_bus = Beta('beta_region_zentralschweiz_tour_bus', 0, None, None, 0)
    beta_region_zurich_tour_bus = Beta('beta_region_zurich_tour_bus', 0, None, None, 0)
    beta_region_sopraceneri_tour_bus = Beta('beta_region_sopraceneri_tour_bus', 0, None, None, 0)
    beta_region_sottoceneri_tour_bus = Beta('beta_region_sottoceneri_tour_bus', 0, None, None, 1)
    beta_region_bodensee_tour_bus = Beta('beta_region_bodensee_tour_bus', 0, None, None, 1)
    beta_region_ostalpen_tour_bus = Beta('beta_region_ostalpen_tour_bus', 0, None, None, 1)
    beta_region_bern_tour_bus = Beta('beta_region_bern_tour_bus', 0, None, None, 0)

    beta_region_geneva_long_distance_bus = Beta('beta_region_geneva_long_distance_bus', 0, None, None, 0)
    beta_region_lausanne_long_distance_bus = Beta('beta_region_lausanne_long_distance_bus', 0, None, None, 1)
    beta_region_neuchatel_long_distance_bus = Beta('beta_region_neuchatel_long_distance_bus', 0, None, None, 1)
    beta_region_fribourg_long_distance_bus = Beta('beta_region_fribourg_long_distance_bus', 0, None, None, 1)
    beta_region_biel_jura_long_distance_bus = Beta('beta_region_biel_jura_long_distance_bus', 0, None, None, 1)
    beta_region_westalpen_long_distance_bus = Beta('beta_region_westalpen_long_distance_bus', 0, None, None, 1)
    beta_region_basel_long_distance_bus = Beta('beta_region_basel_long_distance_bus', 0, None, None, 0)
    beta_region_berner_oberland_long_distance_bus = Beta('beta_region_berner_oberland_long_distance_bus', 0, None, None, 1)
    beta_region_aareland_long_distance_bus = Beta('beta_region_aareland_long_distance_bus', 0, None, None, 1)
    beta_region_zentralschweiz_long_distance_bus = Beta('beta_region_zentralschweiz_long_distance_bus', 0, None, None, 0)
    beta_region_zurich_long_distance_bus = Beta('beta_region_zurich_long_distance_bus', 0, None, None, 0)
    beta_region_sopraceneri_long_distance_bus = Beta('beta_region_sopraceneri_long_distance_bus', 0, None, None, 1)
    beta_region_sottoceneri_long_distance_bus = Beta('beta_region_sottoceneri_long_distance_bus', 0, None, None, 1)
    beta_region_bodensee_long_distance_bus = Beta('beta_region_bodensee_long_distance_bus', 0, None, None, 1)
    beta_region_ostalpen_long_distance_bus = Beta('beta_region_ostalpen_long_distance_bus', 0, None, None, 1)
    beta_region_bern_long_distance_bus = Beta('beta_region_bern_long_distance_bus', 0, None, None, 1)

    beta_region_geneva_other = Beta('beta_region_geneva_other', 0, None, None, 0)
    beta_region_lausanne_other = Beta('beta_region_lausanne_other', 0, None, None, 1)
    beta_region_neuchatel_other = Beta('beta_region_neuchatel_other', 0, None, None, 1)
    beta_region_fribourg_other = Beta('beta_region_fribourg_other', 0, None, None, 1)
    beta_region_biel_jura_other = Beta('beta_region_biel_jura_other', 0, None, None, 1)
    beta_region_westalpen_other = Beta('beta_region_westalpen_other', 0, None, None, 0)
    beta_region_basel_other = Beta('beta_region_basel_other', 0, None, None, 0)
    beta_region_berner_oberland_other = Beta('beta_region_berner_oberland_other', 0, None, None, 1)
    beta_region_aareland_other = Beta('beta_region_aareland_other', 0, None, None, 1)
    beta_region_zentralschweiz_other = Beta('beta_region_zentralschweiz_other', 0, None, None, 0)
    beta_region_zurich_other = Beta('beta_region_zurich_other', 0, None, None, 0)
    beta_region_sopraceneri_other = Beta('beta_region_sopraceneri_other', 0, None, None, 1)
    beta_region_sottoceneri_other = Beta('beta_region_sottoceneri_other', 0, None, None, 0)
    beta_region_bodensee_other = Beta('beta_region_bodensee_other', 0, None, None, 1)
    beta_region_ostalpen_other = Beta('beta_region_ostalpen_other', 0, None, None, 1)
    beta_region_bern_other = Beta('beta_region_bern_other', 0, None, None, 1)

    # Definition of new variables
    america = country == 1
    canada = country == 14
    north_america = (america + canada)
    germany = country == 5
    belgium = country == 3
    france = country == 6
    italy = country == 7
    spain = country == 15
    poland = country == 16
    denmark = country == 17
    czech_republic = country == 18
    austria = country == 19
    united_kingdom = country == 8
    japan = country == 12
    china = country == 2
    korea = country == 9
    east_asia = (china + japan + korea)
    brazil = country == 10
    russia = country == 13
    india = country == 20
    finland = country == 36
    luxembourg = country == 101
    netherlands = country == 111
    western_europe = austria + belgium + france + germany + luxembourg + netherlands
    norway = country == 125
    sweden = country == 189
    scandinavia = finland + norway + sweden
    northern_europe = denmark + scandinavia + united_kingdom
    australia = country == 2001
    new_zealand = country == 2016
    australasia = australia + new_zealand
    bahrain = country == 3004
    indonesia = country == 3067
    qatar = country == 3095
    kuwait = country == 3097
    malaysia = country == 3100
    oman = country == 3106
    saudi_arabia = country == 3121
    singapore = country == 3122
    thailand = country == 3135
    southeast_asia = indonesia + singapore + thailand + malaysia
    united_arab_emirates = country == 3151
    middle_east = (saudi_arabia + bahrain + qatar + kuwait + oman + united_arab_emirates)
    hotel = (accommodation_type == 1) + (accommodation_type == 7)
    holiday_homes = (accommodation_type == 2) + (accommodation_type == 3)
    camping = accommodation_type == 8
    collective_accommodation = (accommodation_type == 9) + (accommodation_type == 10) + (accommodation_type == 11)

    hotel_stars = stars * hotel * (stars > 0)

    # Definition of the utility functions
    V_train = ASC_train + \
              beta_germany_train * germany + beta_united_kingdom_train * united_kingdom + \
              beta_america_australasia_train * north_america + beta_east_asia_train * east_asia + \
              beta_middle_east_train * middle_east + beta_asia_train * china + beta_hotel_train * hotel + \
              beta_holiday_homes_train * holiday_homes + beta_camping_train * camping + \
              beta_collective_accommodation_train * collective_accommodation + beta_stars_train * hotel_stars + \
              beta_france_belgium_train * belgium + beta_france_belgium_train * france + beta_italy_train * italy + \
              beta_spain_train * spain + beta_poland_czech_republic_train * (poland + czech_republic) + \
              beta_america_australasia_train * brazil + beta_northern_europe_train * northern_europe + \
              beta_austria_train * austria + beta_scandinavia_train * scandinavia + \
              beta_finland_train * finland + beta_norway_train * norway + beta_sweden_train * sweden + \
              beta_denmark_train * denmark + beta_russia_train * russia + beta_asia_train * india + \
              beta_australia_train * australia + beta_new_zealand_train * new_zealand + \
              beta_asia_train * southeast_asia + beta_america_australasia_train * australasia + \
              beta_urban_train * urban + beta_rural_train * rural + \
              beta_region_geneva_train * region_geneva + \
              beta_region_lausanne_train * region_lausanne + \
              beta_region_neuchatel_train * region_neuchatel + \
              beta_region_fribourg_train * region_fribourg + \
              beta_region_biel_jura_train * region_biel_jura + \
              beta_region_westalpen_train  * region_westalpen + \
              beta_region_basel_train * region_basel + \
              beta_region_berner_oberland_train * region_berner_oberland + \
              beta_region_aareland_train * region_aareland + \
              beta_region_zentralschweiz_train * region_zentralschweiz + \
              beta_region_zurich_train * region_zurich + \
              beta_region_sopraceneri_train * region_sopraceneri + \
              beta_region_sottoceneri_train * region_sottoceneri + \
              beta_region_bodensee_train * region_bodensee + \
              beta_region_ostalpen_train * region_ostalpen + \
              beta_region_bern_train * region_bern
    V_bicycle = ASC_bicycle + beta_hotel_bicycle * hotel + \
              beta_holiday_homes_bicycle * holiday_homes + beta_camping_bicycle * camping + \
              beta_collective_accommodation_bicycle * collective_accommodation + beta_stars_bicycle * hotel_stars + \
              beta_germany_bicycle * germany + beta_united_kingdom_bicycle * united_kingdom + \
              beta_north_america_bicycle * north_america + beta_east_asia_bicycle * east_asia + \
              beta_china_bicycle * china + \
              beta_belgium_bicycle * belgium + beta_france_bicycle * france + beta_italy_bicycle * italy + \
              beta_spain_bicycle * spain + beta_russia_poland_czech_republic_bicycle * (poland + czech_republic) + \
              beta_brazil_bicycle * brazil + beta_denmark_scandinavia_bicycle * (denmark + scandinavia) + \
              beta_austria_bicycle * austria + beta_scandinavia_bicycle * scandinavia + \
              beta_norway_bicycle * norway + \
              beta_denmark_bicycle * denmark + beta_russia_poland_czech_republic_bicycle * russia + \
              beta_australia_bicycle * australia + \
              beta_southeast_asia_bicycle * southeast_asia + beta_australasia_bicycle * australasia + \
              beta_us_bicycle * america + \
              beta_canada_bicycle * canada + beta_urban_bicycle * urban + beta_rural_bicycle * rural + \
              beta_region_geneva_bicycle * region_geneva + \
              beta_region_lausanne_bicycle * region_lausanne + \
              beta_region_neuchatel_bicycle * region_neuchatel + \
              beta_region_fribourg_bicycle * region_fribourg + \
              beta_region_biel_jura_bicycle * region_biel_jura + \
              beta_region_westalpen_bicycle * region_westalpen + \
              beta_region_basel_bicycle * region_basel + \
              beta_region_berner_oberland_bicycle * region_berner_oberland + \
              beta_region_aareland_bicycle * region_aareland + \
              beta_region_zentralschweiz_bicycle * region_zentralschweiz + \
              beta_region_zurich_bicycle * region_zurich + \
              beta_region_sopraceneri_bicycle * region_sopraceneri + \
              beta_region_sottoceneri_bicycle * region_sottoceneri + \
              beta_region_bodensee_bicycle * region_bodensee + \
              beta_region_ostalpen_bicycle * region_ostalpen + \
              beta_region_bern_bicycle * region_bern
    V_car = ASC_car
    V_bus = ASC_bus + beta_hotel_bus * hotel + \
              beta_holiday_homes_bus * holiday_homes + beta_camping_bus * camping + \
              beta_collective_accommodation_bus * collective_accommodation + \
              beta_france_germany_bus * germany + beta_united_kingdom_bus * united_kingdom + \
              beta_north_america_bus * north_america + beta_east_asia_bus * east_asia + \
              beta_middle_east_bus * middle_east + beta_china_bus * china + \
              beta_belgium_bus * belgium + beta_france_germany_bus * france + beta_italy_spain_bus * italy + \
              beta_italy_spain_bus * spain + beta_poland_bus * poland + beta_czech_republic_bus * czech_republic + \
              beta_brazil_bus * brazil + beta_northern_europe_bus * northern_europe + \
              beta_austria_bus * austria + beta_scandinavia_bus * scandinavia + \
              beta_finland_bus * finland + beta_norway_bus * norway + beta_sweden_bus * sweden + \
              beta_denmark_bus * denmark + beta_russia_bus * russia + beta_india_bus * india + \
              beta_australia_bus * australia + beta_new_zealand_bus * new_zealand + \
              beta_southeast_asia_bus * southeast_asia + beta_australasia_bus * australasia + beta_japan_bus * japan + \
              beta_korea_bus * korea + beta_us_bus * america + beta_canada_bus * canada + \
              beta_stars_bus * hotel_stars + beta_urban_bus * urban + beta_rural_bus * rural + \
              beta_region_geneva_bus * region_geneva + \
              beta_region_lausanne_bus * region_lausanne + \
              beta_region_neuchatel_bus * region_neuchatel + \
              beta_region_fribourg_bus * region_fribourg + \
              beta_region_biel_jura_bus * region_biel_jura + \
              beta_region_westalpen_bus * region_westalpen + \
              beta_region_basel_bus * region_basel + \
              beta_region_berner_oberland_bus * region_berner_oberland + \
              beta_region_aareland_bus * region_aareland + \
              beta_region_zentralschweiz_bus * region_zentralschweiz + \
              beta_region_zurich_bus * region_zurich + \
              beta_region_sopraceneri_bus * region_sopraceneri + \
              beta_region_sottoceneri_bus * region_sottoceneri + \
              beta_region_bodensee_bus * region_bodensee + \
              beta_region_ostalpen_bus * region_ostalpen + \
              beta_region_bern_bus * region_bern
    V_tour_bus = ASC_tour_bus + beta_hotel_tour_bus * hotel + \
              beta_holiday_homes_tour_bus * holiday_homes + beta_camping_tour_bus * camping + \
              beta_collective_accommodation_tour_bus * collective_accommodation + \
              beta_germany_denmark_tour_bus * germany + beta_united_kingdom_tour_bus * united_kingdom + \
              beta_north_america_tour_bus * north_america + beta_east_asia_tour_bus * east_asia + \
              beta_middle_east_tour_bus * middle_east + beta_china_tour_bus * china + \
              beta_belgium_tour_bus * belgium + beta_france_tour_bus * france + beta_italy_tour_bus * italy + \
              beta_spain_tour_bus * spain + beta_russia_poland_czech_republic_tour_bus * (poland + czech_republic) + \
              beta_brazil_tour_bus * brazil + beta_northern_europe_tour_bus * northern_europe + \
              beta_austria_tour_bus * austria + beta_scandinavia_tour_bus * scandinavia + \
              beta_sweden_tour_bus * sweden + \
              beta_germany_denmark_tour_bus * denmark + beta_russia_poland_czech_republic_tour_bus * russia + \
              beta_india_tour_bus * india + \
              beta_australia_tour_bus * australia + beta_new_zealand_tour_bus * new_zealand + \
              beta_southeast_asia_tour_bus * southeast_asia + beta_australasia_tour_bus * australasia + \
              beta_japan_korea_tour_bus * (japan + korea) + beta_us_tour_bus * america + \
              beta_canada_tour_bus * canada + \
              beta_stars_tour_bus * hotel_stars + beta_urban_tour_bus * urban + beta_rural_tour_bus * rural + \
              beta_region_geneva_tour_bus * region_geneva + \
              beta_region_lausanne_tour_bus * region_lausanne + \
              beta_region_neuchatel_tour_bus * region_neuchatel + \
              beta_region_fribourg_tour_bus * region_fribourg + \
              beta_region_biel_jura_tour_bus * region_biel_jura + \
              beta_region_westalpen_tour_bus * region_westalpen + \
              beta_region_basel_tour_bus * region_basel + \
              beta_region_berner_oberland_tour_bus * region_berner_oberland + \
              beta_region_aareland_tour_bus * region_aareland + \
              beta_region_zentralschweiz_tour_bus * region_zentralschweiz + \
              beta_region_zurich_tour_bus * region_zurich + \
              beta_region_sopraceneri_tour_bus * region_sopraceneri + \
              beta_region_sottoceneri_tour_bus * region_sottoceneri + \
              beta_region_bodensee_tour_bus * region_bodensee + \
              beta_region_ostalpen_tour_bus * region_ostalpen + \
              beta_region_bern_tour_bus * region_bern
    V_long_distance_bus = ASC_long_distance_bus + beta_hotel_long_distance_bus * hotel + \
              beta_holiday_homes_long_distance_bus * holiday_homes + beta_camping_long_distance_bus * camping + \
              beta_collect_accomm_long_distance_bus * collective_accommodation + \
              beta_stars_long_distance_bus * hotel_stars + beta_china_long_distance_bus * china + \
              beta_india_long_distance_bus * india + beta_poland_long_distance_bus * poland + \
              beta_brazil_long_distance_bus * brazil + beta_urban_long_distance_bus * urban + \
              beta_rural_long_distance_bus * rural + \
              beta_region_geneva_long_distance_bus * region_geneva + \
              beta_region_lausanne_long_distance_bus * region_lausanne + \
              beta_region_neuchatel_long_distance_bus * region_neuchatel + \
              beta_region_fribourg_long_distance_bus * region_fribourg + \
              beta_region_biel_jura_long_distance_bus * region_biel_jura + \
              beta_region_westalpen_long_distance_bus * region_westalpen + \
              beta_region_basel_long_distance_bus * region_basel + \
              beta_region_berner_oberland_long_distance_bus * region_berner_oberland + \
              beta_region_aareland_long_distance_bus * region_aareland + \
              beta_region_zentralschweiz_long_distance_bus * region_zentralschweiz + \
              beta_region_zurich_long_distance_bus * region_zurich + \
              beta_region_sopraceneri_long_distance_bus * region_sopraceneri + \
              beta_region_sottoceneri_long_distance_bus * region_sottoceneri + \
              beta_region_bodensee_long_distance_bus * region_bodensee + \
              beta_region_ostalpen_long_distance_bus * region_ostalpen + \
              beta_region_bern_long_distance_bus * region_bern
    V_other = ASC_other + beta_hotel_other * hotel + \
              beta_holiday_homes_other * holiday_homes + beta_camping_other * camping + \
              beta_collective_accommodation_other * collective_accommodation + beta_stars_other * hotel_stars + \
              beta_urban_other * urban + beta_rural_other * rural + \
              beta_region_geneva_other * region_geneva + \
              beta_region_lausanne_other * region_lausanne + \
              beta_region_neuchatel_other * region_neuchatel + \
              beta_region_fribourg_other * region_fribourg + \
              beta_region_biel_jura_other * region_biel_jura + \
              beta_region_westalpen_other * region_westalpen + \
              beta_region_basel_other * region_basel + \
              beta_region_berner_oberland_other * region_berner_oberland + \
              beta_region_aareland_other * region_aareland + \
              beta_region_zentralschweiz_other * region_zentralschweiz + \
              beta_region_zurich_other * region_zurich + \
              beta_region_sopraceneri_other * region_sopraceneri + \
              beta_region_sottoceneri_other * region_sottoceneri + \
              beta_region_bodensee_other * region_bodensee + \
              beta_region_ostalpen_other * region_ostalpen + beta_region_bern_other * region_bern

    # Associate utility functions with the numbering of alternatives
    V = {1: V_train, 2: V_bus, 3: V_car, 6: V_long_distance_bus, 7: V_tour_bus, 8: V_bicycle, 9: V_other}

    # Associate the availability conditions with the alternatives
    av = {1: 1, 2: 1, 3: 1, 6: 1, 7: 1, 8: 1, 9: 1}

    # Definition of the model. This is the contribution of each
    # observation to the log likelihood function.
    logprob = models.loglogit(V, av, transport_mode)

    # Change the working directory, so that biogeme writes in the correct folder
    standard_directory = os.getcwd()
    output_directory = Path('data/output/')
    os.chdir(output_directory)

    # Create the Biogeme object
    biogeme = bio.BIOGEME(database, logprob)
    biogeme.modelName = 'mode_choice_tourists'

    # Calculate the null log likelihood for reporting.
    biogeme.calculateNullLoglikelihood(av)

    # Estimate the parameters
    results = biogeme.estimate()

    # Get the results in a pandas table
    pandasResults = results.getEstimatedParameters()

    results.writeLaTeX()

    # Go back to the normal working directory
    os.chdir(standard_directory)


if __name__ == '__main__':
    run()
