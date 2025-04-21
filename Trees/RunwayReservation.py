from Trees.Request import Request


class RunwayReservation:
    def __init__(self):
        # n is the number of requests, k is the grace period between requests
        n, k = map(int, input().strip().split())
        self.requests = []

    def main(self):
        while True:
            try:
                line = input().strip().split()
                cmd = line[0]
                time = int(line[1])

                if cmd == 'r':
                    flightname = line[2]
                    flightnumber = line[3]
                    source = line[4]
                    destination = line[5]

                    self.requests.append(Request('r', time, flightname, flightnumber, source, destination))
                else:
                    self.requests.append(Request('t', time))

            except EOFError:
                break

        # todo: Implement the logic to process the requests



if __name__ == '__main__':
    runwayReservation = RunwayReservation()
    runwayReservation.main()
