from data_loader import load_data
from analysis import process_age_data_over_time

def main():
    file_path = 'lesson_10\data_app\data\data_nairne.csv'
    data = load_data(file_path)

    if data is not None:
        age_summary_over_time = process_age_data_over_time(data)
        print(age_summary_over_time)

if __name__ == "__main__":
    main()