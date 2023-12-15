import drivers
from time import sleep
from datetime import datetime
from subprocess import check_output
import psutil
from gpiozero import CPUTemperature

display = drivers.Lcd()
IP = check_output(["hostname", "-I"], encoding="utf8").split()[0]

try:
    print("Writing to display")
    while True:
        # Saat gösterimi
        current_time = datetime.now().strftime("%H:%M:%S")
        display.lcd_display_string("Saat: ", 1)
        display.lcd_display_string("{}".format(current_time), 2)
        sleep(1.5)
        display.lcd_clear()

        # Tarih gösterimi
        current_date = datetime.now().strftime("%d-%m-%Y")
        display.lcd_display_string("Tarih: ", 1)
        display.lcd_display_string("{}".format(current_date), 2)
        sleep(1.5)
        display.lcd_clear()

        # IP Adresi gösterimi
        display.lcd_display_string("IP: ", 1)
        display.lcd_display_string("{}".format(IP), 2)
        sleep(1.5)
        display.lcd_clear()

        # CPU Kullanımı, GPU Kullanımı ve Sıcaklık gösterimi
        cpu_usage = psutil.cpu_percent()
        gpu_usage = 0  # Raspberry Pi'da genellikle GPU kullanımı standart bir şekilde ölçülemez
        cpu_temp = CPUTemperature().temperature
        display.lcd_display_string("CPU:", 1)
        display.lcd_display_string("{}%".format(cpu_usage), 2)
        sleep(1.5)
        display.lcd_clear()
        display.lcd_display_string("GPU:", 1)
        display.lcd_display_string("{}%".format(gpu_usage), 2)
        sleep(1.5)
        display.lcd_clear()
        display.lcd_display_string("Sıcaklık:",1)
        display.lcd_display_string("{} Derece".format(cpu_temp), 2)
        sleep(1.5)
        display.lcd_clear()

except KeyboardInterrupt:
    # Eğer bir KeyboardInterrupt (ctrl+c'ye basıldığında) olursa, programı kapat ve temizlik yap
    print("Cleaning up!")
    display.lcd_clear()