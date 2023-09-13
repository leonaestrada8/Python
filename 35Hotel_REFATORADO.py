#3.5 HOTEL REFATORADO

class HotelReservation2:
    SINGLE_ROOM_PRICE = 100
    DOUBLE_ROOM_PRICE = 200
    SUITE_ROOM_PRICE = 300
    VIP_DISCOUNT = 0.9

    def book_room(self, room_type, days, is_vip):
        price = self.calculate_price(room_type, is_vip)
        if price <= 0:
            return "Tipo de quarto inválido."
        return f"Reserva efetuada: {room_type} por {days} dias. Preço: {price * days}"

    def calculate_price(self, room_type, is_vip):
        price_mapping = {
            "Single": HotelReservation2.SINGLE_ROOM_PRICE,
            "Double": HotelReservation2.DOUBLE_ROOM_PRICE,
            "Suite": HotelReservation2.SUITE_ROOM_PRICE
        }
        price = price_mapping.get(room_type, 0)
        if is_vip:
            price *= HotelReservation2.VIP_DISCOUNT
        return price

reservation = HotelReservation2()
print(reservation.book_room("Single", 3, True))

