from Request import Request
from BST import BST
import sys

class RunwayReservation:
    def __init__(self):
        # n is the number of requests, k is the grace period between requests
        n, self.k = map(int, input().strip().split())
        self.current_time = 0
        self.requests = []
        self.runway = BST()

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
        self.process()

    def process(self):
        for request in self.requests:
            if request.command == 'r':
                self.handle_r(request)
            if request.command == 't':
                self.handle_t(request.time)

    def handle_r(self, request: Request):
        pred = self.runway.pred(request.time)
        succ = self.runway.succ(request.time)
        if (pred is None or request.time - pred.val >= self.k) and (succ is None or succ.val - request.time >= self.k):
            self.runway.insert(request.time, request)

    def handle_t(self, new_time: int):
        print(f"Current time = {new_time}")
        self.current_time += new_time

        while self.runway.size > 0:
            min_node = self.runway.min()
            if min_node.val > self.current_time:
                break
            
            print(min_node.req)
            self.runway.delete(min_node.val)


if __name__ == '__main__':
    runwayReservation = RunwayReservation()
    runwayReservation.main()
