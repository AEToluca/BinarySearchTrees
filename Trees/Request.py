
class Request:
    class Airline:
        def __init__(self, name: str, number: str, source: str, destination: str):
            self.name = name
            self.number = number
            self.source = source
            self.destination = destination

        def __str__(self):
            return f"{self.name} {self.number} {self.source} {self.destination}"


    def __init__(self, command: str, time: int, name: str="", number: str="", source: str="", destination: str=""):
        self.command = command
        self.time = time
        if command == "r":
            self.airline = self.Airline(name, number, source, destination)
        else:
            self.airline = None

    def __str__(self):
        return f"{self.airline}"
                   