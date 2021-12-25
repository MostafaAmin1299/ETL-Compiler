from app.compiler import parser
from app.gui import ui

def compile():
    try:
        query = str(ui.inputbox.text())
        query = query.lower()
        result = parser.parse(query)
        ui.outputbox.setText(str(result))
    except Exception as e:
        print("Compilation Error.", e)

def execute():
    # try:
        code = str(ui.outputbox.toPlainText())
        exec(code)
        from app import etl
        ui.results.setText(str(etl.result))
    # except Exception as e:
    #     print("Execution Error.", e)