import phonenumbers
from test import number

from phonenumbers import gecoder
ch_nmber = phonenumbers.parse(number, "9353039524")
print(geocoder.description_for_number(ch_nmber,"en"))

from phonenumbers import carrier
service_nmber = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_nmber, "en"))