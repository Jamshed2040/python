class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self) -> None:
        """
        Initialize the default instance variables
        """
        self.__status = False
        self.__muted = False
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME

    def power(self):
        """turn tv on or off"""
        self.__status = not self.__status


    def mute(self) -> None:
        """
        Mute when the TV is on
        """
        if self.__status:
            self.__muted = not self.__muted


    def channel_up(self):
        """Only change the channel if the TV is on"""

        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        """
        Method to decrease the tv channel.
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        """Method for changing volume up if TV is on"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Method for changing volume if TV is on"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to show the tv status.
        :return: tv status.
        """
        power_status = "On" if self.__status else "Off"
        channel_status = self.__channel if self.__status else "0"
        volume_status = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {power_status}, Channel = {channel_status}, Volume = {volume_status}"
