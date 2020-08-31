import os
import unittest
import threading
import time

from intel_task_2.representer import list_files


dir_path = os.path.dirname(os.path.realpath(__file__))
ex1_path = os.path.join(dir_path, 'ex_1.txt')
ex2_path = os.path.join(dir_path, 'ex_2.txt')
ex3_path = os.path.join(dir_path, 'ex_3.txt')


class TestRepresenter(unittest.TestCase):
    def setUp(self):
        self.t_stop = threading.Event()
        self.out_list = []

    def test_stop_iteration_handling(self):
        t = threading.Thread(target=list_files, args=[ex3_path],
                             kwargs={'stop_event': self.t_stop, 'output': self.out_list})
        t.start()
        time.sleep(0.01)
        self.t_stop.set()
        self.assertGreater(len(self.out_list), 2)
        self.assertEqual(self.out_list[2], '-')

    def test_three_files(self):
        t = threading.Thread(target=list_files, args=[ex1_path, ex2_path, ex3_path],
                             kwargs={'stop_event': self.t_stop, 'output': self.out_list})
        t.start()
        time.sleep(0.01)
        self.t_stop.set()
        self.assertEqual(self.out_list[:15],
                         ['1', 'A', '-', '2', 'B', '+', '3', 'C', '-', '1', 'D', '+', '2', 'A', '-'])

    def test_duplicated_file(self):
        t = threading.Thread(target=list_files, args=[ex1_path, ex1_path],
                             kwargs={'stop_event': self.t_stop, 'output': self.out_list})
        t.start()
        time.sleep(0.01)
        self.t_stop.set()
        self.assertEqual(self.out_list[:8], ['1', '1', '2', '2', '3', '3', '1', '1'])


if __name__ == "__main__":
    unittest.main()
