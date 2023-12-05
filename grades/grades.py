class GradingType:
    def __init__(self, lowest_mark, highest_mark, interval=1, viewed_marks = {}):
        self.lowest_mark = lowest_mark
        self.highest_mark = highest_mark
        self.interval = interval
        self.viewed_mark = viewed_marks

class Grade:
    def __init__(self, mark, grading_type):
        self.mark = mark
        self.grading_type = grading_type
        if self.mark < self.grading_type.lowest_mark or self.mark > self.grading_type.highest_mark + 1:
            raise ValueError
        if self.grading_type.interval == 0.5 and self.mark/self.grading_type.interval != round(self.mark/self.grading_type.interval):
            raise ValueError
        if self.grading_type.interval == 1 and isinstance(self.mark, int) is False:
            raise ValueError


    def __lt__(self,other):
        real_value_self = self.mark/(self.grading_type.highest_mark - self.grading_type.lowest_mark)
        real_value_other = other.mark/(other.grading_type.highest_mark - other.grading_type.lowest_mark)
        if real_value_self < real_value_other:
            return True
    