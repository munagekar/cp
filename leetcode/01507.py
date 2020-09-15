class Solution:
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split(' ')

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_dict = {m: i for i, m in enumerate(months, 1)}

        d = int(day[:-2])
        m = month_dict[month]

        return f"{year}-{m:02}-{d:02}"