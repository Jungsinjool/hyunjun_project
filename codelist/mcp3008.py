import spidev
import time
# sensor check interval
delay = 0.5
# MCP3008 CH0 채널 사용
ldr_channel = 0
# SPI instance 생성
spi = spidev.SpiDev()
# SPI 시작 (SPI bus Number, SPI CS number)
spi.open(0, 0)
# SPI clock
spi.max_speed_hz = 100000
# read data from a ADC channel(CH0 ~ CH7)
def SPI_read_adc(channel):
    r = spi.xfer2([1, 8 + channel << 4, 0])
    data = ((r[1] & 3) << 8) + r[2]
    return data
while True:
    ldr_value = SPI_read_adc(ldr_channel) # read CH0
    print("LDR messured value: %d" % ldr_value)
    time.sleep(delay)