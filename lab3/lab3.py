import cmd
import random
import string
import os
import time
import shlex
import tracemalloc


class Node:
    def __init__(self, item):
        self.Item = item
        self.Next = None
        self.Prev = None


class DoublyLinkedList:
    def __init__(self):
        self.First = None
        self.Last = None
        self.Curr = None

    def is_empty(self):
        return self.First is None

    def set_head(self):
        self.Curr = self.First

    def set_tail(self):
        self.Curr = self.Last

    def next(self):
        if self.Curr != self.Last:
            self.Curr = self.Curr.Next

    def prev(self):
        if self.Curr != self.First:
            self.Curr = self.Curr.Prev

    def get_current(self):
        if self.Curr is not None:
            return self.Curr
        else:
            return None

    def get_next(self):
        if self.Curr is not None and self.Curr.Next is not None:
            return self.Curr.Next
        else:
            return None

    def get_prev(self):
        if self.Curr is not None and self.Curr.Prev is not None:
            return self.Curr.Prev
        else:
            return None

    def get_head(self):
        return self.First

    def get_tail(self):
        return self.Last

    def is_first(self):
        return self.Curr == self.First

    def is_last(self):
        return self.Curr == self.Last

    def add_to_head(self, item):
        node = Node(item)
        if self.is_empty():
            self.First = self.Last = self.Curr = node
        else:
            node.Next = self.First
            self.First.Prev = node
            self.First = node

    def add_to_tail(self, item):
        node = Node(item)
        if self.is_empty():
            self.First = self.Last = self.Curr = node
        else:
            node.Prev = self.Last
            self.Last.Next = node
            self.Last = node

    def insert_before(self, item):
        node = Node(item)
        if self.is_empty():
            self.First = self.Last = self.Curr = node
        else:
            node.Next = self.Curr
            if self.Curr == self.First:
                self.First = node
            else:
                node.Prev = self.Curr.Prev
                self.Curr.Prev.Next = node
            self.Curr.Prev = node

    def insert_after(self, item):
        node = Node(item)
        if self.is_empty():
            self.First = self.Last = self.Curr = node
        else:
            node.Prev = self.Curr
            if self.Curr == self.Last:
                self.Last = node
            else:
                node.Next = self.Curr.Next
                self.Curr.Next.Prev = node

            self.Curr.Next = node

    def search(self, index):
        node = self.First
        counter = 0
        while node:
            if counter == index:
                return node
            counter += 1
            node = node.Next
        return None

    def delete(self, node):
        if node:
            if node == self.First and node == self.Last:
                self.First = self.Last = self.Curr = None
            elif node == self.Last:
                node.Prev.Next = None
                self.Last = node.Prev
                if node == self.Curr:
                    self.Curr = node.Prev
            elif node == self.First:
                node.Next.Prev = None
                self.First = node.Next
                if node == self.Curr:
                    self.Curr = node.Next
            else:
                node.Prev.Next = node.Next
                node.Next.Prev = node.Prev
                if node == self.Curr:
                    self.Curr = node.Next
        else:
            print("Item not found")

    def to_string(self):
        result = ""
        current_node = self.First
        while current_node:
            result += current_node.Item
            current_node = current_node.Next
        return result

    def __call__(self):
        if self.is_empty():
            print([])
        else:
            items = []
            current_node = self.First
            while current_node is not None:
                items.append(current_node.Item)
                current_node = current_node.Next
            print(items)

    def __str__(self):
        if self.is_empty():
            return None
        else:
            items = []
            current_node = self.First
            while current_node is not None:
                items.append(current_node.Item)
                current_node = current_node.Next
            return ''.join(items)


