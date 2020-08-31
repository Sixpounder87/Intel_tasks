import threading
import sys
if sys.platform == 'win32':
    from msvcrt import kbhit as key_pressed


def _generator_line(file):
    with open(file) as file_handler:
        for line in file_handler:
            yield line[:-1]


def _call_iterator(gen, output=None):
    val = next(gen)
    print(val) if output is None else output.append(val)


def list_files(*files, stop_event=threading.Event(), output=None):
    file_generator_list = list(map(lambda x: _generator_line(x), files))
    while True:
        if key_pressed() or stop_event.is_set():
            sys.exit()
        for i in range(len(file_generator_list)):
            try:
                _call_iterator(gen=file_generator_list[i], output=output)
            except StopIteration:
                file_generator_list[i] = _generator_line(files[i])
                _call_iterator(gen=file_generator_list[i], output=output)


if __name__ == '__main__':
    var = sys.argv[1:]
    list_files(*var)
