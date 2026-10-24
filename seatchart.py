
def load_seats():
    #if file is present already
    try:
        with open("seats.txt", "r") as f:
            return f.read().split(",")
    #else
    except FileNotFoundError:
        return ["free"] * 10

def save_seats(seats):
    with open("seats.txt", "w") as f:
        f.write(",".join(seats))


def show_seats(seats):
    for i in range(len(seats)):
        print(f"seat{i}:{seats[i]}")


def book_seats(seats, n):
    if n < 0 or n >= len(seats):
        return "invalid seat number"
    if seats[n] == "booked":
        return "seat is already booked"

    seats[n] = "booked"
    return "seat booked successfully"


seats = load_seats()
print(book_seats(seats, 2))
print(book_seats(seats, 2))
show_seats(seats)
save_seats(seats)

