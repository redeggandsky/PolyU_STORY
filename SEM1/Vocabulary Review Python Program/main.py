from controller import Controller
from model import Model
# coding=utf-8
def main():
    model = Model()
    model.init()
    controller = Controller(model)
    try:
        controller.run()
    except Exception:
        print("Program Exit!\n")
    finally:
        model.writefile()
main()