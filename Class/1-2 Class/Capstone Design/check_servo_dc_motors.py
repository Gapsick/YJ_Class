import Jetson.GPIO as GPIO
import time
import subprocess

# Function to run shell commands with sudo
def run_command(command):
    subprocess.run(f"sudo {command}", shell=True, check=True)

# Check if busybox is installed; if not, install it
try:
    subprocess.run("busybox --help", shell=True, check=True)
    print("busybox is already installed.")
except subprocess.CalledProcessError:
    print("busybox not found. Installing...")
    run_command("apt update && apt install -y busybox")

# Define devmem commands for enabling PWM
commands = [
    "busybox devmem 0x700031fc 32 0x45",
    "busybox devmem 0x6000d504 32 0x2",
    "busybox devmem 0x70003248 32 0x46",
    "busybox devmem 0x6000d100 32 0x00"
]

# Execute each devmem command
for command in commands:
    run_command(command)

# 서보 모터 설정
servo_pin = 32  # 서보 모터가 연결된 핀 (PWM 신호)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(servo_pin, GPIO.OUT)
servo = GPIO.PWM(servo_pin, 50)  # 50Hz PWM 신호
servo.start(0)

# DC 모터 설정
dir_pin = 29  # 방향 제어 핀 (DIR)
pwm_pin = 33  # 속도 제어 핀 (PWM)

GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(pwm_pin, GPIO.OUT)

dc_motor = GPIO.PWM(pwm_pin, 1000)  # 1kHz PWM 신호
dc_motor.start(0)  # 초기 속도 0으로 설정

# 서보 모터 각도 설정 함수
def set_servo_angle(angle):
    duty_cycle = 2.5 + (angle / 180) * 10
    servo.ChangeDutyCycle(duty_cycle)
    time.sleep(0.3)
    servo.ChangeDutyCycle(0)

# DC 모터 제어 함수
def control_dc_motor(direction, speed):
    GPIO.output(dir_pin, direction)  # 방향 설정 (True: 정방향, False: 역방향)
    dc_motor.ChangeDutyCycle(speed)  # 속도 설정 (0~100)

# 메인 루프: 서보 모터 및 DC 모터 제어
try:
    while True:
        print("\n1: 서보 모터 제어")
        print("2: DC 모터 제어")
        choice = int(input("선택: "))

        if choice == 1:
            angle = int(input("서보 각도 입력 (0-180): "))
            set_servo_angle(angle)

        elif choice == 2:
            direction_input = input("모터 방향 (f: 정방향, b: 역방향): ")
            speed = int(input("모터 속도 (0-100): "))

            if direction_input.lower() == 'f':
                control_dc_motor(True, speed)
            elif direction_input.lower() == 'b':
                control_dc_motor(False, speed)

finally:
    # 종료 시 모든 핀 정리
    servo.stop()
    dc_motor.stop()
    GPIO.cleanup()
