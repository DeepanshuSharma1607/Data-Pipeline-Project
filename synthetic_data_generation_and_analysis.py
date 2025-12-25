import numpy as np


class DataCreation:
    """Generate synthetic data for analysis."""

    def Age(self):
        return np.random.randint(18, 60, 10000)

    def Marks(self):
        return np.random.randint(18, 99, 10000)

    def Attendance(self):
        return np.random.randint(50, 100, 10000)

    def SleepHrs(self):
        return np.random.randint(3, 10, 10000)

    def StudyHrs(self):
        return np.random.randint(0, 12, 10000)


class OperationalData(DataCreation):
    """Perform statistical analysis on the dataset."""

    def __init__(self, data_list):
        self.data_list = data_list

    def data_formatting(self):
        self.data = np.vstack(self.data_list).T

    def min_max_mean_val(self):
        self.min_val = np.array([np.min(arr) for arr in self.data_list])
        self.max_val = np.array([np.max(arr) for arr in self.data_list])
        self.mean_val = np.array([np.mean(arr) for arr in self.data_list])

    def display(self):
        self.data_formatting()
        self.min_max_mean_val()
        print(f"Shape: {self.data.shape}")
        print(f"Min: {self.min_val}")
        print(f"Max: {self.max_val}")
        print(f"Mean: {self.mean_val}")


class DataCorruption:
    """Introduce intentional noise or invalid data."""

    def __init__(self, data):
        self.data = data

    def corrupt(self, corruption_rate=0.05):
        size = int(len(self.data) * corruption_rate)
        indices = np.random.choice(len(self.data), size, replace=False)
        for i in indices:
            j = np.random.randint(1, 4)
            if j == 1:
                self.data[i] = 0
            elif j == 2:
                self.data[i] = np.random.randint(-1000, 0)
            else:
                self.data[i] = np.random.randint(100, 1000)
        return self.data


def main():
    np.random.seed(42)
    dc = DataCreation()
    data_list = [dc.Age(), dc.Marks(), dc.Attendance(), dc.SleepHrs(), dc.StudyHrs()]

    print("\n--- Normal Data ---")
    op = OperationalData(data_list)
    op.display()

    # Corrupt data
    corrupted_list = [DataCorruption(arr).corrupt() for arr in data_list]

    print("\n--- Corrupted Data ---")
    op_corrupt = OperationalData(corrupted_list)
    op_corrupt.display()


if __name__ == "__main__":
    main()
