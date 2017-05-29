class UAV:

    numUAVs = 0

    def __init__(self, frame = None, numMotors = None):
        self.frame = frame or 'hexa'
        self.motors = numMotors or 6
        UAV.numUAVs += 1
