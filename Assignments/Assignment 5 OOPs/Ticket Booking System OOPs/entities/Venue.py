class Venue:
    def __init__(self, venue_name, address):
        self._venue_name = venue_name
        self._address = address

    @property
    def venue_name(self):
        return self._venue_name

    @venue_name.setter
    def venue_name(self, value):
        self._venue_name = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    def display_venue_details(self):
        print(f"Venue Name = {self._venue_name}")
        print(f"Address of venue = {self._address}")
