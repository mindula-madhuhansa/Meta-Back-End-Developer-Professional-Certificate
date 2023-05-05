# read text file, print and return
def read_file(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
    return content


# append sentences to a list and return
def read_file_into_list(file_name):
    with open(file_name, "r") as file:
        content = file.readlines()
    return content


# write first sentence to another file
def write_first_line_to_file(file_contents, output_filename):
    with open(output_filename, "w") as file:
        sentences = file_contents.split("\n")
        file.write(sentences[0])


# even numbered lines append to a list and return
def read_even_numbered_lines(file_name):
    with open(file_name, "r") as file:
        sentences = file.readlines()
        even_list = []

        for index, line in enumerate(sentences):
            if index % 2 != 0:
                if index == 0:
                    continue
                else:
                    even_list.append(line)

    return even_list


# append sentence to a list in reverse and return
def read_file_in_reverse(file_name):
    with open(file_name, "r") as file:
        sentences = file.readlines()
        sentences.reverse()
    return sentences


def main():
    file_contents = read_file("sampletext.txt")
    print(read_file_into_list("sampletext.txt"))
    write_first_line_to_file(file_contents, "online.txt")
    print(read_even_numbered_lines("sampletext.txt"))
    print(read_file_in_reverse("sampletext.txt"))


if __name__ == "__main__":
    main()
