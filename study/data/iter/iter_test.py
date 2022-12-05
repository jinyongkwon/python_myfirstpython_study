test_array = [{"a": 1}, 2, 3, 4, 5]
test_dict = {"a": [1], "b": 2, "c": 3, "d": 4, "e": 5}
test_tuple = (1, 2, 3, 4, 5)
test_str = "12"
test_array_iter = iter(test_array)
test_dict_iter = iter(test_dict)
test_dict_key_iter = iter(test_dict.keys())
test_dict_value_iter = iter(test_dict.values())
test_tuple_iter = iter(test_tuple)
test_str_iter = iter(test_str)
print(f"test_array_iter : {next(test_array_iter)}")
print(f"test_dict_iter : {next(test_dict_iter)}")
print(f"test_dict_key_iter : {next(test_dict_key_iter)}")
print(f"test_dict_value_iter : {next(test_dict_value_iter)}")
print(f"test_tuple_iter : {next(test_tuple_iter)}")
print(f"test_str_iter : {next(test_str_iter)}")
print(f"test_str_iter : {next(test_str_iter)}")
print(f"test_str_iter : {next(test_str_iter)}")
