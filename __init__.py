from mycroft import MycroftSkill, intent_file_handler


class NetworkOtimization(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('otimization.network.intent')
    def handle_otimization_network(self, message):
        self.speak_dialog('otimization.network')


def create_skill():
    return NetworkOtimization()

