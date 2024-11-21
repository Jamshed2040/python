import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        """setup television instance for testing."""
        self.tv = Television()

    def teardown_method(self):
        """Clean up after each test."""
        del self.tv

    def test_init(self):
        """test the initialization of the television class."""
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

    def test_power(self):
        """Test the power method."""
        self.tv.power()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 0'
        self.tv.power()
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

    def test_mute(self):
        """Test the mute method."""
        # muting when the tv is off (should do nothing)
        self.tv.mute()
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

        # turn on the tv and mute
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 0'

        # Unmute the tv
        self.tv.mute()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 1'

    def test_channel_up(self):
        """Test the channel_up method."""
        # should not change when tv is off
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

        # turn the tv on and test channel changes
        self.tv.power()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = On, Channel = 1, Volume = 0'

        # cycle each channel
        self.tv.channel_up()
        self.tv.channel_up()
        self.tv.channel_up()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 0'

    def test_channel_down(self):
        """Test the channel_down method."""
        # should not change when tv is off
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

        # turn the tv on and test channel changes
        self.tv.power()
        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = On, Channel = 3, Volume = 0'

        self.tv.channel_down()
        assert self.tv.__str__() == 'Power = On, Channel = 2, Volume = 0'

    def test_volume_up(self):
        """Test the volume_up method."""
        # volume should not change when tv is off
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

        # turn on the tv and test volume changes
        self.tv.power()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 1'

        # test max volume
        self.tv.volume_up()
        self.tv.volume_up()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 2'

    def test_volume_down(self):
        """Test the volume_down method."""
        # volume should not change when tv is off
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = Off, Channel = 0, Volume = 0'

        # turn on the tv and test volume changes
        self.tv.power()
        self.tv.volume_up()
        self.tv.volume_up()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 1'

        # test min volume
        self.tv.volume_down()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 0'

        # test unmuting and decreasing volume
        self.tv.mute()
        self.tv.volume_down()
        assert self.tv.__str__() == 'Power = On, Channel = 0, Volume = 0'
