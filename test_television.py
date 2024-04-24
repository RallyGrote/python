import pytest
from television import Television

def test_init():
    test_tv = Television()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_power():
    test_tv = Television()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    assert test_tv.__str__() == 'Power = True, Channel = 0, Volume = 0'

def test_mute():
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

def test_channel_up():
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

def test_channel_down():
    test_tv = Television()
    test_tv.channel_down()
    assert test_tv.__str__() == 'Power = False, Channel = 0, Volume = 0'
    test_tv.power()
    test_tv.channel_down()
    assert test_tv.__str__() == 'Power = True, Channel = 3, Volume = 0'

def test_volume_up():
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

def test_volume_down():
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

