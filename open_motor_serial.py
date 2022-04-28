from json.decoder import JSONDecoder
import serial
import json
import time

class open_motor:

    def __init__(self):
        self.ser = serial.Serial()
        self.pos_pid_msg = {}
        self.vel_pid_msg = {}
        self.pid_config_msg = {}
        self.msg_data = {}
        self._port = None
        self._baudrate = None
        self._timeout = None

    def init_serial_port(self, port, baudRate, timeout):
        self._port = port
        self._baudrate = baudRate
        self._timeout = timeout
        self.ser = serial.Serial(self._port, self._baudrate, timeout=self._timeout)


    def send_pwm_goal(self,pwm0,pwm1,pwm2,pwm3):
        self.msg_data["command"] = "pwm_direct"
        self.msg_data["pwm0"] = pwm0
        self.msg_data["pwm1"] = pwm1
        self.msg_data["pwm2"] = pwm2
        self.msg_data["pwm3"] = pwm3

        msg = json.dumps(self.msg_data).encode("ascii")

        self.ser.write(msg)


    def send_vel_goal(self,vel0,vel1,vel2,vel3):
        self.msg_data["command"] = "vel_pid"
        self.msg_data["vel0"] = vel0
        self.msg_data["vel1"] = vel1
        self.msg_data["vel2"] = vel2
        self.msg_data["vel3"] = vel3

        msg = json.dumps(self.msg_data).encode("ascii")

        self.ser.write(msg)

    def send_pos_goal(self,pos0,pos1,pos2,pos3):
        self.msg_data["command"] = "pos_pid"
        self.msg_data["pos0"] = pos0
        self.msg_data["pos1"] = pos1
        self.msg_data["pos2"] = pos2
        self.msg_data["pos3"] = pos3

        msg = json.dumps(self.msg_data).encode("ascii")

        self.ser.write(msg)


    def get_response(self):
        self.ser.flushInput()
        data = self.ser.readline().decode("utf-8")
        return data

    def get_response_json(self):
        data = self.get_response()
        json_data = json.loads(data)
        return json_data

    def isOpen(self):
       return self.ser.is_open
    # def wait_for_response(self):
    #     response = "string"
    #     while(response != "msg_recieved"):
    #         response = self.get_response()
        

    






