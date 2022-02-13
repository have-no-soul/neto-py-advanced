from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import date


def main():
    print(f'{date.today()}')
    calculate_salary()
    get_employees()


if __name__ == "__main__":
    main()
