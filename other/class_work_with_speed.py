class A:
    def __init__(self, speed, distance):
        self.speed = speed
        self.distance = distance

    def time(self):
        result = '%.2f' % (float(self.distance / self.speed))
        for_operation = str(result).split('.')
        minut = 60 / 100 * int(for_operation[1])
        return 'До цели ' + for_operation[0] + ' часов, ' + str(int(minut)) + ' минут.' if int(
            for_operation[0]) > 0 else 'До цели ' + str(int(minut)) + ' минут.'


print(A(speed=100, distance=50).time())
