<h1 align="center">:triangular_ruler: Engineer helper (beta)</h1>

____

## Описание

***Engineer helper*** (desktop приложение) - набор калькуляторов для инженеров.

Интерфейс приложения прост и интуитивно понятен, что позволяет быстро освоить его и начать использовать для решения
своих задач. Калькулятор поможет вам сэкономить время и повысить точность расчетов, делая
вашу работу более эффективной и продуктивной.



+ **Узконаправленные**
    + ГОСТ 34347-2017
        + Термообработка
        + Утонение патрубка
    + Геометрические
        + Развертка обечайки
        + Длина дуги
        + Длина окружности
        + Размер по дуге
    + Массы
        + Кольцо укрепляющее
+ **Металлопрокат**
    + Уголки
        + Уголки равнополочные
        + Уголки неравнополочные
    + Кругляк
    + Квадрат
    + Лист
    + Труба
    + Профильная труба

____

## Обратная связь

Буду благодарен за любой фидбэк по коду и его улучшению. Напишите мне в [telegram](https://t.me/uchvatov)

____

## Использование

Приложение не требует установки, достаточно просто скачать файл ***Engineer helper 1.0.1.exe*** в корневой папке
проекта.

+ Операционная система: windows
+ Протестировано на системе: windows 10, 11

____

## Развертывание проекта
Приложение создано с помощью библиотеки PyQt.

*Создать окружение*
```
python -m venv venv_app
```

*Установить пакеты из requirements.txt*
```
pip install -r requirements.txt
```

*Для компоновки приложения в один исполняемый файл использован `Pyinstaller`*
```
pyinstaller my_cpec.spec
```
Будет создано две папки `build` и `dist`, файл .exe будет находиться в папке `dist` 
____

## Скриншоты приложения

#### Меню

![узконаправленные](https://e.radikal.host/2023/11/19/image561710efb9ec5411.png)
![металлопрокат](https://e.radikal.host/2023/11/19/image936cc43a0b5d904f.png)

#### Пример виджета "Расчет массы уголка равнополочного"

![калькулятор1](https://e.radikal.host/2023/11/19/imagea91e43c9a23c436a.png)

#### Пример виджета "Масса кольца укрепляющего"

![калькулятор2](https://e.radikal.host/2023/11/19/image655e2bfebe7e145b.png)





