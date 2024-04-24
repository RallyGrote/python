class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self) -> None:
        """
        Method to set default values of television object.
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__mute_volume = Television.MIN_VOLUME

    def power(self) -> None:
        """
        Turns the television on/off
        """
        if self.__status:
            self.__status = False
        else:
            self.__status = True

    def mute(self) -> None:
        """
        Saves the volume then sets it to 0 if muted is false
        otherwise sets volume to the previously saved volume
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__mute_volume
            else:
                self.__muted = True
                self.__mute_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
        else:
            pass

    def channel_up(self) -> None:
        """
        Sets the channel up one value. If called while at the maximum
        channel, sets the channel to the minimum channel
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1
        else:
            pass
    def channel_down(self) -> None:
        """
        Sets the channel down one value. If called while at the minimum
        channel, sets the channel to the maximum channel
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
        else:
            pass

    def volume_up(self) -> None:
        """
        Sets the volume up one value. If volume is at the maximum
        volume, then the volume is unaffected
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__mute_volume
            if self.__volume == Television.MAX_VOLUME:
                pass
            else:
                self.__volume += 1
        else:
            pass

    def volume_down(self) -> None:
        """
        Sets the volume down one value. If volume is at the minimum
        volume, then the volume is unaffected
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__mute_volume
            if self.__volume == Television.MIN_VOLUME:
                pass
            else:
                self.__volume -= 1
        else:
            pass

    def __str__(self) -> str:
        """
        Sets the layout in which a television object will be printed
        """
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'


