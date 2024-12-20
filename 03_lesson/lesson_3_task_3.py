from address import Address
from mailing import Mailing

to_address = Address("1488", "Tver", "Lenina", "14", "88")
from_address = Address("1312", "Sizran", "Lenina", "13", "12")
mailing = Mailing(to_address, from_address, 300, "TrackNumber")

print (f"Track: {mailing.track}")
print (f"From: {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street},"
       f" {mailing.from_address.house}, {mailing.from_address.apartment}")
print (f"To: {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, "
       f"{mailing.to_address.house}, {mailing.to_address.apartment}")
print (f"Cost: {mailing.cost}")

