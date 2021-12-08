
class EventQueue():
    def __init__(self):
        self.eventList = []

    def addInputEvent(self, event):
        self.eventList.append(event)

    def removeInputEvent(self, event):
        self.eventList.remove(event)

    def getInputEvent(self, event):
        for i in range(len(self.eventList)):
            if self.eventList[i] == event:
                return True
        return False
