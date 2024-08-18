import calendar
from datetime import datetime, timedelta


class DateRangeHelper:
    @classmethod
    def get_start_and_end_of_week(cls, date_str):
        """
        Get the start and end dates of the week for a given date.

        Args:
            date_str (str): A date in 'YYYY-MM-DD' format.

        Returns:
            tuple: A tuple containing two `datetime.date` objects:
                - Start of the week.
                - End of the week.

        Example:
            >>> DateRangeHelper.get_start_and_end_of_week('2024-08-15')
            (datetime.date(2024, 8, 12), datetime.date(2024, 8, 18))
        """
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        start_of_week = given_date - timedelta(days=given_date.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        return start_of_week, end_of_week

    @classmethod
    def get_first_and_last_day_of_month(cls, date_str):
        """
        Get the first and last dates of the month for a given date.

        Args:
            date_str (str): A date in 'YYYY-MM-DD' format.

        Returns:
            tuple: A tuple containing two `datetime.date` objects:
                - First day of the month.
                - Last day of the month.

        Example:
            >>> DateRangeHelper.get_first_and_last_day_of_month('2024-08-15')
            (datetime.date(2024, 8, 1), datetime.date(2024, 8, 31))
        """
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        first_day = given_date.replace(day=1)
        _, last_day = calendar.monthrange(given_date.year, given_date.month)
        last_day = given_date.replace(day=last_day)
        return first_day, last_day

    @classmethod
    def get_first_and_last_day_of_year(cls, date_str):
        """
        Get the first and last dates of the year for a given date.

        Args:
            date_str (str): A date in 'YYYY-MM-DD' format.

        Returns:
            tuple: A tuple containing two `datetime.date` objects:
                - First day of the year.
                - Last day of the year.

        Example:
            >>> DateRangeHelper.get_first_and_last_day_of_year('2024-08-15')
            (datetime.date(2024, 1, 1), datetime.date(2024, 12, 31))
        """
        given_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        first_day_of_year = datetime(given_date.year, 1, 1).date()
        last_day_of_year = datetime(given_date.year, 12, 31).date()
        return first_day_of_year, last_day_of_year
