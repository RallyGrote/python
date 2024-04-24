import pytest
from television import Television

def test_init() -> None:
    """
    tests the __init__ function in the television class
    """
    test_tv = Television()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_power() -> None:
    """
    tests the power function in the television class
    """
    test_tv = Television()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_mute() -> None:
    """
    tests the mute function in the television class
    """
    test_tv = Television()
    test_tv.power()
    test_tv.volume_up()
    test_tv.mute()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
    test_tv.volume_up()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 2'
    test_tv.power()
    test_tv.mute()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 2'
    test_tv.mute()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 2'

def test_channel_up() -> None:
    """
    tests the channel_up function in the television class
    """
    test_tv = Television()
    test_tv.channel_up()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    test_tv.channel_up()
    assert test_tv.__str__() == 'Power = True, Channel = 1, Volume = 0'
    test_tv.channel_up()
    test_tv.channel_up()
    test_tv.channel_up()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_channel_down() -> None:
    """
    tests the channel_down function in the television class
    """
    test_tv = Television()
    test_tv.channel_down()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    test_tv.channel_down()
    assert test_tv.__str__() == 'Power = True, Channel = 3, Volume = 0'

def test_volume_up() -> None:
    """
    tests the volume_up function in the television class
    """
    test_tv = Television()
    test_tv.volume_up()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    test_tv.volume_up()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
    test_tv.mute()
    test_tv.volume_up()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 2'
    test_tv.volume_up()
    test_tv.volume_up()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 2'

def test_volume_down() -> None:
    """
    tests the volume_down function in the television class
    """
    test_tv = Television()
    test_tv.volume_up()
    test_tv.volume_up()
    test_tv.volume_down()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    test_tv.volume_up()
    test_tv.volume_up()
    test_tv.volume_down()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 1'
    test_tv.mute()
    test_tv.volume_down()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'
    test_tv.volume_down()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

