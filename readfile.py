def read_file(filename):
    # Open the file
    with open(filename, "r") as file:
        content = file.read()
        string_nums = content.split()
        return list(map(int, string_nums))


if __name__ == "__main__":

    fileNames = ["rand1000.txt", "rand10000.txt"]
    for name in fileNames:
        data = read_file(name)
        print(f"Loaded {len(data)} numbers")
        print(f"First 10 numbers: {data[:10]}")
