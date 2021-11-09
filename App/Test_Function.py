import config as cf
import xlsxwriter
import view
assert cf

def TestFunction():

    test_inputs = { 1: ('las vegas', 0, 0, 0),
                    2: (30, 150, 0, 0),
                    3: ('20:45:00', '23:15:00', 0, 0),
                    4: ('1945-08-06', '1984-11-15', 0, 0),
                    5: (-109.05, -103, 31.33, 37),
                    6: (-109.05, -103, 31.33, 37)}
    test_data = {   8032: test_inputs,
                    16066: test_inputs,
                    24099: test_inputs,
                    32132: test_inputs,
                    40166: test_inputs,
                    48199: test_inputs,
                    56232: test_inputs,
                    64265: test_inputs,
                    72298: test_inputs,
                    80332: test_inputs}

    workbook   = xlsxwriter.Workbook('Test_Data.xlsx')
    worksheet = workbook.add_worksheet()

    initial_index = 3
    for data_size in test_data:
        test_data_size = test_data[data_size]
        print(30*'#' + ' ' + str((initial_index - 2)*10) + '% Test ' + 30*'#')
        catalog = view.UserProgram(True, 0, None, data_size, 0, 0, 0)
        for function in test_data_size:
            definitve_index = 'D' + str(initial_index + (function - 1)*11)
            function_inputs = test_data_size[function]
            input_1 = function_inputs[0]
            input_2 = function_inputs[1]
            input_3 = function_inputs[2]
            input_4 = function_inputs[3]

            summation_elapsed_time = 0
            print(20*'=' + ' Function ' + str(function) + ' Test ' + 20*'=')
            for test in range(0,5):
                print(10*'-' + ' Test No.' + str(test + 1) + ' ' + 10*'-')
                elapsed_time = view.UserProgram(True, function, catalog, input_1, input_2, input_3, input_4)
                summation_elapsed_time += elapsed_time

            mean_elapsed_time = summation_elapsed_time/5
            worksheet.write(definitve_index, mean_elapsed_time)
        initial_index += 1

    workbook.close()

TestFunction()
