def read_file(filename):
    # Open the file
    with open(filename, "r") as file:
        content = file.read()
        string_nums = content.split()
        return list(map(int, string_nums))


if __name__ == "__main__":
    data = read_file("rand1000.txt")
    print(f"Loaded {len(data)} numbers")
    print(f"First 10 numbers: {data[:10]}")
