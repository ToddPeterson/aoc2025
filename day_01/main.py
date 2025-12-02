DIAL_SIZE = 100
DIAL_INITIAL_POSITION = 50


class Dial:
    def __init__(self):
        self._position = DIAL_INITIAL_POSITION
        self.zero_count = 0
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, val):
        self._position = val % DIAL_SIZE
        if self._position == 0:
            self.zero_count += 1
    
    def rotate(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'L':
            distance *= -1
        
        old_count = self.zero_count
        self.position += distance
        print(f'The dial rotated {instruction} to point at {self.position}')
        if self.zero_count != old_count:
            print(f'  Crossed zero {self.zero_count - old_count} times (total: {self.zero_count})')


class Dial2:
    def __init__(self):
        self.position = DIAL_INITIAL_POSITION
        self._zero_count = 0
    
    @property
    def zero_count(self):
        return self._zero_count // 2
    
    def rotate(self, instruction):
        direction = instruction[0]
        distance = int(instruction[1:])

        if direction == 'L':
            distance *= -1
        
        prev = self.position
        self.position += distance

        prev_lo = prev // 100
        curr_lo = self.position // 100
        prev_hi = (prev - 1) // 100
        curr_hi = (self.position - 1) // 100

        self._zero_count += abs(prev_lo - curr_lo) + abs(prev_hi - curr_hi)


def main():
    file_path = 'input.txt'
    dial = Dial2()

    try:
        with open(file_path, 'r') as file:
            for line in file:
                dial.rotate(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    print(f'Zero count: {dial.zero_count}')


if __name__ == "__main__":
    main()
