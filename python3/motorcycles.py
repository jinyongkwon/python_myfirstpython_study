if __name__ == '__main__':
    motorcycles = ['honda', 'yamaha', 'suzuki']
    print(motorcycles)
    motorcycles[0] = 'ducati'
    print(motorcycles)
    last_owned = motorcycles.pop()
    print(last_owned, motorcycles)
