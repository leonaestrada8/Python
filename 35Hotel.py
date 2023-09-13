#3.5 HOTEL ORIGINAL - ANTES DA REFATORAÇÃO

class HotelReservation:
    def book_room(self, room_type, days, is_vip):
        price = 0
        if room_type == "Single":
            price = 100
        elif room_type == "Double":
            price = 200
        elif room_type == "Suite":
            price = 300
        else:
            return "Tipo de quarto invalido."

        if is_vip:
            price *= 0.9

        return f"Reserva efetuada: {room_type} por {days} dias. Preco: {price * days}"

reservation = HotelReservation()
print(reservation.book_room("Single", 3, True))

