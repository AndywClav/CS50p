from datetime import date, datetime
import inflect
import sys

class MinutesLived:
    def __init__(self, value_date: str) -> None:
        value_date: str = value_date.replace(",", "-")

        try:
            self.parsed_date: date = datetime.strptime(value_date, "%Y-%m-%d").date()
        except ValueError:
            sys.exit("Invalid date format.")

        if self.parsed_date > datetime.now().date():
             sys.exit("Date cannot be in the future.")


    def minutes_lived(self) -> int:
        current_date: date = date.today()

        birth_datetime: datetime = datetime.combine(self.parsed_date, datetime.min.time())
        current_datetime: datetime = datetime.combine(current_date, datetime.min.time())
        difference: date = current_datetime - birth_datetime
        return int(difference.total_seconds() // 60)


    def __str__(self) -> str:
        p: inflect.engine = inflect.engine()
        minutes: int = self.minutes_lived()

        minutes_in_words: str = p.number_to_words(minutes, andword="").capitalize()
        return f"{minutes_in_words} minutes"


def main() -> None:
    try:
        birth_date: str = MinutesLived(input("Date of Birth: ").strip())
        print(birth_date)
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
