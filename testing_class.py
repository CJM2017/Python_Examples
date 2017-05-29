from UAV import UAV


if __name__ == "__main__":
    myUav = UAV('quad',4)
    print(myUav.frame)
    print(myUav.motors)