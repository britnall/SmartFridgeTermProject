from multiprocessing import Process


def temp_sensor():
    import temp_sensing
    temp_sensing.main()


def light_sensor():
    import light_sensing
    light_sensing.main()


p1 = Process(target=temp_sensor)
p1.start()

p2 = Process(target=light_sensor)
p2.start()
