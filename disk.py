class Disk:
    def __init__(self, total, used):
        self.total = total
        self.used = used

    @property
    def free(self):
        return self.total - self.used

    @property
    def used_perc(self):
        return self.used / self.total

    def __str__(self):
        return f"Disk[total: {self.total} Gb, used: {self.used} Gb]"

    def __lt__(self, other):
        return self.used_perc < other.used_perc

