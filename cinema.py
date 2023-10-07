class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,rows, cols, hall_no) -> None:
        self.seats = {}
        self._show_list = []
        self.__rows = rows
        self.__cols = cols
        self.__hall_no = hall_no
        super().entry_hall(self)

    def entry_show(self,id, movie_name, time):
        show = (id, movie_name, time)
        self._show_list.append(show)
        
        dd = []
        for i in range (0, self.__rows):
            row = []
            for j in range (0, self.__cols):
                row.append(0)
            dd.append(row)

        self.seats[id] = dd
    
    def book_seats(self,ID, *seats):
        if ID in self.seats:
            for r, c in seats:
                if 1 <= r <= self.__rows and 1 <= c <= self.__cols:
                    if self.seats[ID][r-1][c-1] == 1:
                        print(f'\tSeat {(r,c)} already booked!')

                    else:
                        self.seats[ID][r - 1][c - 1] = 1  
                        print(f'\tBooked seats: {(r,c)}!')
                    
                else:
                    print(f'\tSeat {(r,c)} is Invalid!')
        else:
            print(f'\tInvalid show id {ID}')

    def view_show_list(self):
            print(f'\n\tHere are the ongoing shows:\n')
            print("ID  ","Movie Name", "Date and Time")
            for shows in self._show_list:
                print(shows[0]," ", shows[1],"   ", shows[2])
       

    def view_available_seats(self, id):
        if id in self.seats:
            print("\n\t Here are Available Seats (marked with '0'):\n")
            seats = self.seats[id]
            for i in range(0, self.__rows):
                for j in range(0, self.__cols):
                    print(seats[i][j], end=' ')
                print()
        else:
            print("\n\tInvalid ID.")

                
Anondo = Hall(40,40,1)
Anondo.entry_show("11", "jamjam", "07/10/23 10:00")
Anondo.entry_show("12", "komkom", "07/10/23 12:00")
Anondo.entry_show("13", "tomtom", "07/10/23 4:00")
Anondo.entry_show("14", "yamyam", "07/10/23 6:00")

while(True):
    print("\n\t****** Welcome to STAR CINEMA ******")
    print("\nHow can we help you? Please choose an option:")
    print("Option 1: View ongoing shows.")
    print("Option 2: View available seats.")
    print("Option 3: Book Tickets.")
    print("Last: Press anyohter number to Exit!")
    op = int(input("I choose option: "))
    if op == 1:
        Anondo.view_show_list()
        
    elif op == 2:
        id = input("Enter ID of the show: ")
        Anondo.view_available_seats(id)

    elif op == 3:
        id = input("Enter ID of the show you want to watch: ")
        cnt = int(input("How many seats do you want? : "))
        if cnt <= 4:
            while cnt!= 0:
                seat = list(map(int, input("Enter row and column of the seat you want: ").split()))
                r = seat[0]
                c = seat[1]
                Anondo.book_seats(id, (r,c))
                cnt -= 1
        else:
            print("\nYou can only book upto 4 seats at a time!!")
            print("Please try again.\n")
    else:
        print("Thank you for visiting Star Cinema!")
        break


