import numpy as np

class DataAnalytics:
    def __init__(self, array=None):
        self._array = array

    @property
    def array(self):
        return self._array

    @array.setter
    def array(self, value):
        self._array = value

    @staticmethod
    def _parse_number(value):
        try:
            return int(value)
        except ValueError:
            return float(value)

    @classmethod
    def _read_numbers(cls, prompt, count):
        while True:
            raw = input(prompt).split()
            if len(raw) != count:
                print(f"Please enter exactly {count} elements.")
                continue
            try:
                return [cls._parse_number(v) for v in raw]
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
  
    def create_array(self):
        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                size = int(input("\nEnter the number of elements: "))
                elements = self._read_numbers(
                    f"Enter {size} elements for the array separated by space: ", size)
                arr = np.array(elements)

            case '2':
                rows = int(input("\nEnter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = rows * cols
                elements = self._read_numbers(
                    f"Enter {total} elements for the array separated by space: ", total)
                arr = np.array(elements).reshape(rows, cols)

            case '3':
                depth = int(input("\nEnter the number of blocks: "))
                rows = int(input("Enter the number of rows: "))
                cols = int(input("Enter the number of columns: "))
                total = depth * rows * cols
                elements = self._read_numbers(
                    f"Enter {total} elements for the array separated by space: ", total)
                arr = np.array(elements).reshape(depth, rows, cols)

            case _:
                print("Invalid choice!")
                return

        self._array = arr
        print("\nCreated Array:")
        print(self._array)

        self._index_slice_menu()

    def _index_slice_menu(self):
        while True:
            print("\nChoose an operation:")
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go Back")
            choice = input("Enter your choice: ").strip()

            match choice:
                case '1':
                    self._perform_indexing()
                case '2':
                    self._perform_slicing()
                case '3':
                    break
                case _:
                    print("Invalid choice!")

    def _perform_indexing(self):
        arr = self._array
        try:
            match arr.ndim:
                case 1:
                    idx = int(input("\nEnter the index: "))
                    print(f"\nElement at index {idx}: {arr[idx]}")
                case 2:
                    r = int(input("\nEnter the row index: "))
                    c = int(input("Enter the column index: "))
                    print(f"\nElement at [{r}, {c}]: {arr[r, c]}")
                case 3:
                    d = int(input("\nEnter the block index: "))
                    r = int(input("Enter the row index: "))
                    c = int(input("Enter the column index: "))
                    print(f"\nElement at [{d}, {r}, {c}]: {arr[d, r, c]}")
        except IndexError:
            print("Index out of bounds!")

    def _perform_slicing(self):
        arr = self._array
        try:
            match arr.ndim:
                case 1:
                    rng = input("\nEnter the range (start:end): ")
                    start, end = map(int, rng.split(':'))
                    sliced = arr[start:end]
                case 2:
                    row_rng = input("\nEnter the row range (start:end): ")
                    col_rng = input("Enter the column range (start:end): ")
                    r0, r1 = map(int, row_rng.split(':'))
                    c0, c1 = map(int, col_rng.split(':'))
                    sliced = arr[r0:r1, c0:c1]
                case 3:
                    d_rng = input("\nEnter the block range (start:end): ")
                    row_rng = input("Enter the row range (start:end): ")
                    col_rng = input("Enter the column range (start:end): ")
                    d0, d1 = map(int, d_rng.split(':'))
                    r0, r1 = map(int, row_rng.split(':'))
                    c0, c1 = map(int, col_rng.split(':'))
                    sliced = arr[d0:d1, r0:r1, c0:c1]
                case _:
                    print("Unsupported array dimension!")
                    return
            print("\nSliced Array:")
            print(sliced)
        except (ValueError, IndexError):
            print("Invalid range entered!")

    def math_operations_menu(self):
        if self._array is None:
            print("\nNo array found. Please create an array first.")
            return

        print("\nChoose a mathematical operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")
        print("6. Matrix Multiplication")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1' | '2' | '3' | '4' | '5':
                size = self._array.size
                elements = self._read_numbers(
                    f"\nEnter the same-size array elements "
                    f"({size} elements separated by space): ", size)
                second = np.array(elements).reshape(self._array.shape)

                print("\nOriginal Array:")
                print(self._array)
                print("\nSecond Array:")
                print(second)

                match choice:
                    case '1':
                        print("\nResult of Addition:")
                        print(self._array + second)
                    case '2':
                        print("\nResult of Subtraction:")
                        print(self._array - second)
                    case '3':
                        print("\nResult of Multiplication:")
                        print(self._array * second)
                    case '4':
                        print("\nResult of Division:")
                        print(self._array / second)
                    case '5':
                        print("\nResult of Dot Product:")
                        print(np.dot(self._array, second))

            case '6':
                if self._array.ndim != 2:
                    print("Matrix multiplication requires a 2D array.")
                    return
                rows = int(input("\nEnter number of rows for second matrix: "))
                cols = int(input("Enter number of columns for second matrix: "))
                total = rows * cols
                elements = self._read_numbers(
                    f"Enter {total} elements for the second matrix separated by space: ", total)
                second = np.array(elements).reshape(rows, cols)

                print("\nOriginal Array:")
                print(self._array)
                print("\nSecond Array:")
                print(second)
                try:
                    print("\nResult of Matrix Multiplication:")
                    print(np.matmul(self._array, second))
                except ValueError:
                    print("Incompatible dimensions for matrix multiplication!")

            case _:
                print("Invalid choice!")

    def combine_split_menu(self):
        if self._array is None:
            print("\nNo array found. Please create an array first.")
            return

        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                size = self._array.size
                elements = self._read_numbers(
                    f"\nEnter the elements of another array to combine "
                    f"({size} elements separated by space): ", size)
                second = np.array(elements).reshape(self._array.shape)

                print("\nOriginal Array:")
                print(self._array)
                print("\nSecond Array:")
                print(second)

                combined = np.vstack((self._array, second))
                print("\nCombined Array (Vertical Stack):")
                print(combined)

            case '2':
                print("\nOriginal Array:")
                print(self._array)
                try:
                    splits = int(input("\nEnter the number of equal splits: "))
                    parts = np.array_split(self._array, splits)
                    print("\nSplit Arrays:")
                    for i, part in enumerate(parts, start=1):
                        print(f"\nPart {i}:")
                        print(part)
                except ValueError as e:
                    print(f"Error: {e}")

            case _:
                print("Invalid choice!")

    def search_sort_filter_menu(self):
        if self._array is None:
            print("\nNo array found. Please create an array first.")
            return

        print("\nChoose an option:")
        print("1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")
        choice = input("Enter your choice: ").strip()

        print("\nOriginal Array:")
        print(self._array)

        match choice:
            case '1':
                value = self._parse_number(input("\nEnter the value to search: "))
                indices = np.argwhere(self._array == value)
                if indices.size > 0:
                    print(f"\nValue {value} found at indices:")
                    print(indices)
                else:
                    print(f"\nValue {value} not found in the array.")

            case '2':
                sorted_arr = np.sort(self._array, axis=-1)
                print("\nSorted Array:")
                print(sorted_arr)
                print("(Sorting applied row-wise.)")

            case '3':
                condition = input(
                    "\nEnter a condition (e.g. > 20, <= 40, == 10): ").strip()
                try:
                    operator, value_str = condition.split()
                    value = self._parse_number(value_str)
                    match operator:
                        case '>':
                            mask = self._array > value
                        case '<':
                            mask = self._array < value
                        case '>=':
                            mask = self._array >= value
                        case '<=':
                            mask = self._array <= value
                        case '==':
                            mask = self._array == value
                        case '!=':
                            mask = self._array != value
                        case _:
                            print("Invalid operator! Use one of >, <, >=, <=, ==, !=")
                            return
                    print(f"\nFiltered Values ({condition}):")
                    print(self._array[mask])
                except ValueError:
                    print("Invalid condition format! Use e.g. '> 20'")

            case _:
                print("Invalid choice!")

    def aggregate_stats_menu(self):
        if self._array is None:
            print("\nNo array found. Please create an array first.")
            return

        print("\nChoose an aggregate/statistical operation:")
        print("1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum")
        print("7. Maximum")
        print("8. Percentile")
        print("9. Correlation Coefficient (with another array)")
        choice = input("Enter your choice: ").strip()

        print("\nOriginal Array:")
        print(self._array)

        match choice:
            case '1':
                print(f"\nSum of Array: {np.sum(self._array)}")
            case '2':
                print(f"\nMean of Array: {np.mean(self._array)}")
            case '3':
                print(f"\nMedian of Array: {np.median(self._array)}")
            case '4':
                print(f"\nStandard Deviation of Array: {np.std(self._array)}")
            case '5':
                print(f"\nVariance of Array: {np.var(self._array)}")
            case '6':
                print(f"\nMinimum Value: {np.min(self._array)}")
            case '7':
                print(f"\nMaximum Value: {np.max(self._array)}")
            case '8':
                try:
                    p = float(input("\nEnter the percentile (0-100): "))
                    print(f"\n{p}th Percentile: {np.percentile(self._array, p)}")
                except ValueError:
                    print("Invalid percentile value!")
            case '9':
                size = self._array.size
                elements = self._read_numbers(
                    f"\nEnter the elements of another array "
                    f"({size} elements separated by space): ", size)
                second = np.array(elements).reshape(self._array.shape)
                print("\nSecond Array:")
                print(second)
                corr = np.corrcoef(self._array.flatten(), second.flatten())[0, 1]
                print(f"\nCorrelation Coefficient: {corr}")
            case _:
                print("Invalid choice!")

    @classmethod
    def about(cls):
        return ("DataAnalytics: a NumPy-powered toolkit combining array "
                "operations with Object-Oriented Programming principles.")


def main():
    analyzer = DataAnalytics()

    print("Welcome to the NumPy Analyzer!")
    print("=" * 40)

    while True:
        print("\nChoose an option:")
        print("1. Create a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()

        match choice:
            case '1':
                analyzer.create_array()
            case '2':
                analyzer.math_operations_menu()
            case '3':
                analyzer.combine_split_menu()
            case '4':
                analyzer.search_sort_filter_menu()
            case '5':
                analyzer.aggregate_stats_menu()
            case '6':
                print("\nThank you for using the NumPy Analyzer! Goodbye!")
                break
            case _:
                print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
