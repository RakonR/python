#docstrings are like comments but even worse somehow

class Television:
    """
    A class representing a Television with basic functionality.
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Initialize the Television instance with default settings.
        """
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
        self.saved_volume = self.MIN_VOLUME

    def power(self):
        """
        Toggle the TV's power status.
        """
        self.status = not self.status

    def mute(self):
        """
        Toggle the TV's mute status.
        If muting, the volume is set to MIN_VOLUME.
        If unmuting, the volume is restored to the saved volume.
        """
        if self.status:
            self.muted = not self.muted
            if self.muted:
                self.saved_volume = self.volume
                self.volume = self.MIN_VOLUME
            else:
                self.volume = self.saved_volume

    def channel_up(self):
        """
        Increase the TV channel by 1.
        If the channel is at MAX_CHANNEL, wrap around to MIN_CHANNEL.
        """
        if self.status:
            self.channel = self.MIN_CHANNEL if self.channel == self.MAX_CHANNEL else self.channel + 1

    def channel_down(self):
        """
        Decrease the TV channel by 1.
        If the channel is at MIN_CHANNEL, wrap around to MAX_CHANNEL.
        """
        if self.status:
            self.channel = self.MAX_CHANNEL if self.channel == self.MIN_CHANNEL else self.channel - 1

    def volume_up(self):
        """
        Increase the TV volume by 1.
        If the TV is muted, unmute it before adjusting the volume.
        """
        if self.status:
            if self.muted:
                self.muted = False
                self.volume = self.saved_volume
            if self.volume < self.MAX_VOLUME:
                self.volume += 1

    def volume_down(self):
        """
        Decrease the TV volume by 1.
        If the TV is muted, unmute it before adjusting the volume.
        """
        if self.status:
            if self.muted:
                self.muted = False
                self.volume = self.saved_volume
            if self.volume > self.MIN_VOLUME:
                self.volume -= 1

    def __str__(self):
        """
        Return a string representation of the Television's state.
        """
        return f"Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}"
