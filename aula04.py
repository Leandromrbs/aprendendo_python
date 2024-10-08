import schedule
import time
from plyer import notification

def alert(title, message):
    notification.notify(
        title=title,
        message=message,
        app_name='Alerta do Windows',
        timeout=10
    )

def msg():
    alert('Alerta do Windows', 'Hora de Trabalhar!!')


if __name__ == '__main__':
    schedule.every().day.at('12:52:00').do(msg)

    while True:
        schedule.run_pending()
        time.sleep(1)
