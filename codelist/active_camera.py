#!/usr/bin/python3
from gpiozero import MotionSensor, PWMOutputDevice
from picamera2 import Picamera2, Preview
from time import sleep
import time

# PIR 센서 (GPIO 4)
pir = MotionSensor(4)

# 패시브 버저 (GPIO 17)
buzzer = PWMOutputDevice(17)

# 카메라 설정
camera = Picamera2()
camera_config = camera.create_preview_configuration()
camera.configure(camera_config)

camera.start_preview(Preview.QTGL)
camera.start()

i = 0

def motion_detected():
    global i
    i += 1

    print("움직임 감지!")

    # 파일 이름 (시간 포함)
    filename = f'image_{int(i)}.jpg'
    camera.capture_file(filename)
    print(f"{filename} 저장 완료")rh

    # 🔊 버저 경고음 (5초)
    print("경고음 시작")

    buzzer.frequency = 1000   # 1000Hz (삐 소리)
    buzzer.value = 0.5        # 소리 ON

    sleep(5)

    buzzer.value = 0          # 소리 OFF
    print("경고음 종료")

    # 연속 감지 방지 (센서 안정화)
    sleep(2)

# 움직임 감지 시 실행
pir.when_motion = motion_detected

print("📷 움직임 감지 시스템 작동 중...")

try:
    while True:
        sleep(1)

except KeyboardInterrupt:
    print("프로그램 종료")
    camera.stop_preview()
    camera.stop()