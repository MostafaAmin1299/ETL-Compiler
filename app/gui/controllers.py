from app.compiler import parser
from app.gui import ui
# import time
from timeit import default_timer as timer
from datetime import datetime

def compile():
    global start_time, current_time,result
    current_time = datetime.now().strftime("%H:%M:%S")
    # start_time = time.time()
    start_time = timer()

    try:
        query = str(ui.inputbox.text())
        query = query.lower()
        result = parser.parse(query)
        ui.outputbox.setText(f"Compiling Started at: {current_time} \n \n {result} \n Compilation Process Took: {(timer()-start_time)/1000} Millisecond")
    except Exception as e:
        print("Compilation Error.", e)


def execute():
        current_time = datetime.now().strftime("%H:%M:%S")
        # start_time = time.time()
        start_time = timer()
    # try:
        # code = str(ui.outputbox.toPlainText())
        exec(str(result))
        from app.etl import core
        ui.results.setText(f"Execution Started at {current_time} \n \n{str(core.result)} \n \nExcecution Process Took: {(timer()-start_time)/1000} Millisecond")


    # except Exception as e:
    #     print("Execution Error.", e)
