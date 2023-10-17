def lightning(color,lColors, speed = 0.1):
    delay = random.random() + 0.01
    np.fill(color)
    np.show()
    time.sleep(delay)
    ind = random.randint(0, 1)
    for i in range(random.randint(1,2)):
        np.fill(lColors[ind])
        np.show()
        time.sleep(0.1)
        np.fill([0,0,0])
        np.show()
    np.fill(color)
    np.show()
