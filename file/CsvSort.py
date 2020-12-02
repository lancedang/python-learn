"""
针对只有一列的csv文件进行排序
"""


def sort():
    input_file = open("test-sort.csv")
    output_file = open("sort-result.csv", "a")

    table = []

    for line in input_file:
        col = int(line.strip())
        table.append(col)

    table.sort(reverse=True)

    for item in table:
        output_file.write(str(item) + '\n')


if __name__ == '__main__':
    sort()
