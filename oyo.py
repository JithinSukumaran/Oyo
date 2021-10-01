import scrapy
import json 

class OyoSpider(scrapy.Spider):
    name = 'oyo'
    allowed_domains = ['www.oyorooms.com']
    start_urls = ['https://www.oyorooms.com/api/pwa/search/hotels?fields=id%2Cname%2Ccity%2Cstreet%2Ccategory%2Cgeo_location%2Ccategory%2Chotel_type%2Calternate_name%2Ccountry_name%2Ccountry_id%2Cshort_address%2Caddress%2Chotel_name_without_category%2Ccategorywise_images%2Ccategory_wise_media%2Ccategory_availability%2Cexternal_booking_url%2Cstatus&additional_fields=hotel_badge%2Ccategory_info%2Ccancellation_policies%2Cbest_image%2Croom_pricing%2Cavailability%2Camenities%2Crestrictions%2Ccategory%2Ccaptains_info%2Cnew_applicable_filters%2Cadditional_charge_info%2Cimages%2Chotel_images%2Ccollection_filtered_count%2Cpopular_location_range%2Cguest_ratings%2Coyo_wizard%2Curgency_info%2Coyo_owner_discount%2Ccategory_wise_pricing&tax_exclusive_pricing=true&available_room_count%5Bcheckin%5D=01%2F10%2F2021&available_room_count%5Bcheckout%5D=02%2F10%2F2021&available_room_count%5Bmin_count%5D=1&filters%5Bcity_id%5D=2&filters%5Ball_room_categories%5D=true&pre_apply_coupon_switch=true&search_redirection_enabled=true&rooms_config=0%2C1%2C0&requested_coupon=&services=meals&source=Web%20Booking&format_response%5Bbatch%5D%5Bcount%5D=1320&format_response%5Bbatch%5D%5Boffset%5D=0&format_response%5Bsort_params%5D%5Bsort_on%5D=&format_response%5Bsort_params%5D%5Bascending%5D=true&locale=en']

    def parse(self, response):
        resp = json.loads(response.body)
        hotels = resp.get('hotels')
        for hotel in hotels:
            yield{
                'Hotel Name':hotel.get('name'),
                'Price':hotel.get('mrcData')[0].get('finalPrice'),
                'Room Type': hotel.get('room_categories_with_data')[0].get('name'),
                'Rating':hotel.get('ratings').get('value'),
                'Number of ratings':hotel.get('ratings').get('count'),
                'Available Rooms':hotel.get('room_categories_with_data')[0].get('available_rooms')[0],
                'Max Occupancy Allowed':hotel.get('room_categories_with_data')[0].get('max_occupancy_allowed'),
                'Address':hotel.get('address'),
                'Lat':hotel.get('latitude'),
                'Long':hotel.get('longitude'),
                'Map Link':hotel.get('map_link'),
                'Images':hotel.get('images'),
                'Oyo ID':hotel.get('oyo_id')
            }

