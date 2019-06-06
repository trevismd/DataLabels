from datetime import datetime, time


class Cbct:
    def __init__(self, **kwargs):
        self.date = kwargs["date"]
        self.time = datetime.strptime(kwargs["time"], "%H%M").strftime("%H:%M")
        # self.time = time(int(kwargs["time"][:2]), int(kwargs["time"][3:]))
        self.comment = kwargs["comment"]
        self.treatment = kwargs["treatment"]

    def same_date(self, cbct):
        if self.date == cbct.date:
            return True
        return False

    def same_treatment(self, cbct):
        if self.treatment == cbct.treatment:
            return True
        return False

    def __repr__(self):
        return "For treatment #%s on date %s at %s with comment :\"%s\"" % (
            self.treatment, self.date, self.time, self.comment
        )

    def get_look_str(self):
        return "For treatment #%s on date %s at %s with comment :\n\n\t %s\n\n"\
               % (self.treatment, self.date, self.time, self.comment)