class MyConsole(cmd.Cmd):
    def __init__(self):
        super().__init__()
        self.prompt = "> "
        self.text_folder = "texts"
        self.modified_text_folder = "modified_texts"
        self.statistics_folder = "statistics"
        self.create_folders()
        self.statistics = {
            "doubly_linked_list": {"time": None, "memory": None},
            "dynamic_array": {"time": None, "memory": None}
        }

    def parseline(self, line):
        shortcuts = {
            'in': 'input',
            't': 'text',
            'mod': 'modified',
            'f': 'files',
            'del': 'delete',
            'meth': 'method',
            'st': 'stats',
            'quit': 'exit',
            'h': 'help'
        }
        if line:
            cmd, arg, line = super().parseline(line)
            if cmd in shortcuts:
                return shortcuts[cmd], arg, line
        return super().parseline(line)

    def do_exit(self, arg):
        """Exit the console."""
        print("Exiting the console...")
        return True

    def preloop(self):
        self.do_help("")

    def do_help(self, arg):
        """Get help on commands.

        Usage: help [command]

        If no command is specified, general help is provided.
        """
        super().do_help(arg)

        if not arg:
            print("Available commands:")
            command_list = [
                ("input", "Input text manually or generate text."),
                ("text", "Show the content of the text file."),
                ("modified", "Show the content of the modified text file."),
                ("files", "Show files."),
                ("delete", "Delete a file."),
                ("method", "Execute the specified method."),
                ("stats", "Show statistics."),
                ("exit", "Exit the console."),
            ]
            for command, description in command_list:
                print(f"\t{command}: {description}")

        else:
            if arg == "input":
                print("Usage: input [-m text | -g text_length] [> file_name]")
                print("\t-m: Input text manually.")
                print("\t-g: Generate text.")
                print("\ttext: Text (required for -m).")
                print("\ttext_length: Length of the text to generate (required for -g).")
                print("\tfile_name: Name of the file to save the text to (optional).")
            elif arg == "text":
                print("Usage: text [file_name]")
                print("\tfile_name: Name of the text file to display (optional).")
            elif arg == "modified":
                print("Usage: modified [file_name]")
                print("\tfile_name: Name of the modified text file to display (optional).")
            elif arg == "files":
                print("Usage: files [-t | -m | -s]")
                print("\t-t: Show texts files.")
                print("\t-m: Show modified texts files.")
                print("\t-s: Show statistics files.")
            elif arg == "delete":
                print("Usage: delete [-t | -m | -s] file_name")
                print("\t-t: Delete a text file.")
                print("\t-m: Delete a modified text file.")
                print("\t-s: Delete a statistics file.")
                print("\t-a: Delete a file from all folders.")
            elif arg == "method":
                print("Usage: method [-l | -a] [file_name]")
                print("\t-l: Use doubly linked list.")
                print("\t-a: Use dynamic array.")
                print("\tfile_name: Name of the file to process (optional).")
            elif arg == "stats":
                print("Usage: stats [-t | -m] [file_name]")
                print("\t-t: Show processing time statistics.")
                print("\t-m: Show memory usage statistics.")
                print("\tfile_name: Name of the file to display statistics for (optional).")
            else:
                print("Command not found.")

    def create_folders(self):
        if not os.path.exists(self.text_folder):
            os.makedirs(self.text_folder)
        if not os.path.exists(self.modified_text_folder):
            os.makedirs(self.modified_text_folder)
        if not os.path.exists(self.statistics_folder):
            os.makedirs(self.statistics_folder)

    def do_input(self, arg):
        """Input text manually or generate text."""
        args = shlex.split(arg)
        if "-m" in args:
            if ">" in args:
                self.input_text_manually(args[1], args[3])
            else:
                self.input_text_manually(args[1])
        elif "-g" in args:
            if ">" in args:
                self.generate_text(int(args[1]), args[3])
            else:
                self.generate_text(int(args[1]))
        elif ">" in args:
            self.input_text_manually(args[0], args[2])
        else:
            self.input_text_manually(args[0])

    def input_text_manually(self, text, file_name="text.txt"):
        if text == "":
            print("No text entered.")
            return
        for char in text:
            # If the character is a lowercase Latin letter, print a message
            if not (char.islower() or char == ' '):
                print(f"Character '{char}' is not a lowercase Latin letter.")
                break
        else:
            with open(os.path.join(self.text_folder, file_name), "w") as file:
                file.write(text)
            print(f"Text has been saved to {file_name}.")

    def generate_text(self, n, file_name="text.txt"):
        text = generate_text(n)
        with open(os.path.join(self.text_folder, file_name), "w") as file:
            file.write(text)
        print(f"Generated text with {n} words has been saved to {file_name}.")

    def do_text(self, arg):
        """Show the content of the text file."""
        if arg == "":
            file_name = os.path.join(self.text_folder, "text.txt")
        else:
            file_name = os.path.join(self.text_folder, os.path.splitext(arg)[0] + ".txt")
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                print(file.read())
        else:
            print("File does not exist.")

    def do_modified(self, arg):
        """Show the content of the modified text file."""
        if arg == "":
            file_name = os.path.join(self.modified_text_folder, "text_modified.txt")
        else:
            file_name = os.path.join(self.modified_text_folder, os.path.splitext(arg)[0] + "_modified.txt")
        if os.path.exists(file_name):
            with open(file_name, "r") as file:
                print(file.read())
        else:
            print("File does not exist.")

    def do_files(self, arg):
        """Show files."""
        args = shlex.split(arg)
        if not args:
            print(f"Texts files:")
            for file in os.listdir(self.text_folder):
                print(f"\t{file}")
            print(f"Modified texts files:")
            for file in os.listdir(self.modified_text_folder):
                print(f"\t{file}")
            print(f"Statistics files:")
            for file in os.listdir(self.statistics_folder):
                print(f"\t{file}")
        else:
            if "-t" in args:
                print(f"Texts files:")
                for file in os.listdir(self.text_folder):
                    print(f"\t{file}")
            if "-m" in args:
                print(f"Modified texts files:")
                for file in os.listdir(self.modified_text_folder):
                    print(f"\t{file}")
            if "-s" in args:
                print(f"Statistics files:")
                for file in os.listdir(self.statistics_folder):
                    print(f"\t{file}")

    def do_delete(self, arg):
        """Delete a file."""
        args = shlex.split(arg)
        if "-t" in args:
            file_path = os.path.join(self.text_folder, args[1])
            folder = "text_folder"
        elif "-m" in args:
            file_path = os.path.join(self.modified_text_folder, args[1])
            folder = "modified_text_folder"
        elif "-s" in args:
            file_path = os.path.join(self.statistics_folder, args[1])
            folder = "statistics_folder"
        elif "-a" in args:
            file_path = os.path.join(self.text_folder, args[1])
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File {args[1]} has been deleted from {self.text_folder}.")
            file_path = os.path.join(self.modified_text_folder, args[1][:-4] + "_modified.txt")
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File {args[1][:-4]}_modified.txt has been deleted from {self.modified_text_folder}.")
            file_path = os.path.join(self.statistics_folder, args[1][:-4] + "_stats.txt")
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File {args[1][:-4]}_stats.txt has been deleted from {self.statistics_folder}.")
            return
        else:
            file_path = os.path.join(self.text_folder, args[0])
            folder = "text_folder"
        if os.path.exists(file_path) and len(args) == 1:
            os.remove(file_path)
            print(f"File '{args[0]}' has been deleted from {folder}.")
        elif os.path.exists(file_path) and len(args) == 2:
            os.remove(file_path)
            print(f"File '{args[1]}' has been deleted from {folder}.")
        else:
            print(f"File does not exist.")

    def do_method(self, arg):
        """Execute the specified method."""
        args = shlex.split(arg)
        if args[0] == "-l":
            if len(args) == 2:
                self.show_list(args[1])
            else:
                self.show_list("text.txt")
        elif args[0] == "-a":
            if len(args) == 2:
                self.show_array(args[1])
            else:
                self.show_array("text.txt")

    def show_list(self, file_name="text.txt"):
        text_file_path = os.path.join(self.text_folder,
                                               os.path.splitext(file_name)[0] + ".txt")
        if os.path.exists(text_file_path):
            dll = process_text_doubly_linked_list(self.read_text(file_name))
            tracemalloc.start()
            start_time = time.time()
            modified_text = doubly_linked_list(dll)
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            self.save_statistics("doubly_linked_list", end_time - start_time, (peak - current) / 1024, file_name)

            modified_text_file_path = os.path.join(self.modified_text_folder,
                                                   os.path.splitext(file_name)[0] + "_modified.txt")
            with open(modified_text_file_path, "w") as modified_file:
                modified_file.write(modified_text)
        else:
            print("File does not exist")

    def show_array(self, file_name="text.txt"):
        text_file_path = os.path.join(self.text_folder,
                                      os.path.splitext(file_name)[0] + ".txt")
        if os.path.exists(text_file_path):
            array = process_text_dynamic_array(self.read_text(file_name))
            tracemalloc.start()
            start_time = time.time()
            modified_text = dynamic_array(array)
            end_time = time.time()
            current, peak = tracemalloc.get_traced_memory()
            tracemalloc.stop()
            self.save_statistics("dynamic_array", end_time - start_time, (peak - current) / 1024, file_name)

            modified_text_file_path = os.path.join(self.modified_text_folder,
                                                   os.path.splitext(file_name)[0] + "_modified.txt")
            with open(modified_text_file_path, "w") as modified_file:
                modified_file.write(modified_text)
        else:
            print("File does not exist")

    def do_stats(self, arg):
        """Show statistics."""
        args = shlex.split(arg)
        if not args:
            self.show_all_stats()
        elif len(args) == 1:
            if "-t" not in args and "-m" not in args:
                self.show_all_stats(args[0])
            elif "-t" in args:
                self.show_time()
            elif "-m" in args:
                self.show_memory()
        elif len(args) == 2:
            if "-t" in args and "-m" in args:
                self.show_all_stats()
            elif "-t" in args and "-m" not in args:
                self.show_time(args[1])
            elif "-m" in args and "-t" not in args:
                self.show_memory(args[1])
        else:
            self.show_all_stats(args[2])

    def show_all_stats(self, file_name="text.txt"):
        file_path = os.path.join(self.statistics_folder, os.path.splitext(file_name)[0] + "_stats.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                print(file.read())
        else:
            print("File does not exist.")

    def show_time(self, file_name="text.txt"):
        file_path = os.path.join(self.statistics_folder, os.path.splitext(file_name)[0] + "_stats.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
                print(lines[0].rstrip())
                print(lines[1].rstrip())
                print(lines[2].rstrip(), "\n")
                print(lines[5].rstrip())
                print(lines[6].rstrip())
        else:
            print("File does not exist.")

    def show_memory(self, file_name="text.txt"):
        file_path = os.path.join(self.statistics_folder, os.path.splitext(file_name)[0] + "_stats.txt")
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                lines = file.readlines()
                print(lines[0].rstrip())
                print(lines[1].rstrip())
                print(lines[3].rstrip(), "\n")
                print(lines[5].rstrip())
                print(lines[7].rstrip())
        else:
            print("File does not exist")

    def read_text(self, file_name):
        with open(os.path.join(self.text_folder, file_name), "r") as file:
            return file.read()

    def save_statistics(self, method, time_taken, memory_usage, file_name):
        if method == "doubly_linked_list":
            self.statistics[method]["time"] = time_taken * 1000
            self.statistics[method]["memory"] = memory_usage
        elif method == "dynamic_array":
            self.statistics[method]["time"] = time_taken * 1000
            self.statistics[method]["memory"] = memory_usage

        # Prepare statistics text
        stats_text = []
        stats_text.append(f"File: {file_name}")
        stats_text.append("\tMethod: doubly_linked_list")
        stats_text.append(f"\t\tTime: {self.statistics['doubly_linked_list']['time']} ms")
        stats_text.append(f"\t\tMemory: {self.statistics['doubly_linked_list']['memory']} KB")
        stats_text.append("\n\tMethod: dynamic_array")
        stats_text.append(f"\t\tTime: {self.statistics['dynamic_array']['time']} ms")
        stats_text.append(f"\t\tMemory: {self.statistics['dynamic_array']['memory']} KB")

        # Write statistics to file
        stats_file_path = os.path.join(self.statistics_folder, os.path.splitext(file_name)[0] + "_stats.txt")
        with open(stats_file_path, "w") as file:
            file.write("\n".join(stats_text))


def generate_word():
    length = random.randint(1, 10)
    word = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return word


def generate_text(n):
    text = ' '.join(generate_word() for _ in range(n))
    return text


def process_text_doubly_linked_list(text):
    dll = DoublyLinkedList()
    for symbol in text:
        dll.add_to_tail(symbol)
    return dll


def process_text_dynamic_array(text):
    symbols = list(text)
    return symbols


def doubly_linked_list(dll):
    dll.add_to_tail(' ')
    dll.add_to_tail(' ')
    dll.set_head()
    word_length = 0
    while not dll.is_last():
        if dll.get_current().Item == ' ' and word_length != 0:
            if word_length % 2 != 0:
                for _ in range(word_length):
                    dll.delete(dll.get_prev())
            else:
                for _ in range(word_length):
                    dll.prev()
                for _ in range(word_length):
                    if dll.get_current().Item == 'o':
                        dll.delete(dll.get_current())
                    else:
                        dll.next()
                if dll.get_prev():
                    dll.insert_before(dll.get_prev().Item)
        if dll.get_current().Item == ' ':
            word_length = 0
        else:
            word_length += 1
        dll.next()

    # Removing spaces
    dll.set_head()
    while dll.get_current().Item == ' ':
        dll.delete(dll.get_current())
    while not dll.is_last():
        if dll.get_current().Item == ' ':
            while dll.get_next() and dll.get_next().Item == ' ':
                dll.delete(dll.get_next())
        dll.next()
    while dll.get_current().Item == ' ':
        dll.delete(dll.get_current())

    return dll.to_string()


def dynamic_array(arr):
    arr.append(' ')
    arr.append(' ')
    word_length = 0
    index = 0
    while index < len(arr):
        if arr[index] == ' ' and word_length != 0:
            if word_length % 2 != 0:
                for _ in range(word_length):
                    del arr[index - 1]
                    index -= 1
            else:
                for _ in range(word_length):
                    index -= 1
                for _ in range(word_length):
                    if arr[index] == 'o':
                        del arr[index]
                    else:
                        index += 1
                arr.insert(index, arr[index - 1])
                index += 1
            word_length = 0
        if arr[index] == ' ':
            word_length = 0
        else:
            word_length += 1
        index += 1

    # Removing spaces
    index = 0
    while index < len(arr):
        if arr[index] == ' ':
            while index + 1 < len(arr) and arr[index + 1] == ' ':
                del arr[index + 1]
            if index == 0:
                del arr[index]
            elif index == len(arr) - 1:
                del arr[index]
            else:
                index += 1
        else:
            index += 1

    return ''.join(arr)


def doubly_linked_list2(dll):
    modified_text = ""
    dll.add_to_tail(' ')
    dll.set_head()
    word_length = 0
    last_letter = ''
    while True:
        if dll.get_current().Item == ' ' and word_length != 0:
            if word_length % 2 == 0:
                for i in range(word_length):
                    dll.prev()
                for i in range(word_length):
                    if dll.get_current().Item != 'o':
                        modified_text += dll.get_current().Item
                        last_letter = dll.get_current().Item
                    dll.next()
                modified_text += last_letter + ' '
        if dll.get_current().Item == ' ':
            word_length = 0
        else:
            word_length += 1
        if dll.is_last():
            break
        else:
            dll.next()
    return modified_text.rstrip()


def dynamic_array2(array):
    modified_text = ""
    start_word = 0
    array.append(' ')
    last_letter = ''
    for i in range(len(array)):
        if array[i] == ' ' and i != start_word:
            if (i - start_word) % 2 == 0:
                for letter in array[start_word:i]:
                    if letter != 'o':
                        modified_text += letter
                        last_letter = letter
                modified_text += last_letter + ' '
        if array[i] == ' ':
            start_word = i + 1
    return modified_text.rstrip()


if __name__ == "__main__":
    console = MyConsole()
    console.prompt = "> "
    console.cmdloop("\nWelcome to the console application!\n"
                    "The application processes the text, keeping only words with an even number of letters without the letter 'o' and doubling the last letter.\n")
