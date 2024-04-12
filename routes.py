from main import app, JSONResponse

from controllers.bingo_controller import Bingo

bingo_controller = Bingo()

def parse_result(response, **kwargs):
    try:
        return JSONResponse(content={"response": response}, media_type="application/json", **kwargs)
    except Exception as err:
        return JSONResponse(content=err, status_code=500)

@app.get("/")
def get_bingo():
    return bingo_controller.get_bingo()

@app.get("/card")
def get_card():
    card = bingo_controller.get_card()
    return parse_result(card, status_code=201)

@app.get("/number")
def get_number():
    number = bingo_controller.get_drawn_numbers()
    return parse_result(number, status_code=200)

@app.get("/number/list")
def get_numbers_list():
    numbers, percentage = bingo_controller.get_drawn_numbers_list_and_percentage()
    return parse_result({"numbers": numbers, "percentage": percentage}, status_code=200)

@app.get("/bingo/has-bingo")
def get_bingo():
    bingo = bingo_controller.has_bingo()
    return parse_result(bingo)