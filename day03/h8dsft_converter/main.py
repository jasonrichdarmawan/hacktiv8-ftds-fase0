# 1. Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke 
#    celcius, dan celcius ke kelvin.
# 2. Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
#    Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah 
#    celcius atau kelvin. Panggil function yang pertama jika diperlukan.
# 3. Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. 
#    Berikan argumen untuk memastikan bahwa outputny adalah celcius atau kelvin.
# 4. Berikan dokumentasi pada setiap baris kode yang kalian tulis.

from enum import Enum
from typing import Literal

from numpy import isin

class Temperature:
    "class must be initialized before using the method"
    __temperature: float
    __scale: Literal["Celcius", "Kelvin", "Fahrenheit"]

    # constructor.
    def __init__(self, temperature: int, scale: Literal["Celcius", "Kelvin", "Fahrenheit"]):
        self.SetTemperature(temperature, scale)

    # __setTemperature == method that can't be accessed outside of the class.
    # setTemperature(sellf, temperature) == method that can't be accessed
    # before class initialization
    def SetTemperature(self, temperature: int, scale: Literal["Celcius", "Kelvin", "Fahrenheit"]):
        "method to change the temperature"
        if scale not in ["Celcius", "Kelvin", "Fahrenheit"]:
            raise ValueError(f'scale {scale} is illegal')

        # casting to make sure the args type is correct.
        self.__temperature = float(temperature)
        self.__scale = str(scale)

    # 1. Buatlah sebuah function yang dapat mengkonversi suhu dari kelvin ke 
    #    celcius, dan celcius ke kelvin.
    def Print(self, scale: Literal['Celcius', 'Kelvin', 'Fahrenheit']):
        "method to print the temperature in a specific scale"
        if scale not in ["Celcius", "Kelvin", "Fahrenheit"]:
            return ValueError("scale's value is illegall")

        if scale == "Celcius":
            return self.ToCelcius()
        if scale == "Kelvin":
            return self.ToKelvin()
        if scale == "Fahrenheit":
            return self.ToFahrenheit()

    # 3. Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. 
    #    Berikan argumen untuk memastikan bahwa outputny adalah celcius atau kelvin.
    def ToCelcius(self) -> str:
        "method to print the temperature in Celcius scale"
        if self.__scale == "Kelvin":
            return f'{(self.__temperature - 273.15):.2f} Celcius'
        if self.__scale == "Fahrenheit":
            return f'{((self.__temperature - 32) * 5/9):.2f} Celcius'
        return f'{self.__temperature:.2f} {self.__scale}'
    
    # 3. Buatlah sebuah function yang dapat mengkonversi suhu dari fahrenheit. 
    #    Berikan argumen untuk memastikan bahwa outputny adalah celcius atau kelvin.
    def ToKelvin(self) -> str:
        "method to print the temperature in Kelvin scale"
        if self.__scale == "Celcius":
            return f'{(self.__temperature + 273.15):.2f} Kelvin'
        if self.__scale == "Fahrenheit":
            return f'{((self.__temperature - 32) * 5/9 + 273.15):.2f} Kelvin'
        return f'{self.__temperature:.2f} {self.__scale}'

    # 2. Buatlah sebuah function yang dapat mengkonversi suhu ke fahrenheit. 
    #    Tambahkan parameter untuk memastikan bahwa argumen yang dimasukan adalah 
    #    celcius atau kelvin. Panggil function yang pertama jika diperlukan.
    def ToFahrenheit(self) -> str:
        "method to print the temperature in Fahrenheit scale"
        if self.__scale == "Celcius":
            return f'{((self.__temperature * 9/5) + 32):.2f} Fahrenheit'
        if self.__scale == "Kelvin":
            return f'{(((self.__temperature - 273.15) * 9/5 + 32)):.2f} Fahrenheit'
        return f'{self.__temperature:.2f} Fahrenheit'