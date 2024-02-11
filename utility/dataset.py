import pandas as pd



class SubwayDataset:
    def __init__(self) -> None:
        self.subway_lines_dataset = pd.DataFrame(
            columns=[
                "stationname","datetime","input",
                "output", "peopleinsidetrain"
        ])
    
    
    def append(self, record):
        self.subway_lines_dataset = \
            self.subway_lines_dataset.append(record, ignore_index=True)
    
    
    def save(self, filename="subway_dataset.csv"):
        self.subway_lines_dataset.to_csv(filename)

    def describe(self):
        print(self.subway_lines_dataset.describe())