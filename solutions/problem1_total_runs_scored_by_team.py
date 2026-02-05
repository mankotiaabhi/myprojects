import csv
import matplotlib.pyplot as plt
import os



def total_runs_of_team(file_path):
    result = {}

    with open(file_path,'r',encoding='utf-8') as file:
        match_deliveries = csv.DictReader(file)

        for delivery in match_deliveries:
            batting_team = delivery['batting_team']
            total_runs = int(delivery['total_runs'])

            if batting_team not in result:
                result[batting_team] = 0
            result[batting_team] += total_runs
        return result

def plot(file_path):
    runs_data = total_runs_of_team(file_path)
    # print(runs_data)
    teams = list(runs_data.keys())
    runs = list(runs_data.values())

    os.makedirs("output", exist_ok=True)
    plt.figure(figsize=(12,8))
    plt.bar(teams, runs)

    plt.title("Total Runs Scored by Each Team")
    plt.xlabel("Teams")
    plt.ylabel("Total Runs")

    plt.xticks(rotation=90)
    plt.tight_layout()

    plt.savefig("./output/problem1.png")
    plt.show()

def execute() :
    file_path = "./data/deliveries.csv"
    plot(file_path)



# if __name__ == "__main__":
#     execute()

print(__name__)
